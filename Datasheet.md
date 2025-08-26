# **Semana 2 Comandos principales de Numpy - Machine Learning 601N**

Nicolas Bernal A-numpy-arreglos
# Introducion
NumPy (Numerical Python) es una biblioteca de código abierto para Python que proporciona soporte para trabajar con vectores y matrices multidimensionales de alto rendimiento, junto con una colección de funciones matemáticas y lógicas para operarlas
## A) Arreglos en Numpy

- Creación de arreglos

np.array(lista) → Crea un arreglo a partir de una lista o tupla.

- ej:

```python
import numpy as np  # Importamos la librería
# ============================
# 1. Creación de Arreglos
# ============================
print("=== Creación de Arreglos ===")
arreglo1 = np.array([1, 2, 3, 4, 5])
print("Arreglo desde lista:", arreglo1)
```
- Esto nos devuelve:
```python
=== Creación de Arreglos ===
Arreglo desde lista: [1 2 3 4 5]
```
---

- Matrices  
np.zeros((m,n)) → Genera una matriz de ceros.  
np.ones((m,n)) → Genera una matriz de unos.  

- ej:
```python
# ============================
# 2. Arreglos de ceros y unos
# ============================
print("\n=== Crear un arreglo de ceros y unos ===")
ceros = np.zeros((3,3))   # Matriz 3x3 de ceros
unos = np.ones((2,4))     # Matriz 2x4 de unos
print("Matriz de ceros:\n", ceros)
print("Matriz de unos:\n", unos)
``` 
- esto nos devuelve
```python
=== Crear un arreglo de ceros y unos ===
Matriz de ceros:
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
Matriz de unos:
 [[1. 1. 1. 1.]
 [1. 1. 1. 1.]]
```
 ---

- Operaciones con arreglos  

Podemos realizar operaciones aritméticas directamente entre arreglos, aplicándose elemento a elemento.

- ej
```python
# ============================
# 3. Operaciones con arreglos
# ============================
print("\n=== Operaciones con arreglos ===")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print("Arreglo a:", a)
print("Arreglo b:", b)

suma = a + b
multiplicacion = a * b
print("Suma:", suma)
print("Multiplicación:", multiplicacion)
```

- Esto nos devuelve:
```python
=== Operaciones con arreglos ===
Arreglo a: [10 20 30]
Arreglo b: [1 2 3]
Suma: [11 22 33]
Multiplicación: [10 40 90]
```
---

- Estadísticos básicos  

NumPy permite obtener medidas estadísticas de manera sencilla.

- ej:
```python
# ============================
# 4. Estadísticos básicos
# ============================
print("\n=== Estadísticos básicos ===")
datos = np.array([5, 10, 15, 20, 25])
print("Datos:", datos)

promedio = np.mean(datos)
maximo = np.max(datos)
minimo = np.min(datos)
print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)
```

- Esto nos devuelve:
```python
=== Estadísticos básicos ===
Datos: [ 5 10 15 20 25]
Promedio: 15.0
Máximo: 25
Mínimo: 5
```

---

- Uso de np.arange  

np.arange(inicio, fin, paso) genera un arreglo en un rango definido.

- ej:
```python
# ============================
# 5. Uso de np.arange
# ============================
print("\n=== Uso de np.arange ===")
rango = np.arange(0, 10, 2)  # Desde 0 hasta 8, con paso de 2
print("np.arange(0, 10, 2):", rango)
```

- Esto nos devuelve:
```python
=== Uso de np.arange ===
np.arange(0, 10, 2): [0 2 4 6 8]
```
---

- Uso de np.linspace  

np.linspace(inicio, fin, num) genera un arreglo con valores igualmente espaciados.

- ej:
```python
# ============================
# 6. Uso de np.linspace
# ============================
print("\n=== Uso de np.linspace ===")
linea = np.linspace(0, 1, 5)  # 5 valores entre 0 y 1
print("np.linspace(0, 1, 5):", linea)
```

- Esto nos devuelve:
```python
=== Uso de np.linspace ===
np.linspace(0, 1, 5): [0.   0.25 0.5  0.75 1.  ]

```
---

- Propiedades de un arreglo  

Los arreglos en NumPy tienen propiedades que nos permiten conocer sus características:  

.shape → Dimensiones del arreglo  

.size → Número total de elementos  

.dtype → Tipo de datos de los elementos  

