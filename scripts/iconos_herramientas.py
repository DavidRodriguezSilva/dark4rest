#!/usr/bin/env python3
"""Genera las fichas de herramientas del perfil en perfil/assets/tools/.

Las fichas que skillicons.dev no tiene se arman aquí con el mismo formato (48x48,
esquina redondeada, fondo oscuro). Los logos vienen de Simple Icons (CC0) y se bajan
al correr el script; las herramientas sin logo libre llevan un monograma.

    python3 scripts/iconos_herramientas.py
"""

import re
import urllib.request
from pathlib import Path

SALIDA = Path(__file__).resolve().parent.parent / "perfil" / "assets" / "tools"
FONDO, BORDE = "#0b1210", "#c9c3f5"

# archivo: (slug en Simple Icons, color del logo)
LOGOS = {
    "cisco": ("cisco", "049FD9"),
    "siemens": ("siemens", "009999"),
    "wolfram": ("wolframmathematica", "DD1100"),
    "easyeda": ("easyeda", "1765F6"),
    "owasp": ("owasp", "eef1ec"),
}
# archivo: (texto, color)
MONOGRAMAS = {
    "rds": ("RDS", "#527FFF"),
    "mplab": ("MP", "#e8b14b"),
    "proteus": ("Px", "#6ddda1"),
}


def ficha(contenido, titulo):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48" role="img" aria-label="{titulo}">'
        f'<title>{titulo}</title>'
        f'<rect width="48" height="48" rx="10" fill="{FONDO}"/>'
        f'<rect x=".5" y=".5" width="47" height="47" rx="9.5" fill="none" stroke="{BORDE}" stroke-opacity=".25"/>'
        f"{contenido}</svg>\n"
    )


def trazo(slug, color):
    pedido = urllib.request.Request(f"https://cdn.simpleicons.org/{slug}/{color}", headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(pedido, timeout=20) as r:
        svg = r.read().decode("utf-8")
    return re.search(r'<path d="([^"]+)"', svg).group(1)


SALIDA.mkdir(parents=True, exist_ok=True)

ANCHOS = {"cisco", "siemens"}  # logotipos largos: se escalan por el ancho, no por la altura

for nombre, (slug, color) in LOGOS.items():
    d = trazo(slug, color)
    t = "translate(6 6) scale(1.5)" if nombre in ANCHOS else "translate(9 9) scale(1.25)"
    (SALIDA / f"{nombre}.svg").write_text(ficha(f'<path transform="{t}" fill="#{color}" d="{d}"/>', nombre), encoding="utf-8")

for nombre, (texto, color) in MONOGRAMAS.items():
    (SALIDA / f"{nombre}.svg").write_text(
        ficha(
            f'<text x="24" y="30" text-anchor="middle" fill="{color}" font-family="ui-monospace,Menlo,Consolas,monospace" '
            f'font-size="{16 if len(texto) < 3 else 14}" font-weight="700">{texto}</text>',
            nombre,
        ),
        encoding="utf-8",
    )

print(f"{len(LOGOS) + len(MONOGRAMAS)} fichas en {SALIDA}")
