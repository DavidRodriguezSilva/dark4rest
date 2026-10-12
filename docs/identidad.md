# Identidad visual

## La idea

Un **bosque oscuro**: oscuro de denso, no de noche. Montañas, valle, niebla y
árboles muy juntos en una sola escena, con un ciclo de día y noche. Cada pieza
de la familia es una **luciérnaga** con su propio color: de día casi no se
ven; de noche son lo único que brilla.

El banner (`assets/banner.svg`) lo genera `scripts/banner.py`. No se edita a
mano: se cambia el script y se regenera. El ciclo dura 48 s, respeta
`prefers-reduced-motion` y no carga nada externo.

## Paleta

| Rol | Color | Uso |
|---|---|---|
| Fondo de bosque | `#0b1210` | Fondo de íconos, primer plano del banner |
| Texto claro | `#eef1ec` | Trazos y texto sobre fondo oscuro |
| dark-echo | `#6ddda1` | Acento de la app |
| dark-owl | `#c9c3f5` | Acento de la app (propuesto: luz de luna) |
| kalndr | `#e8b14b` | Acento de la app |
| Pieza nueva | por elegir | Un tono que no choque con los tres de arriba |

## Regla de íconos

Ícono de trazo (estilo Lucide), **grosor 2 en una grilla de 24**, extremos
redondeados, un solo color de acento sobre el fondo de bosque, esquina de
5.5 px. El logo de la familia (`assets/logo.svg`) sigue la regla: tres pinos,
uno por app, y el ojo del búho en el del centro.

## Logos por ajustar

Se tachan cuando el repo de la app tenga el cambio.

- [x] **Dark4rest**: logo de familia (`assets/logo.svg`)
- [x] **Dark4rest**: banner con ciclo de día y noche (`assets/banner.svg`)
- [ ] **dark-echo**: hoy son dos barras rellenas, sin trazo y sin fondo. Pasarlo a trazo sobre el fondo de bosque (p. ej. ondas de sonido saliendo de un árbol)
- [ ] **dark-owl**: el búho en trazo ya sigue la regla; falta usar el acento `#c9c3f5` en lugar del blanco y el fondo `#0b1210` en lugar del azul marino
- [ ] **kalndr**: ya es trazo y tiene su acento; falta el fondo de bosque en los íconos PWA (192/512)
- [ ] **Vista previa social** (1280×640) de cada repo con la misma escena del banner y el ícono de la app
- [ ] **dark-raven / dark-mycelium**: ícono desde el principio con la regla
