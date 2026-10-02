#!/usr/bin/env bash
# Crea un entorno virtual de Python e instala las dependencias de requirements.txt.
# El requirements.txt esta en la raiz del repo, fuera de esta carpeta.
set -euo pipefail

# Raiz del repo (carpeta padre de la que contiene este script)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

REQUIREMENTS="${REPO_ROOT}/requirements.txt"
ENV_DIR="${REPO_ROOT}/env"

if [ ! -f "${REQUIREMENTS}" ]; then
    echo "No se encontro ${REQUIREMENTS}" >&2
    exit 1
fi

# Crear el entorno virtual si no existe
if [ ! -d "${ENV_DIR}" ]; then
    echo "Creando entorno virtual en ${ENV_DIR}..."
    python3 -m venv "${ENV_DIR}"
fi

# Activar e instalar dependencias
# shellcheck disable=SC1091
source "${ENV_DIR}/bin/activate"
python -m pip install --upgrade pip
python -m pip install -r "${REQUIREMENTS}"

echo ""
echo "Entorno listo. Para activarlo ejecuta:"
echo "    source ${ENV_DIR}/bin/activate"
