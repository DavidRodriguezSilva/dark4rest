#!/usr/bin/env python3
"""Genera assets/banner.svg: el bosque oscuro con su ciclo de día y noche.

Determinista (semilla fija): correrlo dos veces da el mismo archivo, así que el
diff de un cambio de diseño muestra sólo el cambio. Sin dependencias.

    python3 scripts/banner.py            # escribe assets/banner.svg
    python3 scripts/banner.py salida.svg # o donde se le indique
"""

import math
import random
import sys
from pathlib import Path

W, H = 1200, 400
CICLO = 48  # segundos de un día completo
rnd = random.Random(4)

# Colores de familia: cada app es una luciérnaga en el bosque.
ECO = "#6ddda1"  # dark-echo
OWL = "#c9c3f5"  # dark-owl
KAL = "#e8b14b"  # kalndr


def f(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


def cordillera(base, amplitud, picos, semilla):
    """Silueta de montaña como suma de senos con fase aleatoria."""
    r = random.Random(semilla)
    ondas = [(r.uniform(0.5, 1.0) / (i + 1), (i + 1) * picos, r.uniform(0, 6.3)) for i in range(4)]
    pts = []
    for x in range(0, W + 21, 20):
        t = x / W * math.pi
        y = base - amplitud * sum(a * (0.6 + 0.4 * math.sin(k * t + p)) for a, k, p in ondas)
        pts.append(f"{x},{f(y)}")
    return f"M0,{H} L" + " L".join(pts) + f" L{W},{H} Z"


def pino(x, suelo, alto, ancho):
    """Pino de tres pisos: triángulos superpuestos, el de arriba más angosto."""
    d = []
    for i in range(3):
        top = suelo - alto + i * alto * 0.22
        base = suelo - alto * (0.55 - i * 0.25)
        w = ancho * (0.55 + i * 0.25)
        d.append(f"M{f(x)},{f(top)} L{f(x + w / 2)},{f(base)} L{f(x - w / 2)},{f(base)} Z")
    return "".join(d)


def hilera(suelo, alto, densidad, semilla):
    r = random.Random(semilla)
    d, x = [], -20.0
    while x < W + 20:
        a = alto * r.uniform(0.7, 1.3)
        d.append(pino(x, suelo + r.uniform(-6, 6), a, a * 0.42))
        x += a * 0.42 / densidad
    return "".join(d)


capas_bosque = [
    # (suelo, alto, densidad, color) de atrás hacia adelante
    (268, 46, 1.6, "#1d3230"),
    (300, 62, 1.8, "#15241f"),
    (338, 84, 2.0, "#0e1916"),
    (392, 120, 2.2, "#080f0d"),
]

estrellas = []
for _ in range(90):
    x, y = rnd.uniform(0, W), rnd.uniform(0, 190)
    r = rnd.choice([0.6, 0.8, 1.1])
    estrellas.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{r}"/>')

luciernagas = []
for i in range(26):
    c = [ECO, OWL, KAL][i % 3]
    x, y = rnd.uniform(40, W - 40), rnd.uniform(250, 380)
    dur, delay = rnd.uniform(5, 9), rnd.uniform(0, 6)
    luciernagas.append(
        f'<circle class="lu" cx="{f(x)}" cy="{f(y)}" r="2.2" fill="{c}" '
        f'style="animation-duration:{f(dur)}s,{CICLO}s;animation-delay:-{f(delay)}s,0s"/>'
    )

# Un astro cruza el cielo en media vuelta (media hoja de CICLO) y queda oculto la otra media.
# El sol arranca en t=0 y la luna 24 s después con el mismo recorrido, así que mientras uno
# está arriba el otro está bajo el horizonte. El cielo se oscurece con la misma fase.
HORIZONTE = 290  # y donde el astro toca el horizonte, detrás de las montañas
RX, RY = 500, 250
PASOS = 48
astro_kf = []
for i in range(PASOS + 1):
    t = 2 * math.pi * i / PASOS - math.pi / 2
    x, y = 600 + RX * math.sin(t), HORIZONTE - RY * math.cos(t)
    visible = 1 if y < HORIZONTE else 0
    astro_kf.append(f"{f(100 * i / PASOS)}% {{transform:translate({f(x)}px,{f(y)}px);opacity:{visible}}}")
ASTRO_KF = " ".join(astro_kf)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Dark4rest: un bosque oscuro con montañas, un valle y luciérnagas, en un ciclo de día y noche">
<style>
  @keyframes noche {{ 0% {{opacity:.5}} 6%,44% {{opacity:0}} 50% {{opacity:.5}} 56%,94% {{opacity:1}} 100% {{opacity:.5}} }}
  @keyframes ocaso {{ 0% {{opacity:.6}} 8%,40% {{opacity:0}} 50% {{opacity:.9}} 60%,92% {{opacity:0}} 100% {{opacity:.6}} }}
  @keyframes sombra {{ 0% {{opacity:.3}} 6%,44% {{opacity:.04}} 56%,94% {{opacity:.6}} 100% {{opacity:.3}} }}
  @keyframes astro {{ {ASTRO_KF} }}
  @keyframes flota {{ 0%,100% {{transform:translate(0,0)}} 50% {{transform:translate(6px,-9px)}} }}
  @keyframes niebla {{ 0%,100% {{transform:translateX(-40px)}} 50% {{transform:translateX(40px)}} }}
  @keyframes parpadeo {{ 0%,46%,50%,100% {{transform:scaleY(1)}} 48% {{transform:scaleY(.1)}} }}
  .noche {{ animation: noche {CICLO}s linear infinite }}
  .ocaso {{ animation: ocaso {CICLO}s linear infinite }}
  .sombra {{ animation: sombra {CICLO}s linear infinite }}
  .sol {{ animation: astro {CICLO}s linear infinite }}
  .luna {{ animation: astro {CICLO}s linear infinite; animation-delay: -{CICLO // 2}s }}
  .lu {{ transform-box: fill-box; animation-name: flota, noche; animation-iteration-count: infinite; animation-timing-function: ease-in-out, linear; filter: url(#brillo) }}
  .niebla {{ animation: niebla 30s ease-in-out infinite }}
  .ojos {{ transform-box: fill-box; transform-origin: center; animation: parpadeo 7s infinite }}
  @media (prefers-reduced-motion: reduce) {{
    * {{ animation: none !important }}
    .sol {{ transform: translate(600px,40px) }}
    .luna, .noche, .ocaso, .sombra, .lu {{ display: none }}
  }}
</style>
<defs>
  <linearGradient id="dia" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#5a9fc4"/><stop offset="1" stop-color="#dbe8d6"/>
  </linearGradient>
  <linearGradient id="cielo-noche" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#05070e"/><stop offset="1" stop-color="#18222c"/>
  </linearGradient>
  <linearGradient id="horizonte" x1="0" y1="0" x2="0" y2="1">
    <stop offset=".2" stop-color="{KAL}" stop-opacity="0"/><stop offset=".85" stop-color="#d9774b" stop-opacity=".95"/>
  </linearGradient>
  <radialGradient id="halo"><stop offset="0" stop-color="#fff" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
  <filter id="brillo" x="-3" y="-3" width="7" height="7"><feGaussianBlur stdDeviation="2.4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>

<rect width="{W}" height="{H}" fill="url(#dia)"/>
<rect class="noche" width="{W}" height="{H}" fill="url(#cielo-noche)"/>
<rect class="ocaso" width="{W}" height="260" fill="url(#horizonte)"/>
<g class="noche" fill="#e9ecf5">{"".join(estrellas)}</g>

<g class="sol" style="opacity:0">
  <circle r="60" fill="url(#halo)"/>
  <circle r="22" fill="#f4e2b0"/>
</g>
<g class="luna" style="opacity:0">
  <circle r="50" fill="url(#halo)"/>
  <circle r="16" fill="#e4e6f2"/>
  <circle cx="7" cy="-5" r="14" fill="#c7cbe0" fill-opacity=".35"/>
</g>

<path d="{cordillera(232, 88, 2.2, 1)}" fill="#3a5560"/>
<path d="{cordillera(252, 66, 3.1, 2)}" fill="#2b4246"/>
<path class="niebla" d="M-60,250 Q300,228 600,248 T1260,244 L1260,262 Q900,272 600,262 T-60,266 Z" fill="#cfd8d4" fill-opacity=".18"/>
{"".join(f'<path d="{hilera(s, a, d, i + 10)}" fill="{c}"/>' for i, (s, a, d, c) in enumerate(capas_bosque))}
<rect y="372" width="{W}" height="28" fill="#080f0d"/>

<rect class="sombra" width="{W}" height="{H}" fill="#03050a"/>

<g class="noche">
  <g class="ojos"><circle cx="884" cy="318" r="2.6" fill="{OWL}" filter="url(#brillo)"/><circle cx="895" cy="318" r="2.6" fill="{OWL}" filter="url(#brillo)"/></g>
</g>
{"".join(luciernagas)}

<text x="600" y="372" text-anchor="middle" fill="#eef1ec" font-family="ui-monospace,'JetBrains Mono','IBM Plex Mono',Menlo,Consolas,monospace" font-size="44" font-weight="700" letter-spacing="14">DARK4REST</text>
<text x="600" y="393" text-anchor="middle" fill="#eef1ec" fill-opacity=".72" font-family="ui-monospace,'IBM Plex Mono',Menlo,Consolas,monospace" font-size="13" letter-spacing="3">herramientas offline</text>
</svg>
"""

salida = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "assets" / "banner.svg"
salida.parent.mkdir(parents=True, exist_ok=True)
salida.write_text(svg, encoding="utf-8")
print(f"{salida} ({len(svg) // 1024} KB)")
