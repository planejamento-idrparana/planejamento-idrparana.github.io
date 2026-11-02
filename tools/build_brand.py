"""Gera favicon.svg, apple-touch-icon.png e og-image.png a partir de assets/parana.js.

Uso: py -3 tools/build_brand.py   (requer Google Chrome instalado)
"""
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
GREEN, GREEN2, BLUE, BLUE2, INK = "#009857", "#2fad56", "#0478bc", "#0163ad", "#2b373e"

pr = json.loads((ROOT / "assets/parana.js").read_text(encoding="utf-8")[len("window.PR="):].rstrip().rstrip(";"))
W, H, OUTLINE = pr["w"], pr["h"], pr["outline"]

FAVICON = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><radialGradient id="s" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#2b9be0"/><stop offset="1" stop-color="{BLUE2}"/></radialGradient></defs>
<rect width="64" height="64" rx="14" fill="{GREEN}"/>
<circle cx="40" cy="20" r="11" fill="url(#s)"/>
<path transform="translate(5 17) scale({54 / W:.4f})" d="{OUTLINE}" fill="#fff"/>
</svg>
"""


def og_html() -> str:
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="4.6"/>' for x, y, _ in pr["mun"])
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800&family=Inter:wght@500&display=swap" rel="stylesheet">
<style>
body{{margin:0;width:1200px;height:630px;background:#f6f9f7;font-family:Inter,sans-serif;color:{INK};overflow:hidden;position:relative}}
.l{{position:absolute;left:72px;top:64px;width:520px}}
.brand{{display:flex;align-items:center;gap:18px}}
.brand img{{height:58px}}
.brand b{{font:800 26px Montserrat;letter-spacing:.08em;color:{GREEN};border-left:2px solid #dbe5e0;padding-left:18px}}
h1{{font:800 64px/1.05 Montserrat;margin:96px 0 0;letter-spacing:-.01em}}
h1 em{{font-style:normal;color:{GREEN}}}
.rule{{display:flex;gap:8px;height:7px;width:190px;margin:30px 0 26px}}
.rule:before{{content:"";flex:7;background:{BLUE};transform:skewX(-35deg)}}
.rule:after{{content:"";flex:3;background:{GREEN};transform:skewX(-35deg)}}
.url{{font-size:24px;color:#5d6b73}}
svg{{position:absolute;right:36px;top:130px;width:540px}}
svg circle.m{{fill:{GREEN}}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:14px;background:linear-gradient(90deg,{BLUE} 70%,{GREEN} 70%)}}
</style></head><body>
<div class="l">
  <div class="brand"><img src="{(ROOT / 'assets/logo-idr.webp').as_uri()}"><b>DEPLAN</b></div>
  <h1>Do dado à decisão, <em>em todo o Paraná.</em></h1>
  <div class="rule"></div>
  <div class="url">planejamento-idrparana.github.io</div>
</div>
<svg viewBox="0 0 {W} {H}" style="overflow:visible">
  <defs><radialGradient id="s" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#2b9be0"/><stop offset="1" stop-color="{BLUE2}"/></radialGradient></defs>
  <circle cx="640" cy="20" r="110" fill="url(#s)" opacity=".9"/>
  <path d="{OUTLINE}" fill="#e6f2ea" stroke="{GREEN}" stroke-width="2"/>
  <g fill="{GREEN}" opacity=".85">{dots}</g>
</svg>
<div class="bar"></div>
</body></html>"""


def shot(html: str, out: Path, w: int, h: int) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "p.html"
        page.write_text(html, encoding="utf-8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        f"--window-size={w},{h}", "--virtual-time-budget=5000",
                        f"--user-data-dir={tmp}", f"--screenshot={out}", page.as_uri()],
                       check=True, capture_output=True, timeout=90)
    assert out.exists() and out.stat().st_size > 1000, f"falhou: {out}"


if __name__ == "__main__":
    (ROOT / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    # iOS arredonda sozinho: ícone quadrado e opaco
    touch = FAVICON.replace("<svg ", "<svg width=180 height=180 ").replace('rx="14"', 'rx="0"')
    shot(f'<body style="margin:0">{touch}</body>',
         ROOT / "assets/apple-touch-icon.png", 180, 180)
    shot(og_html(), ROOT / "assets/og-image.png", 1200, 630)
    print("ok: favicon.svg, assets/apple-touch-icon.png, assets/og-image.png")
