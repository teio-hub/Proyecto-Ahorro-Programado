# Aplicación para gestionar planes de ahorro, usuarios y abonos, con interfaz gráfica en Kivy y base de datos PostgreSQL en Render.

---

## 1. Requisitos previos

- Python 3.10 o superior
- pip actualizado

---

## 2. Clonar el repositorio

```bash
git clone https://github.com/manolo-restrepo/Proyecto-Ahorro-Programado.git
cd Proyecto-Ahorro-Programado
```

---

## 3. Instalar dependencias

```bash
pip install kivy psycopg2-binary
```

---

## 4. Configurar la conexión a la base de datos

1. Copia el archivo de ejemplo:

```bash
cp secret_config_sample.py secret_config.py
```

2. Abre `secret_config.py` y rellena con tus datos de Render:

```python
PGHOST = "tu-host.render.com"
PGDATABASE = "nombre_de_tu_base"
PGUSER = "tu_usuario"
PGPASSWORD = "tu_contraseña"
PGPORT = "5432"
```

Puedes encontrar estos datos en el panel de Render → tu base de datos → **Connection Details**.

---

## 5. Crear las tablas en la base de datos

Ejecuta los scripts SQL en este orden desde tu cliente PostgreSQL (por ejemplo VS Code con la extensión PostgreSQL):

```sql
-- 1. Crear usuarios
\i sql/crear-usuarios.sql

-- 2. Crear planes de ahorro
\i sql/crear-planes.sql

-- 3. Crear abonos
\i sql/crear-abonos.sql
```

---

## 6. Ejecutar la interfaz gráfica

Desde la raíz del proyecto:

```bash
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
|   ├── README
│   ├── model/
│   │   ├── __init__.py
│   │   ├── Abono.py
│   │   ├── logica_ahorro.py
│   │   ├── PlanAhorro.py
│   │   └── Usuario.py
│   └── view/
│       ├── __init__.py
│       ├── ahorros_gui.py
│       ├── gestion_gui.py
│       └── interfaz_consola.py
├── test/
│   ├── __init__.py
│   ├── test_abonos.py
│   ├── test_ahorro.py
│   ├── test_planes.py
│   └── test_usuarios.py
├── secret_config_sample.py
├── secret_config.py
└── README.md
```
