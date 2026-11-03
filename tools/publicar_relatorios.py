"""Gera as versões públicas dos relatórios situacionais em relatorios/.

Os originais (uso interno) ficam em E:\\ e não são alterados. Este script copia cada
relatório, remove dados pessoais de terceiros e trava se sobrar algum identificador.

Uso: py -3 tools/publicar_relatorios.py
"""
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "relatorios"
E = Path("E:/")
DEC = json.JSONDecoder()

# campos de produtor que o relatório do Leite usa fora da tabela nominal (que não é exibida)
LC_CAMPOS = ("nucleo", "municipio", "laticinios", "localizado","atendido", "n_atend",
             "n_prog", "horas", "programas", "quantidade", "recencia", "frequencia",
             "dap", "caf_status")
PESSOA = re.compile(r"\d{11}|@|^\d{2}\.\d{3}\.\d{3} ")  # CPF no nome, e-mail ou padrão MEI
PJ = re.compile(r"\b(LTDA|S\.A\b|S/A\b|SA$|SOCIEDADE|COOPERATIVA|COOP\b|ASSOCIA|SINDICATO|FUNDA[CÇ]|"
                r"INSTITUTO|COMPANHIA|CIA\b|CONSORCIO|CONDOMINIO|IGREJA|PREFEITURA|MUNICIPIO|"
                r"EMPRESA|SERVICO|UNIVERSIDADE|FEDERACAO|CENTRAL|COMERCIO|INDUSTRIA)", re.I)


def json_em(texto: str, marcador: str):
    """Localiza o literal JSON logo após `marcador` e devolve (objeto, início, fim)."""
    m = re.search(re.escape(marcador.strip()).replace(r"\ ", r"\s*") + r"\s*", texto)
    assert m, f"marcador ausente: {marcador}"
    i = m.end()
    obj, n = DEC.raw_decode(texto[i:])
    return obj, i, i + n


def troca(texto: str, marcador: str, fn) -> str:
    obj, i, j = json_em(texto, marcador)
    return texto[:i] + json.dumps(fn(obj), ensure_ascii=False, separators=(",", ":")) + texto[j:]


