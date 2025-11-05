# 📺 Análisis de Series y Películas de Netflix

## 📖 Descripción del Proyecto

Este proyecto realiza un **análisis exploratorio de datos (EDA)** sobre el catálogo completo de Netflix, utilizando Python y Jupyter Notebook. El análisis incluye limpieza de datos, visualizaciones y hallazgos sobre la distribución de contenido entre películas y series.

### 🎯 Objetivos

- Analizar la distribución de contenido en Netflix (Movies vs TV Shows)
- Limpiar y preparar datos para análisis
- Identificar patrones y tendencias en el catálogo
- Crear visualizaciones informativas
- Documentar hallazgos principales

## 📊 Dataset

### Información General

| Aspecto | Descripción |
|---------|-------------|
| **Nombre del Dataset** | netflix_titles.csv |
| **Total de Registros** | 8,807 |
| **Total de Variables** | 12 columnas |
| **Fuente de Datos** | Kaggle |
| **Propósito** | Análisis Descriptivo |

### 📋 Estructura de Variables

| Variable | Descripción | Tipo |
|----------|-------------|------|
| `show_id` | Identificador único de película/serie | object |
| `type` | Tipo de contenido (Movie/TV Show) | object |
| `title` | Título de la película/serie | object |
| `director` | Director(es) a cargo | object |
| `cast` | Elenco de actores | object |
| `country` | País(es) de producción | object |
| `date_added` | Fecha en que se agregó a Netflix | object |
| `release_year` | Año de lanzamiento | int64 |
| `rating` | Clasificación por edad | object |
| `duration` | Duración (minutos/temporadas) | object |
| `listed_in` | Género(s) o categoría(s) | object |
| `description` | Sinopsis del contenido | object |

## 🏗️ Estructura del Proyecto

```
proyecto data analytics Netflix/
│
├── Dataset/
│   └── netflix_titles.csv          # Dataset principal
│
├── NoteBook/
│   └── analisis.ipynb               # Jupyter Notebook con el análisis
│
├── .venv/                           # Entorno virtual (generado por uv)
│
└── README.md                        # Este archivo
```

## 🔧 Requisitos Previos

### Sistema Operativo
- ✅ Windows 10/11
- ✅ Linux
- ✅ macOS

### Software Necesario
- **Python 3.8+** (uv lo gestionará automáticamente)
- **uv** - Gestor de paquetes ultrarrápido para Python
- **Git** - Para clonar el repositorio

## ⚡ Instalación con uv

### Paso 1: Instalar uv

#### En Windows (PowerShell)
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### En Linux/macOS
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Paso 2: Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd "proyecto data analytics Netflix"
```

### Paso 3: Crear Entorno Virtual

```bash
uv venv
```

Esto creará un entorno virtual en la carpeta `.venv`

### Paso 4: Activar el Entorno Virtual

#### En Windows (PowerShell)
```powershell
.venv\Scripts\Activate.ps1
```

#### En Windows (CMD)
```cmd
.venv\Scripts\activate.bat
```

#### En Linux/macOS
```bash
source .venv/bin/activate
```

### Paso 5: Instalar Dependencias

```bash
uv pip install pandas matplotlib jupyter notebook
```

### Paso 6: Iniciar Jupyter Notebook

```bash
jupyter notebook
```

Esto abrirá Jupyter en tu navegador predeterminado.

### Paso 7: Abrir el Notebook

1. En la interfaz de Jupyter, navega a `NoteBook/`
2. Haz clic en `analisis.ipynb`
3. Ejecuta las celdas secuencialmente (Shift + Enter)

## 📦 Dependencias del Proyecto

| Librería | Versión | Propósito |
|----------|---------|----------|
| `pandas` | Latest | Manipulación y análisis de datos |
| `matplotlib` | Latest | Visualización de datos |
| `jupyter` | Latest | Entorno de notebook interactivo |

## 🔍 Análisis Incluidos

### 1. 📥 Carga y Exploración de Datos
- Importación del dataset
- Visualización de primeras filas
- Información del DataFrame (dimensiones, tipos de datos)

### 2. 🧹 Limpieza de Datos

#### Formateo de Datos
- Conversión de fechas a formato estándar
- Estandarización de texto (capitalización, Title Case)
- Normalización de IDs

#### Manejo de Valores Nulos
- **Estrategia implementada:**
  - **> 5% de nulos**: Imputación con "Desconocido"
  - **< 5% de nulos**: Eliminación de registros

| Columna | % Nulos | Tratamiento |
|---------|---------|-------------|
| director | 29.91% | Imputado |
| cast | 9.37% | Imputado |
| country | 9.44% | Imputado |
| date_added | 0.11% | Eliminado |
| rating | 0.05% | Eliminado |
| duration | 0.03% | Eliminado |

#### Manejo de Duplicados
- Verificación por `show_id`
- Eliminación de registros duplicados

### 3. 📊 Visualizaciones

- **Gráfico de torta**: Distribución Movies vs TV Shows
- **Análisis comparativo** de tipos de contenido

## 🎯 Resultados y Hallazgos

### 📈 Distribución de Contenido

```
🎬 Películas (Movies): 6,126 títulos (69.7%)
📺 Series (TV Shows):  2,664 títulos (30.3%)
```

**Conclusión Principal:** Netflix ha apostado significativamente más por las películas que por las series en su catálogo.

### ✅ Calidad de los Datos

- ✔️ 0% valores nulos después del procesamiento
- ✔️ 0 registros duplicados
- ✔️ Datos formateados y estandarizados
- ✔️ Ready para análisis avanzados

## 🛠️ Comandos Útiles de uv

### Gestión de Paquetes

```bash
# Instalar un paquete
uv pip install nombre_paquete

