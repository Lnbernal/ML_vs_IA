**Hecho por Juan Pinzón: C) Pandas – Creación y manipulación de DataFrames y Series**
**¿Qué es Pandas?**


Pandas facilita tareas como:
    -Cargar datos desde archivos (CSV, Excel, SQL, JSON).
    -Seleccionar, filtrar y transformar información.
    -Modificar tipos de datos y realizar operaciones estadísticas.


Pandas es una librería de Python diseñada para el análisis y manipulación de datos. Proporciona 4 estructuras principales:

**1. Creación de Series**

pd.Series(lista) → Crea una serie unidimensional con índices asociados.

**Código:**

import pandas as pd   # Importamos la librería

# ============================
# 1. Creación de Series
# ============================
print("=== Creación de Series ===")
serie1 = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])  # Serie con índices personalizados
print("Serie creada:\n", serie1)

**Salida:**
=== Creación de Series ===
a    10
b    20
c    30
d    40
dtype: int64

**Explicación:**

Se importa la librería pandas.

Creamos una Serie con valores [10, 20, 30, 40] y la indexamos con letras.

Al imprimirla, se muestra cada valor con su índice correspondiente.

**2. Creación de DataFrames**

pd.DataFrame(diccionario) → Crea un DataFrame (tabla) a partir de un diccionario.

**Código:**

# ============================
# 2. Creación de DataFrames
# ============================
print("=== Creación de DataFrame ===")
datos = {
    "Nombre": ["Ana", "Luis", "Pedro"],   # Columna de nombres
    "Edad": [23, 30, 21],                 # Columna de edades
    "Ciudad": ["Bogotá", "Medellín", "Cali"]  # Columna de ciudades
}
df = pd.DataFrame(datos)   # Se crea el DataFrame
print(df)


**Salida:**

=== Creación de DataFrame ===
  Nombre  Edad    Ciudad
0    Ana    23    Bogotá
1   Luis    30  Medellín
2  Pedro    21      Cali


**Explicación:**

El diccionario datos contiene tres listas, cada una será una columna.

pd.DataFrame(datos) convierte ese diccionario en una tabla.

**3. Selección de columnas y filas**

Podemos acceder a columnas completas o filas específicas.

**Código:**

# ============================
# 3. Selección de Datos
# ============================
print("=== Selección de Datos ===")
print("Columna Nombre:\n", df["Nombre"])       # Seleccionar una columna
print("\nFila por índice (iloc[0]):\n", df.iloc[0])  # Fila por posición
print("\nFila por etiqueta (loc[1]):\n", df.loc[1])  # Fila por índice/etiqueta


**Salida:**

=== Selección de Datos ===
Columna Nombre:
0     Ana
1    Luis
2   Pedro
Name: Nombre, dtype: object

Fila por índice (iloc[0]):
Nombre      Ana
Edad         23
Ciudad    Bogotá
Name: 0, dtype: object

Fila por etiqueta (loc[1]):
Nombre        Luis
Edad            30
Ciudad    Medellín
Name: 1, dtype: object


**Explicación:**

df["Nombre"] → Devuelve toda la columna "Nombre".

df.iloc[0] → Selecciona la primera fila por posición.

df.loc[1] → Selecciona la fila con índice 1.

**4. Tipos de datos**

Podemos revisar y modificar los tipos de datos de cada columna.

**Código:**

# ============================
# 4. Tipos de Datos
# ============================
print("=== Tipos de Datos ===")
print(df.dtypes)  # Ver tipos de cada columna

# Convertir tipo de dato
df["Edad"] = df["Edad"].astype(float)  # Convertir Edad a float
print("\nEdad convertida a float:\n", df.dtypes)


**Salida:**

=== Tipos de Datos ===
Nombre    object
Edad       int64
Ciudad    object
dtype: object

Edad convertida a float:
Nombre     object
Edad      float64
Ciudad     object
dtype: object

**Explicación:**

df.dtypes muestra el tipo de cada columna (números, texto, etc.).

Con .astype(float) convertimos la columna "Edad" a números decimales.


Pandas es una herramienta fundamental para el análisis de datos en Python, ya que permite manejar información en estructuras flexibles como Series y DataFrames. Con estas se pueden realizar operaciones de selección, transformación y conversión de tipos de manera sencilla, facilitando la exploración y preparación de los datos para tareas más avanzadas en ciencia de datos y aprendizaje automático.