- ej:
```python
# ============================
# 7. Propiedades de un arreglo
# ============================
print("\n=== Propiedades de un arreglo ===")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Arreglo:\n", arr)
print("Dimensiones (shape):", arr.shape)
print("Número de elementos (size):", arr.size)
print("Tipo de datos (dtype):", arr.dtype)

```
- Esto nos devuelve:
```python
=== Propiedades de un arreglo ===
Arreglo:
 [[1 2 3]
  [4 5 6]]
Dimensiones (shape): (2, 3)
Número de elementos (size): 6
Tipo de datos (dtype): int32
```
--------------------------------------_______________________---------------------------------------------
B-numpy-estadisticas
**_Punto B - Juan Hernández_**
**Guía de NumPy - Operaciones estadísticas y funciones avanzadas**

NumPy no solo permite crear y manipular arreglos, también incluye funciones estadísticas, generación de 
números aleatorios y herramientas para álgebra lineal, lo que lo hace fundamental para análisis de 
datos y cálculos científicos.

**B Operaciones estadísticas y funciones avanzadas en NumPy**
**__1.Funciones estadísticas básicas:__** NumPy facilita el cálculo de medidas estadísticas comunes sobre 
arreglos:

-np.mean() → Calcula la media (promedio).
-np.std() → Calcula la desviación estándar.
-np.sum() → Calcula la suma de los elementos.

```python
import numpy as np  # Importamos la librería
# ============================
# 1. Funciones estadísticas básicas
# ============================
print("== Funciones estadísticas básicas ==")
import numpy as np

datos = np.array([10, 20, 30, 40, 50])
print("Datos:", datos)

media = np.mean(datos)
desviacion = np.std(datos)
suma = np.sum(datos)

print("Media:", media)
print("Desviación estándar:", desviacion)
print("Suma total:", suma)
```
- Esto nos devuelve como salida:
```python
== Funciones estadísticas básicas ==
Datos: [10 20 30 40 50]
Media: 30.0
Desviación estándar: 14.142135623730951
Suma total: 150
```
**_2.Generación de secuencias con arange y linspace_**
Estas funciones permiten generar secuencias numéricas rápidamente:

-np.arange(inicio, fin, paso) → Genera números en un rango con un paso definido.
-np.linspace(inicio, fin, num) → Genera un número fijo de valores igualmente espaciados.

```python
# ============================
# 2. Secuencias
# ============================
print("\n== Secuencias con arange y linspace ==")
rango = np.arange(1, 10, 2)       # Desde 1 hasta 9 con paso de 2
linea = np.linspace(0, 1, 5)      # 5 valores entre 0 y 1

print("np.arange(1, 10, 2):", rango)
print("np.linspace(0, 1, 5):", linea)
```
- Esto nos devuelve como salida:
```python
== Secuencias con arange y linspace ==
np.arange(1, 10, 2): [1 3 5 7 9]
np.linspace(0, 1, 5): [0.   0.25 0.5  0.75 1.  ]
```
**_3.Números aleatorios con np.random_**
NumPy permite generar números aleatorios para simulaciones o pruebas:

-np.random.rand(n) → Genera n números aleatorios entre 0 y 1.
-np.random.randint(min, max, size) → Enteros aleatorios en un rango.

```python
# ============================
# 3. Aleatorios
# ============================
print("\n== Números aleatorios ==")
aleatorios = np.random.rand(5)         # 5 números aleatorios [0,1)
enteros = np.random.randint(1, 10, 5)  # 5 enteros entre 1 y 9

print("Aleatorios (0-1):", aleatorios)
print("Enteros (1-9):", enteros)
```
- Esto nos devuelve como salida:
Numeros aleatorios y enteros

**_4.Álgebra lineal con NumPy_**
NumPy incluye operaciones básicas de álgebra lineal, las cuales són:

-np.dot(a,b) → Producto punto.
-np.matmul(a,b) → Multiplicación de matrices.
-np.linalg.inv(matriz) → Inversa de una matriz.
-np.linalg.det(matriz) → Determinante.

```python
# ============================
# 4. Algebra Lineal
# ============================
print("\n== Álgebra lineal ==")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

producto_punto = np.dot(A, B)
inversa = np.linalg.inv(A)
determinante = np.linalg.det(A)

print("Matriz A:\n", A)
print("Matriz B:\n", B)
print("Producto punto (A·B):\n", producto_punto)
print("Inversa de A:\n", inversa)
print("Determinante de A:", determinante)
```
- Esto nos devuelve como salida:
```python
== Álgebra lineal ==
Matriz A:
 [[1 2]
 [3 4]]
Matriz B:
 [[5 6]
 [7 8]]
Producto punto (A·B):
 [[19 22]
 [43 50]]
Inversa de A:
 [[-2.   1. ]
 [ 1.5 -0.5]]
Determinante de A: -2.0000000000000004
```
**_5.Reshape y concatenación(extra)_**

-reshape(n,m) → Cambia la forma del arreglo sin modificar los datos.
-np.concatenate([a,b]) → Une arreglos.

