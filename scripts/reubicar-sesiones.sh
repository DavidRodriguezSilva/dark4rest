#!/usr/bin/env bash
# Reengancha las sesiones y la memoria de Claude Code después de mover un repo.
#
# Claude Code guarda cada proyecto en ~/.claude/projects/<ruta-codificada>/ y
# cada sesión anota su "cwd". Si el repo cambia de carpeta, las sesiones quedan
# huérfanas: `claude --resume` no las encuentra. Este script renombra la carpeta
# y reescribe el cwd de cada sesión.
#
# Uso:
#   ./scripts/reubicar-sesiones.sh RUTA_VIEJA RUTA_NUEVA            # simulación
#   ./scripts/reubicar-sesiones.sh RUTA_VIEJA RUTA_NUEVA --aplicar  # ejecuta
#
# Ejemplo:
#   ./scripts/reubicar-sesiones.sh /home/drack/projects/kalndr /home/drack/projects/dark4rest/apps/kalndr
#
# Antes de aplicar: cerrar cualquier `claude` abierto en ese repo.
# Rollback: el respaldo queda en ~/.claude/respaldos/; basta con borrar la
# carpeta nueva y descomprimirlo en ~/.claude/projects/.
set -euo pipefail

VIEJA=${1:?ruta vieja}; NUEVA=${2:?ruta nueva}; MODO=${3:-}
BASE="$HOME/.claude/projects"
codificar() { printf '%s' "$1" | sed 's/[^A-Za-z0-9]/-/g'; }
ORIG="$BASE/$(codificar "$VIEJA")"
DEST="$BASE/$(codificar "$NUEVA")"

echo "origen : $ORIG"
echo "destino: $DEST"

[[ -d "$ORIG" ]] || { echo "No hay sesiones en el origen; nada que hacer."; exit 0; }
[[ -e "$DEST" ]] && { echo "ERROR: el destino ya existe. Revisar a mano antes de fusionar."; exit 1; }
[[ -d "$NUEVA" ]] || { echo "ERROR: $NUEVA no existe. ¿Ya se movió el repo?"; exit 1; }

# Un claude vivo en la ruta vieja seguiría escribiendo en el origen.
for p in /proc/[0-9]*; do
  if [[ "$(readlink "$p/cwd" 2>/dev/null)" == "$VIEJA"* ]]; then
    echo "ERROR: hay procesos trabajando en $VIEJA (pid ${p#/proc/}). Ciérralos primero."; exit 1
  fi
done

SESIONES=$(find "$ORIG" -maxdepth 1 -name '*.jsonl' | wc -l)
CWDS=$(grep -ho "\"cwd\":\"$VIEJA[^\"]*\"" "$ORIG"/*.jsonl 2>/dev/null | wc -l || true)
echo "sesiones: $SESIONES · líneas con cwd a reescribir: $CWDS"
echo "memoria : $(ls "$ORIG/memory" 2>/dev/null | wc -l) archivo(s), se mueven tal cual"

if [[ "$MODO" != "--aplicar" ]]; then
  echo; echo "Simulación. Repite con --aplicar para ejecutar."; exit 0
fi

mkdir -p "$HOME/.claude/respaldos"
RESPALDO="$HOME/.claude/respaldos/$(basename "$ORIG")-$(date +%Y%m%d-%H%M%S).tgz"
tar czf "$RESPALDO" -C "$BASE" "./$(basename "$ORIG")"  # ./ porque el nombre empieza con "-"
echo "respaldo: $RESPALDO"

mv "$ORIG" "$DEST"
find "$DEST" -maxdepth 1 -name '*.jsonl' -exec \
  sed -i "s#\"cwd\":\"$VIEJA#\"cwd\":\"$NUEVA#g" {} +

QUEDAN=$(grep -ho "\"cwd\":\"$VIEJA[\"/]" "$DEST"/*.jsonl 2>/dev/null | wc -l || true)
echo "listo. cwd viejos restantes: $QUEDAN (debe ser 0)"
echo "Comprobar: cd $NUEVA && claude --resume"
