Semana 2 Comandos principales de Numpy - Machine Learning 601N

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
=======
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