```python
# =========================================
# 5. Cambiar arreglos o unir arreglos
# =========================================
print("\n== Reshape y concatenación ==")
arr = np.arange(1, 7)  # [1 2 3 4 5 6]
print("Arreglo original:", arr)

matriz = arr.reshape((2, 3))
print("Arreglo como matriz 2x3:\n", matriz)

a = np.array([1, 2])
b = np.array([3, 4])
concatenado = np.concatenate((a, b))
print("Concatenación:", concatenado)
```
- Esto nos devuelve como salida:
```python
== Reshape y concatenación ==
Arreglo original: [1 2 3 4 5 6]
Arreglo como matriz 2x3:
 [[1 2 3]
 [4 5 6]]
Concatenación: [1 2 3 4]
```
El Punto B trata sobre operaciones estadísticas y funciones avanzadas en NumPy, incluyendo cálculo de 
medidas como media y desviación estándar, generación de secuencias y números aleatorios, operaciones de 
álgebra lineal (producto punto, determinante, inversa) y manipulación de arreglos con reshape y 
concatenate.

--------------------------------_______________________________---------------------------------

C-pandas-dataframes
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
```python
import pandas as pd   # Importamos la librería

# ============================
# 1. Creación de Series
# ============================
print("=== Creación de Series ===")
serie1 = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])  # Serie con índices personalizados
print("Serie creada:\n", serie1)
```

**Salida:**
```python
=== Creación de Series ===
a    10
b    20
c    30
d    40
dtype: int64
```

**Explicación:**

Se importa la librería pandas.

Creamos una Serie con valores [10, 20, 30, 40] y la indexamos con letras.

Al imprimirla, se muestra cada valor con su índice correspondiente.

**2. Creación de DataFrames**

pd.DataFrame(diccionario) → Crea un DataFrame (tabla) a partir de un diccionario.

**Código:**
```python
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
```

**Salida:**
```python
=== Creación de DataFrame ===
  Nombre  Edad    Ciudad
0    Ana    23    Bogotá
1   Luis    30  Medellín
2  Pedro    21      Cali
```

**Explicación:**

El diccionario datos contiene tres listas, cada una será una columna.

pd.DataFrame(datos) convierte ese diccionario en una tabla.

**3. Selección de columnas y filas**

Podemos acceder a columnas completas o filas específicas.

**Código:**
```python
# ============================
# 3. Selección de Datos
# ============================
print("=== Selección de Datos ===")
print("Columna Nombre:\n", df["Nombre"])       # Seleccionar una columna
print("\nFila por índice (iloc[0]):\n", df.iloc[0])  # Fila por posición
print("\nFila por etiqueta (loc[1]):\n", df.loc[1])  # Fila por índice/etiqueta
```

**Salida:**
```python
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
```

**Explicación:**

df["Nombre"] → Devuelve toda la columna "Nombre".

df.iloc[0] → Selecciona la primera fila por posición.

df.loc[1] → Selecciona la fila con índice 1.

**4. Tipos de datos**

Podemos revisar y modificar los tipos de datos de cada columna.

**Código:**
```python
# ============================
# 4. Tipos de Datos
# ============================
print("=== Tipos de Datos ===")
print(df.dtypes)  # Ver tipos de cada columna

# Convertir tipo de dato
df["Edad"] = df["Edad"].astype(float)  # Convertir Edad a float
print("\nEdad convertida a float:\n", df.dtypes)
```

**Salida:**
```python
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
```
**Explicación:**

df.dtypes muestra el tipo de cada columna (números, texto, etc.).

Con .astype(float) convertimos la columna "Edad" a números decimales.


Pandas es una herramienta fundamental para el análisis de datos en Python, ya que permite manejar información en estructuras flexibles como Series y DataFrames. Con estas se pueden realizar operaciones de selección, transformación y conversión de tipos de manera sencilla, facilitando la exploración y preparación de los datos para tareas más avanzadas en ciencia de datos y aprendizaje automático.
--------------------------------------------------_______________________________---------------------------------
D-pandas-avanzado
# ==============================
# Punto D – Carlos Andrés Romero
# Pandas: Operaciones avanzadas en DataFrames
# ==============================

import pandas as pd

# ==============================
# 1. Manejo de valores nulos – fillna y dropna
# Definición:
## Los valores nulos representan datos faltantes en un DataFrame.
## Con fillna() se pueden reemplazar con valores como la media o un número fijo.
## Con dropna() se eliminan filas o columnas que tengan datos faltantes.
# ==============================
```python
print("\n== 1. Manejo de valores nulos ==")

data = {
    'ID': [1, 2, 3, 4, 5],
    'Nombre': ['Ana', 'Luis', 'Sofía', 'Carlos', 'María'],
    'Edad': [23, 30, 28, None, 35],
    'Ciudad': ['Chía', 'Tabio', 'Cajicá', 'Chía', None]
}

df = pd.DataFrame(data)
print("\nDataFrame original:\n", df)

# Rellenar valores nulos en 'Edad' con la media
df['Edad'] = df['Edad'].fillna(df['Edad'].mean())

# Eliminar filas donde falte 'Ciudad'
df_sin_nulos = df.dropna(subset=['Ciudad'])
print("\nDataFrame sin nulos:\n", df_sin_nulos)
```

