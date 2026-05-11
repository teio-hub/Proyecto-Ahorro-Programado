<h1>📌 Calculadora de Ahorro Programado 
  <img src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif" width="60px">
</h1>

---
##  Creadores
- María Paula Ospina Zabala
- Alejandro Tello Giraldo
- Hans Schoonewolff Otero
- Carolina Flórez Salazar 
  
 --- 
 ## 👩‍💻 Persona entrevistada
- **Nombre:** Karen Londoño 
- **Cargo:** Gerente de proyectos en una compañía financiera
- **Experiencia relacionada:** Finanzas
- **Fecha de la entrevista:** 08/02/2026

---

## 📖 Descripción del Proyecto
La **Calculadora de Ahorro Programado** es una aplicación diseñada para ayudar a las personas a planificar su ahorro mensual con el fin de alcanzar una meta financiera específica en un periodo de tiempo determinado.
La aplicación permite calcular el valor que se debe ahorrar mensualmente y, además, ofrece la posibilidad de registrar **abonos extra** en cualquier momento y por cualquier cantidad, ajustando el ahorro restante de forma automática.

---
## 🎯 Objetivo
Esta herramienta busca facilitar al usuario una ayuda para alcanzar su meta de ahorro de una manera sencilla, además de brindarle una planificación financiera personal que permita:
-  Definir una meta de ahorro.
-  Establecer un plazo en meses.
-  Calcular el ahorro mensual necesario.
-  Registrar abonos adicionales.
-  Visualizar el progreso del ahorro.
  
---
## ▶️ Funcionamiento

### Prerrequisitos

Antes de comenzar, asegúrese de tener lo siguiente:

- **Python 3** instalado en su computador. Si no lo tiene, descárguelo desde [https://www.python.org/downloads/](https://www.python.org/downloads/)
  > ⚠️ En Windows, durante la instalación marque la casilla **"Add Python to PATH"**
- La carpeta del proyecto descargada en su computador (`Proyecto-Ahorro-Programado`)

---

## 🔎 Opción 1 — Desde la terminal (CMD / Bash)

### Paso 1 — Abrir la terminal

**Windows:** Presione `Windows + R`, escriba `cmd` y presione Enter.

**Mac:** Presione `Cmd + Espacio`, busque **Terminal** y ábrala.

**Linux:** Busque **Terminal** en el menú de aplicaciones.

### Paso 2 — Ir a la carpeta del proyecto

Escriba `cd` seguido de la ruta donde guardó el proyecto. Por ejemplo:

**Windows:**
```cmd
cd C:\Users\TuUsuario\Desktop\Proyecto-Ahorro-Programado
```

**Mac / Linux:**
```bash
cd /Users/TuUsuario/Desktop/Proyecto-Ahorro-Programado
```

> 💡 **Tip:** Puede arrastrar la carpeta del proyecto hacia la ventana de la terminal y la ruta aparecerá automáticamente.

### Paso 3 — Ejecutar el programa

**Windows:**
```cmd
python src\view\interfaz_consola.py
```

**Mac / Linux:**
```bash
python3 src/view/interfaz_consola.py
```

Si todo está bien, verá el menú del programa en pantalla.

### Ejecutar las pruebas unitarias

**Windows:**
```cmd
python -m unittest test\*.py
```

**Mac / Linux:**
```bash
python3 -m unittest test\*.py
```

> ⚠️ Si aparece el error `pytest: command not found`, instálelo primero con:
> ```
> pip install pytest
> ```
> Luego vuelva a ejecutar el comando de pruebas.

Si las pruebas pasaron correctamente, verá un mensaje con `passed` en verde 
Si alguna falló, verá `FAILED` en rojo con una descripción del error 

---

## 🔎 Opción 2 — Desde un entorno de desarrollo (VS Code, PyCharm, etc.)

### Paso 1 — Abrir el proyecto

Abra su entorno de desarrollo y seleccione la opción **"Abrir carpeta"** (o *Open Folder*). Busque y seleccione la carpeta `Proyecto-Ahorro-Programado`.

### Paso 2 — Seleccionar el intérprete de Python

Asegúrese de que su entorno tenga configurado Python 3 como intérprete.

**En VS Code:** Presione `Ctrl + Shift + P`, busque **"Python: Select Interpreter"** y elija la versión de Python 3 instalada en su equipo.

**En PyCharm:** Vaya a `File > Settings > Project > Python Interpreter` y seleccione Python 3.

### Paso 3 — Ejecutar el programa

Abra el archivo `src/view/interfaz_consola.py` y ejecútelo:

**En VS Code:** Presione el botón ▶️ en la esquina superior derecha, o haga clic derecho sobre el archivo y seleccione **"Run Python File"**.

**En PyCharm:** Presione el botón ▶️ en la esquina superior derecha, o haga clic derecho sobre el archivo y seleccione **"Run"**.

Si todo está bien, verá el menú del programa en el panel de terminal interno.

### Ejecutar las pruebas unitarias

Abra el archivo `test/test_ahorro.py` y ejecútelo de la misma forma que el paso anterior.

> 💡 También puede ejecutar las pruebas desde la terminal integrada del entorno (`View > Terminal`) usando el mismo comando de la Opción 1.

---
## 📥 Entradas del Sistema
El usuario debe ingresar:
- **Meta de ahorro (Meta)**  
- **Tasa de interés mensual (i)**  
- **Plazo en meses (n)**  
- **Abonos extra (opcional y siempre en la última cuota)**
- **Valor del abono**

## ⚙️ Proceso del Sistema
La aplicación utiliza la fórmula financiera de ahorro programado:
**Cuota = Meta × [ i / ((1 + i)^n − 1) ]**
Donde:
- **Meta** = Valor objetivo a alcanzar  
- **i** = Tasa de interés mensual  
- **n** = Número de meses  
- **Cuota** = Valor que debe ahorrarse mensualmente  

❗ **Caso especial:** Si la tasa es 0%, se usa: **Cuota = Meta / n** ❗

## Fórmula de cálculo de cuota

**Cuota mensual (sin abono):**
```
C = meta × (r / ((1 + r)^n - 1))
```

**Cuota mensual (con abono extra):**
```
C = (meta - abono) × (r / ((1 + r)^n - 1))
```

**Donde:**
- `r` = tasa de interés mensual
- `n` = plazo en meses
- `abono` = monto del abono extra (reduce la meta directamente)

**Total de intereses ganados (sin abono):**
```
TI = meta - C × n
```

**Total de intereses ganados (con abono):**
```
TI = (meta - abono) - C × n
```

### Funcionamiento:
1. **Validación:** Se verifican que meta, plazo y tasa sean válidos.
2. **Cálculo inicial:** Se determina la cuota mensual con base en la fórmula.
3. **Simulación mes a mes:** Se proyecta el crecimiento del ahorro aplicando los intereses.
4. **Abonos extras (opcional):**
   - Se suman al capital acumulado en el último mes (en caso de ser dos abonos, los dos se hacen en el último mes).
   - Empiezan a generar intereses inmediatamente.
   - Se recalcula la cuota para los meses restantes.
5. **Resultado final:** Se muestra la cuota mensual, total de intereses y total ahorrado.

---
## 📤 Salidas del Sistema
El sistema mostrará:
-  **Cuota mensual:** Valor que debe ahorrarse cada mes para alcanzar la meta.
-  **Total de intereses:** Dinero adicional generado durante el periodo de ahorro.
-  **Total ahorrado:** Suma de la meta más los intereses ganados.
-  **Nuevo plan tras abonos:** Si se realizan abonos extras, muestra la cuota recalculada.
-  **Confirmación de meta:** Mensaje cuando la meta sea alcanzada.

### Mensajes de Error
En caso de datos inválidos, el sistema indica qué dato causó el problema y cómo corregirlo:

- ❌ `MetaInvalida`: "ERROR: La meta debe ser mayor que cero. Se recibió meta={valor}. Ingrese un valor positivo."
- ❌ `PlazoInvalido`: "ERROR: El plazo no puede ser cero. Se recibió plazo={valor}. Ingrese un plazo de al menos 1 mes."
- ❌ `PlazoInvalido`: "ERROR: El plazo no puede ser negativo. Se recibió plazo={valor}. Ingrese un plazo de al menos 1 mes."
- ❌ `InteresInvalido`: "ERROR: La tasa de interés no puede ser negativa. Se recibió interes={valor}. Ingrese una tasa mayor o igual a cero."
- ❌ `MesAbonoInvalido`: "ERROR: El mes del abono no es válido. Se recibió mes_abono={valor} con plazo={valor}. El mes debe estar entre 1 y {plazo}."

---

### Descripción carpetas
- **`src/model/`** — Contiene la lógica del sistema. En esta carpeta se 
  encuentra el archivo `logica_ahorro.py`, responsable de ejecutar todos los 
  cálculos financieros del programa: la cuota mensual, los intereses generados 
  y el recálculo del plan ante la presencia de abonos extraordinarios.

- **`src/view/`** — Contiene la presentación del sistema. El archivo 
  `interfaz_consola.py` gestiona la comunicación entre el programa y el usuario, 
  mostrando los mensajes en pantalla, solicitando los datos de entrada y 
  presentando los resultados obtenidos.

- **`test/`** — Contiene las pruebas de validación del sistema. El archivo 
  `test_ahorro.py` agrupa un conjunto de pruebas automatizadas que verifican 
  el correcto funcionamiento de la lógica del programa frente a distintos 
  escenarios de uso.


---
