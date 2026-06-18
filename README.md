# Financial Analysis Service

API que iremos construyendo a lo largo de las sesiones de la asignatura. Al final de las tres clases tendrá análisis de series temporales, modelos de machine learning y un RAG sobre documentación financiera.

Leyendo está guía deberíamos ser capaces de tener la versión 0.1.0 de la API, de manera que podamos ir añadiendo features sesión a sesión.

---

## Qué vamos a instalar

| Herramienta | Para qué sirve |
|---|---|
| **Git** | Control de versiones — imprescindible en cualquier proyecto de software |
| **uv** | Gestiona Python y las dependencias del proyecto sin necesitar permisos de administrador |
| **Python 3.12** | Lo instala uv automáticamente, solo para este proyecto |

---

## 1. Instalar Git

### Windows (sin permisos de administrador)

1. Entra en https://git-scm.com/download/win
2. Descarga **"64-bit Git for Windows Portable"**
3. Ejecuta el `.exe` descargado — no pide permisos de administrador
4. Al terminar, abre el **Git Bash** que viene incluido y úsalo para todos los comandos de esta guía

Comprueba que funciona:
```bash
git --version
```

### Linux

La mayoría de máquinas Linux ya tienen Git instalado. Compruébalo primero:
```bash
git --version
```

Si aparece una versión, ya está listo. Si no, prueba las opciones siguientes en orden.

**Opción A — Sistema de módulos** (habitual en máquinas universitarias y servidores compartidos)
```bash
module load git
git --version
```
Si funciona, añádelo a tu `.bashrc` para no tener que ejecutarlo cada vez:
```bash
echo "module load git" >> ~/.bashrc
```

---

## 2. Instalar uv

`uv` se instala en tu carpeta de usuario — no necesita permisos de administrador.

### Windows

Abre **PowerShell** (no hace falta que sea como administrador) y ejecuta:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Cierra PowerShell y ábrelo de nuevo para que el PATH se actualice. Luego comprueba:
```powershell
uv --version
```

> **¿Te dice que el comando no se encuentra?** Ejecuta esto para añadir uv al PATH de forma permanente:
> ```powershell
> [System.Environment]::SetEnvironmentVariable("Path", $env:Path + ";$env:USERPROFILE\.local\bin", "User")
> ```
> Cierra y vuelve a abrir PowerShell.

### Linux / macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Cierra y vuelve a abrir la terminal, o ejecuta:
```bash
source ~/.bashrc    # si usas bash
source ~/.zshrc     # si usas zsh
```

Comprueba que funciona:
```bash
uv --version
```

---

## 3. Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd financial-analysis-svc
```

> Si no tienes la URL, el profesor la compartirá en clase.

---

## 4. Instalar Python 3.12 y las dependencias

Dentro de la carpeta del proyecto, ejecuta:

```bash
uv sync
```

Eso es todo. `uv` leerá el archivo `.python-version` del proyecto, instalará Python 3.12 si no lo tienes, creará un entorno virtual aislado e instalará todas las dependencias. No toca tu Python del sistema.

Comprueba qué versión de Python está usando el proyecto:
```bash
uv run python --version
```

Deberías ver `Python 3.12.x`.

---

## 5. Arrancar el servicio

```bash
uv run uvicorn app.main:app --reload
```

Si todo va bien, verás algo así:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

---

## 6. Comprobar que funciona

Abre un navegador y entra en:

```
http://localhost:8000/health
```

Deberías ver:

```json
{"status": "ok"}
```

También tienes la documentación interactiva automática en:

```
http://localhost:8000/docs
```

---

## Estructura del proyecto

```
financial-analysis-svc/
├── app/
│   ├── __init__.py
│   └── main.py          # punto de entrada de la API
├── .python-version      # fija la versión de Python para este proyecto
├── pyproject.toml       # dependencias del proyecto
└── README.md
```

---

## Solución de problemas frecuentes

**"uv: command not found" después de instalarlo**
La terminal no ha cargado el nuevo PATH. Ciérrala y ábrela de nuevo.

**El puerto 8000 ya está en uso**
```bash
uv run uvicorn app.main:app --reload --port 8001
```
Y accede a `http://localhost:8001/health`.

**En Windows, PowerShell dice "la ejecución de scripts está deshabilitada"**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Luego vuelve a ejecutar el comando de instalación de uv.

---

## Para parar el servidor

Pulsa `Ctrl + C` en la terminal donde está corriendo.
