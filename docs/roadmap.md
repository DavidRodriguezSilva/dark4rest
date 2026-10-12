# Roadmap

Lo que viene en la familia. Cada pieza nueva nace aquí como una ficha corta y,
cuando se decide construirla, pasa a su propio repo en `apps/` con su
OpenSpec (con dark-echo como referencia de convenciones).

## dark-raven *(nombre tentativo)*: texto a voz

**Qué te da:** escribes o pegas un texto y lo escuchas leído. Lo contrario de
dark-owl: el búho escucha y escribe; el cuervo, que imita voces, lee en voz
alta.

- **Motor candidato:** [Piper](https://github.com/rhasspy/piper) (voces ONNX,
  buenas voces en español, corre en CPU). Alternativa por evaluar: Kokoro.
- **Offline:** el instalador trae una voz por defecto y las demás se
  agregan como archivos, sin descargarlas en la ejecución.
- **Alcance mínimo:** texto → audio, pausar y reanudar, velocidad, exportar a
  WAV. Leer archivos (txt, md, pdf) queda para una segunda versión.
- **Abierto:** ¿escritorio (Electron, como dark-owl) o PWA (WASM, como
  dark-echo)? Piper tiene build WASM, así que la PWA es viable.

## dark-mycelium *(nombre tentativo)*: traductor

**Qué te da:** traduces texto entre idiomas sin conexión. El micelio es la red
que comunica árboles distintos bajo el bosque.

- **Motor candidato:** [Bergamot](https://browser.mt/) (el de la traducción
  offline de Firefox, corre en WASM) o Argos Translate (Python + CTranslate2).
- **Offline:** cada par de idiomas es un paquete que se instala como archivo.
- **Alcance mínimo:** español ↔ inglés, texto pegado.
- **Abierto:** Bergamot permite que sea PWA; Argos obligaría a escritorio.

## Ideas sueltas

Sin compromiso, para no perderlas:

- Composición: dark-owl → dark-mycelium → dark-raven = dictar en un idioma y
  oírlo en otro, sin que ninguna pieza dependa de las otras.