def leite(t: str) -> str:
    def dados(d):
        rnd = random.Random(42)
        prods = [{k: p.get(k) for k in LC_CAMPOS} for p in d["produtores"]]
        # A página só cruza laticínio com núcleo (cartões) e município com atendimento (mapas).
        # Sortear os laticínios dentro do núcleo mantém essas contagens exatas e desfaz o
        # vínculo laticínio + município + histórico de ATER de um produtor específico.
        por_nucleo = {}
        for p in prods:
            por_nucleo.setdefault(p["nucleo"], []).append(p)
        for grupo in por_nucleo.values():
            lats = [p["laticinios"] for p in grupo]
            rnd.shuffle(lats)
            for p, lat in zip(grupo, lats):
                p["laticinios"] = lat
        rnd.shuffle(prods)  # ordem original seguia o cadastro
        return {**d, "produtores": prods}

    def perfis(p):
        return {**p, "profiles": [{**x, "municipio": ""} for x in p["profiles"]]}

    if not t.lstrip().lower().startswith("<!doctype"):  # a versão de revisão é um fragmento
        t = ('<!doctype html>\n<meta charset="utf-8">\n'
             '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + t)
    t = sem_revisao(t)
    t = troca(t, "const DATA =", dados)
    return troca(t, "const PROFILES =", perfis) if re.search(r"const PROFILES\s*=", t) else t


def sem_revisao(t: str) -> str:
    """Tira a faixa "Versão para revisão" (fluxo de comentários do Claude), que é interna."""
    t2, n = re.subn(r'\s*<div class="revbar">.*?</p>\s*</div>', "", t, count=1, flags=re.S)
    return t2 if n else t


def compra_direta(t: str) -> str:
    # nomes de representantes e de servidores (gestor e fiscal), protocolo e número do CAF
    # não são usados pela página; organizações (pessoas jurídicas) e valores ficam
    fora = ("representante", "gestor", "fiscal", "protocolo", "contrato", "caf_nr")

    def dados(d):
        return {**d, "cooperativas": [{k: v for k, v in c.items() if k not in fora}
                                      for c in d["cooperativas"]]}

    t = sem_revisao(t)
    t = troca(t, "const DATA =", dados)
    return t.replace(" — v6</title>", "</title>")


def plantas(t: str) -> str:
    def cnpj(c):
        # só pessoa jurídica identificável mantém nome e CNPJ
        regs = [r if PJ.search(r[1]) and not PESSOA.search(f"{r[1]} {r[2]}") else ["", "", "", *r[3:]]
                for r in c["registros"]]
        return {**c, "registros": regs}

    def renasem(r):
        def pj(x):
            return "*" not in x["doc"] and PJ.search(x["nome"]) and not PESSOA.search(x["nome"])
        regs = [x if pj(x) else {**x, "doc": "", "cod": "", "nome": "Pessoa física ou empresário individual"}
                for x in r["registros"]]
        return {**r, "registros": regs}

    t = troca(t, '"cnpj":', cnpj)
    t = troca(t, '"renasem":', renasem)
    return t.replace("sem informação de sócios ou pessoas físicas além do que consta nos "
                     "cadastros públicos",
                     "sem nomes ou documentos de pessoas físicas e empresários individuais")


def xeta(t: str) -> str:
    # nomes de servidores e produtividade individual saem; fica o papel
    trocas = {
        "Genivaldo Pestana (Técnico Agrícola, responsável) e Bruno dos Santos Paschoal":
            "2 técnicos do escritório local",
        "Carlos Roberto Marcolino (70 dos 110), Ana Carolina Bertolaccini, Fernando Cesar Machado":
            "3 extensionistas da unidade",
    }
    for a, b in trocas.items():
        assert a in t, f"trecho não encontrado: {a[:30]}"
        t = t.replace(a, b)
    return t


def getec(t: str) -> str:
    # só totais por regional/programa; tiram-se nomes de tabelas do banco e a menção à conta
    trocas = {
        " com a conta do autor": "",
        " (<code>tb_sap3_1</code>: equivalente técnico, extensionista, município e programa, por ano)": "",
        " (<code>tb_pro</code>)": "",
        "Assessoria de Planejamento": "Departamento de Planejamento",
    }
    for a, b in trocas.items():
        t = t.replace(a, b)
    assert "tb_" not in t and "conta do autor" not in t
    return t


RELATORIOS = {
    "leite-das-criancas.html": ("LC-CD/Relatorio_Leite_Criancas_IDR_v6_revisao.html", leite),
    "leite-das-criancas-safra-2025-26.html": ("LC-CD/Relatorio_Leite_Criancas_IDR_v6_safra_revisao.html", leite),
    "compra-direta-2025-26.html": ("LC-CD/Relatorio_Compra_Direta_IDR_v6.html", compra_direta),
    "eventos-ater-2026-s1.html": ("asplan/Relatorio_Eventos_GETEC_2026S1_IDR.html", None),
    "agroecologia-organicos.html": ("Agroecologia/Relatorio_Agroecologia_Organicos_IDR_padrao.html", None),
    "ater-idosos.html": ("Idosos/Relatorio_Idosos_ATER_IDR_padrao.html", None),
    "merenda-agricultura-familiar-caf.html": ("fundepar/Relatorio_Merenda_AF_CAF_IDR.html", None),
    "plantas-ornamentais.html": ("Plantas Ornamentais/Relatorio-Plantas-Ornamentais-Parana_padrao.html", plantas),
    "getec-ater-2018-2026.html": ("asplan/Relatorio_GETEC_2018-2026.html", getec),
    "getec-equivalente-tecnico-2018-2026.html": ("asplan/Equivalente_Tecnico_GETEC_2018-2026.html", getec),
    # Xetá: dados pessoais já tratados, mas o dossiê cita disputa fundiária e empresa;
    # só entra com aval da chefia
    # "herareka-xeta-paa-2026.html": ("Povos tradicionais/relatorio_herareka_xeta_PAA_2026.html", xeta),
}


def cpf_valido(s: str) -> bool:
    d = [int(c) for c in s]
    if len(set(d)) == 1:
        return False
    return all(sum(d[i] * (n + 1 - i) for i in range(n)) * 10 % 11 % 10 == d[n] for n in (9, 10))


def auditoria(nome: str, t: str) -> None:
    cpfs = [x for x in re.findall(r"(?<![\d.])\d{11}(?![\d.])", t) if cpf_valido(x)]
    cpfs += re.findall(r"(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)", t)
    emails = [e for e in re.findall(r"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}", t) if "@1." not in e]
    chaves = re.findall(r'"(cpf|caf_nr|nis|telefone|email|representante|gestor|fiscal)"\s*:', t)
    nomes = re.findall(r"Genivaldo|Marcolino|Bertolaccini|Paschoal|Ripol", t)
    interno = re.findall(r"Versão(?:&nbsp;| )para(?:&nbsp;| )revisão|@claude|[Uu]so interno", t)
    erros = {k: len(v) for k, v in [("cpf", cpfs), ("email", emails), ("chaves", chaves),
                                    ("servidores", nomes), ("interno", interno)] if v}
    assert not erros, f"{nome}: dados pessoais remanescentes {erros}"


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for destino, (origem, fn) in RELATORIOS.items():
        src = E / origem
        if not src.exists():
            print(f"FALTA {destino:42} <- {src}")
            continue
        t = src.read_text(encoding="utf-8")
        t = fn(t) if fn else t
        t = t.replace("ASPLAN", "DEPLAN")  # a assessoria passou a departamento
        auditoria(destino, t)
        (OUT / destino).write_text(t, encoding="utf-8")
        print(f"ok  {destino:42} {len(t) // 1024:>6} KB  <- {origem}")
