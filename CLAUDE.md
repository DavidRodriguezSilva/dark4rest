# Dark4rest: repo de orquestación

## Rol

Aquí el trabajo es **transversal**: vitrina de GitHub, roadmap, identidad
visual, logros y fichas de piezas nuevas. El rol es el del equipo senior del
lineamiento global (desarrollo, arquitectura, UI/UX, liderazgo técnico).

El código de cada pieza **no se toca desde aquí**: cada app en `apps/` es un
repositorio independiente, con su propio `CLAUDE.md`/`AGENTS.md`, su OpenSpec y
sus sesiones. Un cambio en una app se hace en la sesión de esa app.

## Estructura

- `apps/`: piezas de la familia (dark-echo, dark-owl, kalndr). Ignorado por git.
- `ref/`: repos de terceros. `whisper.cpp` es el motor de dark-owl, que lo
  busca por defecto en `../../ref/whisper.cpp` (`scripts/setup-whisper.js`).
- `perfil/`: repo `DavidRodriguezSilva/DavidRodriguezSilva` (README del perfil). Ignorado.
- `assets/banner.svg`: **generado** por `scripts/banner.py`. No editarlo a mano.

## Reglas

- `~/projects/mi-org` está **fuera de alcance**: no se abre ni se cita.
- Principios de la familia: offline primero, una responsabilidad por pieza,
  cada pieza funciona sola (ver `README.md`).
- Etiquetas que prometen contenido: un enlace dice qué vas a encontrar.
- Commits: sólo cuando Drack lo pide, granulares por pieza lógica, sin coautor.
- Al mover un repo, reenganchar sus sesiones con `scripts/reubicar-sesiones.sh`.

## Pendientes de la reorganización

- [x] Mover `dark-owl` a `apps/` y apuntar `setup-whisper.js` a `../../ref/whisper.cpp`
      (cambio sin commitear en dark-owl).
- [ ] Recompilar `ref/whisper.cpp/build` si CMake se queja de la ruta (la
      caché guarda rutas absolutas).
- [ ] Correr `reubicar-sesiones.sh --aplicar` para kalndr, dark-echo y dark-owl.
- [ ] Los shims de `node_modules/.bin` de dark-echo y kalndr guardan la ruta
      vieja en `NODE_PATH`. Funcionan igual; si algo falla, borrar
      `node_modules` y correr `pnpm install --offline`.
