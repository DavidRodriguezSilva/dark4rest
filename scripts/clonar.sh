#!/usr/bin/env bash
# Arma el árbol de Dark4rest: clona cada pieza en apps/ y cada referencia en ref/.
# Los que ya existen se dejan como están. Uso: ./scripts/clonar.sh
set -euo pipefail
cd "$(dirname "$0")/.."

USUARIO=https://github.com/DavidRodriguezSilva
APPS=(dark-echo dark-owl kalndr)
REFS=(
  "https://github.com/ggml-org/whisper.cpp.git"
  "https://github.com/b84330808/whisperpress.git"
)

clonar() { # url destino
  if [[ -d "$2/.git" ]]; then echo "= $2 ya existe"; else git clone "$1" "$2"; fi
}

mkdir -p apps ref
for a in "${APPS[@]}"; do clonar "$USUARIO/$a.git" "apps/$a"; done
for r in "${REFS[@]}"; do n=$(basename "$r" .git); clonar "$r" "ref/$n"; done
clonar "$USUARIO/DavidRodriguezSilva.git" perfil || echo "! perfil: el repo aún no existe en GitHub"
