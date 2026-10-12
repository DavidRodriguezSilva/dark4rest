<p align="center"><img src="assets/banner.svg" alt="Dark4rest: un bosque oscuro con montañas y luciérnagas, en un ciclo de día y noche" width="100%"></p>

# Dark4rest

Una biblioteca de **funcionalidades pequeñas, offline y bien terminadas**.
Cada una es como un tornillo o una tuerca: funciona sola, hace una cosa y la
hace bien, y lo que cambia es dónde se usa.

## Las piezas

| | Pieza | Qué te da | Estado |
|---|---|---|---|
| <img src="assets/apps/dark-echo.svg" width="28"> | [**dark-echo**](https://github.com/DavidRodriguezSilva/dark-echo) | Lluvia, viento, río y ruido de color sintetizados en vivo, sin bucles que se repitan | [Publicada](https://davidrodriguezsilva.github.io/dark-echo/) |
| <img src="assets/apps/dark-owl.png" width="28"> | [**dark-owl**](https://github.com/DavidRodriguezSilva/dark-owl) | Dicta y obtén el texto, sin que el audio salga de tu máquina | En desarrollo |
| <img src="assets/apps/kalndr.svg" width="28"> | [**kalndr**](https://github.com/DavidRodriguezSilva/kalndr) | Los festivos de Colombia, los puentes y las mejores fechas de vacaciones | [Publicada](https://davidrodriguezsilva.github.io/kalndr/) |
| | **dark-raven** *(nombre tentativo)* | Escribe un texto y escúchalo leído en voz alta | Planeada |
| | **dark-mycelium** *(nombre tentativo)* | Traduce entre idiomas sin conexión | Planeada |

El detalle de lo que viene está en [`docs/roadmap.md`](docs/roadmap.md).

## Principios

1. **Offline primero.** Ninguna pieza llama a internet para funcionar. Si
   necesita modelos o datos, los trae el instalador.
2. **Una responsabilidad.** Si una funcionalidad no cabe en una frase, son dos
   piezas.
3. **Sola y combinable.** Cada pieza se instala, se usa y se prueba sin las
   demás.
4. **Ligera.** Optimizada para el equipo de quien la usa, no para el del autor.
5. **Sin cuentas ni telemetría.** Lo tuyo se queda contigo.

## Este repositorio

Es el repo de orquestación: la vitrina, el roadmap y los acuerdos comunes. El
código de cada pieza vive en su propio repositorio, clonado dentro de este
árbol pero **independiente** (no son submódulos):

```
dark4rest/
├── apps/      piezas de la familia, un repo cada una (ignorado aquí)
├── ref/       repos de terceros que sirven de referencia o de motor (ignorado)
├── assets/    banner, logo e íconos de las piezas
├── docs/      roadmap, identidad visual y logros de GitHub
├── perfil/    el README del perfil de GitHub, repo aparte (ignorado)
└── scripts/   clonar la familia, generar el banner
```

Para armar el árbol completo en una máquina nueva:

```sh
git clone https://github.com/DavidRodriguezSilva/dark4rest.git
cd dark4rest && ./scripts/clonar.sh
```

## Licencia

MIT, igual que cada pieza.