- Salida esperada 
```python
 DataFrame original:
    ID  Nombre   Edad  Ciudad
 0   1     Ana   23.0    Chía
 1   2    Luis   30.0   Tabio
 2   3   Sofía   28.0  Cajicá
 3   4  Carlos    NaN    Chía
 4   5   María   35.0    NaN
 ```

- DataFrame sin nulos:
 ```python
    ID  Nombre       Edad  Ciudad
 0   1     Ana  23.000000    Chía
 1   2    Luis  30.000000   Tabio
 2   3   Sofía  28.000000  Cajicá
 3   4  Carlos  29.000000    Chía
```

# ==============================
# 2. Filtro con condiciones
# Definición:
## Los filtros permiten seleccionar filas que cumplen una condición lógica,
## como "mayores de 25 años" o "ciudad igual a Chía".
# ==============================

```python
print("\n== 2. Filtro con condiciones ==")

# Filtrar personas mayores de 25 años
filtro = df_sin_nulos[df_sin_nulos['Edad'] > 25]
print("\nMayores de 25 años:\n", filtro)

```

- Salida esperada 
```python
Mayores de 25 años:
    ID  Nombre   Edad  Ciudad
 1   2    Luis   30.0   Tabio
 2   3   Sofía   28.0  Cajicá
 3   4  Carlos   29.0    Chía
 ```


# ==============================
# 3. Agrupación – groupby
# Definición:
## La función groupby() se usa para agrupar datos por una o más columnas.
## Luego se pueden aplicar funciones como mean(), sum(), count() sobre esos grupos.
# ==============================

```python

print("\n== 3. Agrupación por Ciudad ==")

# Agrupar por ciudad y calcular el promedio de edad
agrupado = df_sin_nulos.groupby('Ciudad')['Edad'].mean().reset_index()
print("\nPromedio de edad por ciudad:\n", agrupado)

```

- Salida esperada
```python
Promedio de edad por ciudad:
   Ciudad       Edad
 0  Cajicá  28.000000
 1    Chía  26.000000
 2   Tabio  30.000000
 ```


# ==============================
# 4. Unión de DataFrames – merge
# Definición:
## El método merge() permite unir dos DataFrames,
## similar a los "JOIN" en SQL, combinando datos con columnas en común.
# ==============================
```python

print("\n== 4. Unión de DataFrames ==")

# Segundo DataFrame con información extra
data_extra = {
    'Ciudad': ['Chía', 'Tabio', 'Cajicá'],
    'Depto': ['Cundinamarca', 'Cundinamarca', 'Cundinamarca']
}
df_extra = pd.DataFrame(data_extra)

# Merge con la información extra
df_merged = pd.merge(df_sin_nulos, df_extra, on='Ciudad', how='left')
print("\nDataFrame unido:\n", df_merged)

```

- Salida esperada
```python
DataFrame unido:
    ID  Nombre   Edad  Ciudad        Depto
 0   1     Ana   23.0    Chía  Cundinamarca
 1   2    Luis   30.0   Tabio  Cundinamarca
 2   3   Sofía   28.0  Cajicá  Cundinamarca
 3   4  Carlos   29.0    Chía  Cundinamarca
 ```


# ==============================
# 5. Exportación a CSV y Excel
# Definición:
## Con to_csv() y to_excel() se pueden exportar los datos a archivos externos.
## Con read_csv() o read_excel() se pueden volver a importar para trabajar en Python.
# ==============================
```python

print("\n== 5. Exportación de archivos ==")

# Exportar a CSV y Excel
df_merged.to_csv("turismo.csv", index=False)
df_merged.to_excel("turismo.xlsx", index=False)

# Importar de nuevo desde CSV
df_importado = pd.read_csv("turismo.csv")
print("\nImportado desde CSV:\n", df_importado)

```

- Salida esperada 
```python
Importado desde CSV:
    ID  Nombre   Edad  Ciudad        Depto
 0   1     Ana   23.0    Chía  Cundinamarca
 1   2    Luis   30.0   Tabio  Cundinamarca
 2   3   Sofía   28.0  Cajicá  Cundinamarca
 3   4  Carlos   29.0    Chía  Cundinamarca
 ```
