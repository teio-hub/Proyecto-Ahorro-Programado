# Aplicación para gestionar planes de ahorro, usuarios y abonos, con interfaz gráfica en Kivy y aplicación web con Flask, conectada a una base de datos PostgreSQL en Render.

---

## 1. Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.10 o superior
- pip actualizado
- Git instalado

Instala las dependencias necesarias:
```bash
pip install flask kivy psycopg2-binary
```

---

## 2. Obtener el proyecto

**Opción A — Clonar el repositorio:**
```bash
git clone https://github.com/ilyyy-bit/Proyecto-Ahorro-Programado.git
```

**Opción B — Descargar el ZIP:**
En GitHub, haz click en **Code** → **Download ZIP**, descomprime la carpeta y ábrela.

---

## 3. Configurar la conexión a la base de datos

Necesitas crear un archivo llamado `secret_config.py` en la raíz del proyecto. Puedes guiarte del archivo `secret_config_sample.py` que ya está incluido — solo copia ese archivo, renómbralo a `secret_config.py` y rellena los datos:

En Mac/Linux:
```bash
cp secret_config_sample.py secret_config.py
```
En Windows:
```bash
copy secret_config_sample.py secret_config.py
```

O simplemente crea el archivo `secret_config.py` manualmente en la raíz del proyecto con este contenido:
```python
PGHOST = "tu-host.render.com"
PGDATABASE = "nombre_de_tu_base"
PGUSER = "tu_usuario"
PGPASSWORD = "tu_contraseña"
PGPORT = "5432"
```
Puedes encontrar estos datos en Render → tu base de datos → **Connect** → **External Database URL**.

---

## 4. Crear las tablas en la base de datos

**Opción A:** Desde la aplicación web, haz click en el link **"crear las tablas en la base de datos"** que aparece en cada página.

**Opción B:** Ejecuta los scripts SQL en este orden desde VS Code con la extensión PostgreSQL:
```sql
-- 1. Crear usuarios
\i sql/crear-usuarios.sql

-- 2. Crear planes de ahorro
\i sql/crear-planes.sql

-- 3. Crear abonos
\i sql/crear-abonos.sql
```

---

## 5. Ejecutar la aplicación web

**Primera vez que ejecutas la aplicación:**

1. Abre la terminal (PowerShell o CMD en Windows)
2. Navega a la carpeta donde clonaste el repositorio. Si la ruta tiene espacios, usa comillas:
```
cd "C:\ruta\donde\clonaste\Proyecto-Ahorro-Programado"
```
3. Ejecuta el archivo bat desde la terminal:
```
.\run.bat
```
4. Abre el navegador en:
```
http://127.0.0.1:5000
```

**Las siguientes veces:**

Una vez que hayas ejecutado el paso anterior al menos una vez, puedes simplemente hacer doble clic en `run.bat` para iniciar la aplicación.

**Alternativa (sin usar run.bat):**
```
cd "C:\ruta\donde\clonaste\Proyecto-Ahorro-Programado"
python app.py
```

### Aplicación publicada en línea
```
https://proyecto-ahorro-programado-web.onrender.com
```

---

## 6. Ejecutar la interfaz gráfica (Kivy)

1. Abre la terminal y navega a la carpeta del proyecto:
```
cd "C:\ruta\donde\clonaste\Proyecto-Ahorro-Programado"
```
2. Ejecuta:
```
python src/view/gestion_gui.py
```

---

## 7. Ejecutar los tests

Desde la raíz del proyecto:
```bash
python test/test_usuarios.py
python test/test_planes.py
python test/test_abonos.py
```

---

## 8. Estructura del proyecto

```
Proyecto-Ahorro-Programado/
├── sql/
│   ├── crear-usuarios.sql
│   ├── crear-planes.sql
│   ├── crear-abonos.sql
│   └── borrar-tablas.sql
├── src/
│   ├── controller/
│   │   ├── usuarios_controller.py
│   │   ├── planes_controller.py
│   │   └── abonos_controller.py
│   ├── model/
│   │   ├── __init__.py
│   │   ├── Abono.py
│   │   ├── logica_ahorro.py
│   │   ├── PlanAhorro.py
│   │   └── Usuario.py
│   ├── view/
│   │   ├── __init__.py
│   │   ├── ahorros_gui.py
│   │   ├── gestion_gui.py
│   │   └── interfaz_consola.py
│   └── view_web/
│       ├── __init__.py
│       └── vista_ahorro.py
├── templates/
│   ├── pagina_inicio.html
│   ├── planes.html
│   ├── plan_buscado.html
│   ├── plan_modificar.html
│   ├── usuarios.html
│   ├── usuario_buscado.html
│   ├── usuario_modificar.html
│   ├── abonos.html
│   ├── abono_buscado.html
│   └── abono_modificar.html
├── test/
│   ├── __init__.py
│   ├── test_abonos.py
│   ├── test_ahorro.py
│   ├── test_planes.py
│   └── test_usuarios.py
├── app.py
├── run.bat
├── secret_config_sample.py
├── requirements.txt
└── README.md
```