# Instalar múltiples paquetes
uv pip install pandas matplotlib jupyter

# Actualizar un paquete
uv pip install --upgrade nombre_paquete

# Listar paquetes instalados
uv pip list

# Desinstalar un paquete
uv pip uninstall nombre_paquete
```

### Gestión de Entorno

```bash
# Crear entorno virtual
uv venv

# Crear con versión específica de Python
uv venv --python 3.11

# Generar requirements.txt
uv pip freeze > requirements.txt

# Instalar desde requirements.txt
uv pip install -r requirements.txt
```

### Desactivar Entorno

```bash
deactivate
```

## 🚀 Próximos Análisis Sugeridos

- [ ] **Análisis Temporal**: Tendencias de contenido agregado por año
- [ ] **Top Países**: Países con mayor producción de contenido
- [ ] **Análisis de Géneros**: Categorías más populares
- [ ] **Ratings**: Clasificaciones más comunes por tipo
- [ ] **Duración Promedio**: Análisis estadístico de duraciones
- [ ] **Directores Prolíficos**: Top directores con más títulos
- [ ] **Dashboard Interactivo**: Visualización con Plotly/Streamlit

## 💡 ¿Por qué usar uv?

### Ventajas sobre pip

| Característica | uv | pip tradicional |
|----------------|----|-----------------|
| **Velocidad** | ⚡ 10-100x más rápido | 🐌 Estándar |
| **Caché inteligente** | ✅ Sí | ❌ Limitado |
| **Instalación paralela** | ✅ Sí | ❌ No |
| **Resolución de dependencias** | ⚡ Ultrarrápida | 🐌 Lenta |
| **Compatibilidad** | ✅ 100% con pip | ✅ N/A |

### Benchmarks

```
Instalación de pandas + matplotlib + jupyter:

uv:   ~3 segundos  ⚡
pip:  ~45 segundos 🐌
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto:

1. **Fork** el repositorio
2. **Crea una rama** para tu feature:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. **Commit** tus cambios:
   ```bash
   git commit -m "Agregar: descripción de cambios"
   ```
4. **Push** a tu rama:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. **Abre un Pull Request**

### Lineamientos de Contribución

- Mantén el código limpio y documentado
- Agrega comentarios explicativos en español
- Sigue las convenciones de nomenclatura existentes
- Actualiza el README si es necesario

## 📝 Notas Técnicas

### Tecnologías Utilizadas

- **Lenguaje**: Python 3.8+
- **Gestor de Paquetes**: uv
- **IDE/Editor**: Jupyter Notebook
- **Librerías**: pandas, matplotlib

### Requisitos de Sistema

- **RAM**: Mínimo 4 GB (recomendado 8 GB)
- **Espacio en disco**: ~500 MB para entorno y dependencias
- **Conexión a Internet**: Necesaria para instalación inicial

## 🐛 Solución de Problemas

### Problema: uv no se reconoce como comando

**Solución Windows:**
```powershell
# Reinicia PowerShell después de instalar uv
# O agrega manualmente al PATH:
$env:Path += ";$HOME\.cargo\bin"
```

**Solución Linux/Mac:**
```bash
# Agrega a ~/.bashrc o ~/.zshrc:
export PATH="$HOME/.cargo/bin:$PATH"
source ~/.bashrc
```

### Problema: No se puede activar el entorno virtual

**Solución Windows:**
```powershell
# Si hay error de permisos, ejecuta:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problema: Jupyter no se abre

```bash
# Verifica la instalación:
uv pip list | grep jupyter

# Reinstala si es necesario:
uv pip install --force-reinstall jupyter
```

## 📄 Licencia

[Especifica tu licencia aquí - MIT, Apache 2.0, etc.]

## 📧 Contacto

- **Autor**: [Tu Nombre]
- **Email**: [tu.email@ejemplo.com]
- **LinkedIn**: [Tu perfil de LinkedIn]
- **GitHub**: [Tu usuario de GitHub]

## 🙏 Agradecimientos

- Dataset proporcionado por [Kaggle](https://www.kaggle.com/)
- Comunidad de Python y pandas
- Desarrolladores de uv (Astral)

---

**⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub**

**📚 Proyecto creado con fines educativos y de análisis de datos**

---

*Última actualización: Noviembre 2024*