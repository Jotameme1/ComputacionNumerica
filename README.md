# ComputacionNumerica
Aprendizaje de contenidos de calculo discreto y herramienta de control de versiones github

## Entorno virtual de Python (venv)

Como alternativa a Docker, puedes trabajar con un entorno virtual local. El script [Create_python/create_env.sh](Create_python/create_env.sh) crea el entorno en la carpeta `env/` (raíz del repo) e instala las dependencias de [requirements.txt](requirements.txt) (`numpy` y `matplotlib`).

### 1. Crear el entorno e instalar dependencias

Desde la raíz del repo:

```bash
bash Create_python/create_env.sh
```

El script:

- Sube a la raíz del repo, así funciona desde donde lo ejecutes.
- Crea el entorno virtual en `env/` solo si aún no existe.
- Actualiza `pip` e instala lo definido en `requirements.txt`.

> La carpeta `env/` está ignorada en `.gitignore`, por lo que no se sube al repo.

### 2. Activar el entorno

```bash
source env/bin/activate
```

Una vez activado, el prompt muestra `(env)` y puedes ejecutar tus scripts:

```bash
python src/Eval1/mi_script.py
```

Para salir del entorno:

```bash
deactivate
```

## Montar el entorno con Docker

El [Docker/Dockerfile](Docker/Dockerfile) parte de la imagen `python:3.12-slim`, instala `curl` y las dependencias de Python definidas en [requirements.txt](requirements.txt) (`numpy` y `matplotlib`). La carpeta `src/` se monta como volumen al ejecutar, de modo que los cambios que hagas en tu máquina se ven al instante dentro del contenedor sin reconstruir la imagen.

### 1. Construir la imagen

Desde la raíz del repo:

```bash
docker build -f Docker/Dockerfile -t computacion-numerica .
```

Solo hace falta volver a construirla si cambias `requirements.txt`.

### 2. Ejecutar el contenedor

```bash
docker run -it --rm -v "$(pwd)/src:/app/src" computacion-numerica
```

- `-it` abre una terminal interactiva dentro del contenedor.
- `--rm` elimina el contenedor al salir.
- `-v "$(pwd)/src:/app/src"` monta tu carpeta `src/` como volumen.

Al entrar quedas en `/app/src`. Para correr un script:

```bash
python Eval1/mi_script.py
```

> `matplotlib` usa el backend `Agg` (sin ventana), así que guarda los gráficos en archivo con `savefig()` en lugar de `show()`.
