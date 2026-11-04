// Conteúdo do ecossistema DEPLAN. Para adicionar um item, inclua um objeto em `itens`.
// Seção: { id, titulo, menu? (rótulo curto no topo), sub, itens }
// Item: { nome, descricao, url, tag }  (sem url = cartão "Em breve", sem link)
// Uma seção pode trocar `itens` por `grupos: [{ titulo, itens }]` (subdivisões).
window.ECOSSISTEMA = [
  {
    id: 'realidade-rural', titulo: 'Realidade Rural',
    sub: 'Retratos do campo paranaense: produção, território e pessoas.',
    itens: [
      {
        nome: 'Datageo Paraná', url: 'https://datageoparana.github.io', tag: 'Plataforma pública',
        descricao: '10 painéis interativos sobre preços, produção, crédito rural, comércio exterior, emprego e demografia, com dados oficiais (DERAL/SEAB, BCB, MDIC, IBGE).',
      },
      {
        nome: 'DGP-Comando', url: 'https://dgp-comando.github.io', tag: 'Sala de Situação',
        descricao: 'Sala de Situação do Paraná: mapa e globo com mais de 80 camadas de dados dos 399 municípios.',
      },
      {
        nome: 'Programa Água Segura', url: 'https://aguasegura.github.io/mapainterativo/', tag: 'Mapa interativo',
        descricao: 'Microbacias de abastecimento público do Paraná: 98 ottobacias, 44 mananciais e 22 regionais. Parceria IDR-Paraná e SANEPAR.',
      },
      { nome: 'Painéis interativos Realidade Rural', tag: 'Painéis BI' },
      { nome: 'Mapas e indicadores territoriais', descricao: 'Recortes por município e regional para leitura do território rural.' },
    ],
  },
  {
    id: 'monitoramento', titulo: 'Monitoramento e Relatórios', menu: 'Monitoramento',
    sub: 'Acompanhamento das ações e resultados do Instituto.',
    // relatórios situacionais: versões públicas geradas por tools/publicar_relatorios.py
    // e, para os projetos, por erva-mate/scripts/getec/07_relatorio_publico.py
    grupos: [
      {
        titulo: 'Prestação de contas',
        itens: [
          {
            nome: 'Balanço Social IDR-Paraná 2025', url: 'https://balanco-social-idrparana.github.io/', tag: 'Balanço Social',
            descricao: 'Relatório de impactos das ações e tecnologias do IDR-Paraná, com a metodologia Ambitec-Agro, como prestação de contas à sociedade paranaense.',
          },
        ],
      },
      {
        titulo: 'Programas e políticas públicas',
        itens: [
          {
            nome: 'Leite das Crianças 2026', url: 'relatorios/leite-das-criancas.html', tag: 'Relatório situacional',
            descricao: 'Cobertura da ATER junto aos 2.860 produtores que fornecem leite ao Programa Leite das Crianças, por núcleo, município e laticínio.',
          },
          {
            nome: 'Leite das Crianças, safra 2025/26', url: 'relatorios/leite-das-criancas-safra-2025-26.html', tag: 'Relatório situacional',
            descricao: 'O mesmo retrato do programa, com os atendimentos de ATER restritos à janela da safra 2025/26.',
          },
          {
            nome: 'Compra Direta 2025/26', url: 'relatorios/compra-direta-2025-26.html', tag: 'Relatório situacional',
            descricao: 'As 188 organizações da agricultura familiar contratadas na Compra Direta e o alcance da ATER do IDR-Paraná junto a elas.',
          },
          {
            nome: 'Merenda da agricultura familiar e o CAF', url: 'relatorios/merenda-agricultura-familiar-caf.html', tag: 'Relatório situacional',
            descricao: 'Fornecedoras da Chamada Pública do Fundepar, sua situação no CAF e os agricultores associados ainda fora do cadastro.',
          },
        ],
      },
      {
        titulo: 'Públicos e cadeias produtivas',
        itens: [
          {
            nome: 'Agroecologia e produção orgânica', url: 'relatorios/agroecologia-organicos.html', tag: 'Relatório situacional',
            descricao: 'Produtores orgânicos certificados do Paraná (CNPO) comparados à agricultura familiar e à ATER agroecológica do IDR-Paraná.',
          },
          {
            nome: 'ATER ao público 60+', url: 'relatorios/ater-idosos.html', tag: 'Relatório situacional',
            descricao: 'Ações de assistência técnica e extensão rural com pessoas de 60 anos ou mais, de janeiro de 2024 a agosto de 2026.',
          },
          {
            nome: 'Floresce Paraná: flores e plantas ornamentais', url: 'relatorios/plantas-ornamentais.html', tag: 'Relatório situacional',
            descricao: 'Diagnóstico da cadeia de flores e plantas ornamentais: produção, empresas, RENASEM, mercado e lacunas da ATER.',
          },
        ],
      },
      {
        titulo: 'Execução da ATER (GETEC)',
        itens: [
          {
            nome: 'Eventos de ATER, 1º semestre de 2026', url: 'relatorios/eventos-ater-2026-s1.html', tag: 'Relatório situacional',
            descricao: '6.085 eventos de extensão rural registrados no GETEC/SISATER, lidos por método, programa, território e público.',
          },
          {
            nome: 'Projetos do IDR-Paraná', url: 'relatorios/projetos/indice.html', tag: 'Um relatório por projeto',
            descricao: 'Série 2016 a 2026 de cada projeto do GETEC, com público por região e município e grupos de assistidos.',
          },
          {
            nome: 'ATER no Paraná, 2018 a 2026', url: 'relatorios/getec-ater-2018-2026.html', tag: 'Relatório situacional',
            descricao: 'Produtores atendidos e assistidos, métodos individuais e grupais e crédito rural, previsto e realizado, por regional.',
          },
          {
            nome: 'Equivalente técnico, 2018 a 2026', url: 'relatorios/getec-equivalente-tecnico-2018-2026.html', tag: 'Relatório situacional',
            descricao: 'Força de trabalho em ATER, em extensionistas equivalentes, por regional, por programa e regional × programa.',
          },
        ],
      },
    ],
  },
  {
    id: 'planejamento', titulo: 'Planejamento',
    sub: 'Programas, metas e instrumentos de gestão estratégica.',
    itens: [
      {
        nome: 'GETEC', url: 'http://www.idrgetec.idr.pr.gov.br', tag: 'Sistema institucional',
        descricao: 'Sistema de Gestão Técnica do IDR-Paraná, para registro e acompanhamento das atividades técnicas.',
      },
      {
        nome: 'Arranjos Regionais 2027', url: 'https://arranjos-regionais-idr.github.io', tag: 'Acesso restrito',
        descricao: 'Montagem dos arranjos regionais de 2027: cada regional combina cadeias produtivas, áreas transversais, público, municípios e equipe, com acesso por código da DEPLAN.',
      },
    ],
  },
  {
    id: 'ferramentas', titulo: 'Ferramentas e Instrumentos de ATER', menu: 'Ferramentas de ATER',
    sub: 'Instrumentos de apoio ao trabalho técnico nas propriedades.',
    itens: [
      { nome: 'Planejamento Integrado da Propriedade' },
      { nome: 'Projetos e propostas técnicas para as propriedades' },
      { nome: 'Crédito Rural' },
      { nome: 'SIGEAP', descricao: 'Leite.' },
      { nome: 'SAFE', descricao: 'Energias renováveis, crédito rural, eventos e capacitações.' },
    ],
  },
  {
    id: 'gestao-ater', titulo: 'Gestão de ATER',
    sub: 'Rede, diagnóstico, projetos, referências e normas da extensão rural.',
    itens: [
      {
        nome: 'Rede Paranaense de ATER', url: 'https://rededeaterparana.github.io', tag: 'Rede estadual',
        descricao: 'Rede de entidades de Assistência Técnica e Extensão Rural do Paraná, com cadastro de adesão e mapa da capacidade instalada.',
      },
      { nome: 'Diagnóstico da ATER' },
      { nome: 'Elaboração de Projetos e Precificação de ATER' },
      { nome: 'Coletânea sobre Extensão Rural' },
      { nome: 'Legislação e normativos' },
      { nome: 'Apresentações' },
    ],
  },
];
