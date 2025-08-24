Introducción NumPy (Numerical Python) es una biblioteca de código
abierto para Python que proporciona soporte para trabajar con vectores y
matrices multidimensionales de alto rendimiento, junto con una colección
de funciones matemáticas y lógicas para operarlas.

A)  Arreglos en NumPy

-   Creación de arreglos np.array(lista) → Crea un arreglo a partir de
    una lista o tupla.

Ejemplo: import numpy as np # Importamos la librería #
============================ # 1. Creación de Arreglos #
============================ print(“=== Creación de Arreglos ===”)
arreglo1 = np.array([1, 2, 3, 4, 5]) print(“Arreglo desde lista:”,
arreglo1)

Esto nos devuelve: === Creación de Arreglos === Arreglo desde lista: [1
2 3 4 5]

  -----------------------------------------------------
  - Matrices np.zeros((m,n)) → Genera una matriz de
  ceros. np.ones((m,n)) → Genera una matriz de unos.
  -----------------------------------------------------
  - Operaciones con arreglos Podemos realizar
  operaciones aritméticas directamente entre arreglos,
  aplicándose elemento a elemento.

  Ejemplo: # ============================ # 3.
  Operaciones con arreglos #
  ============================ print(“=== Operaciones
  con arreglos ===”) a = np.array([10, 20, 30]) b =
  np.array([1, 2, 3]) print(“Arreglo a:”, a)
  print(“Arreglo b:”, b)

  suma = a + b multiplicacion = a * b print(“Suma:”,
  suma) print(“Multiplicación:”, multiplicacion)

  Esto nos devuelve: === Operaciones con arreglos ===
  Arreglo a: [10 20 30] Arreglo b: [1 2 3] Suma: [11 22
  33] Multiplicación: [10 40 90]
  -----------------------------------------------------

-   Estadísticos básicos NumPy permite obtener medidas estadísticas de
    manera sencilla.

Ejemplo: # ============================ # 4. Estadísticos básicos #
============================ print(“=== Estadísticos básicos ===”) datos
= np.array([5, 10, 15, 20, 25]) print(“Datos:”, datos)

promedio = np.mean(datos) maximo = np.max(datos) minimo = np.min(datos)
print(“Promedio:”, promedio) print(“Máximo:”, maximo) print(“Mínimo:”,
minimo)

Esto nos devuelve: === Estadísticos básicos === Datos: [ 5 10 15 20 25]
Promedio: 15.0 Máximo: 25 Mínimo: 5

  -----------------------------------------------------
  - Uso de np.arange np.arange(inicio, fin, paso)
  genera un arreglo en un rango definido.
  -----------------------------------------------------
  - Uso de np.linspace np.linspace(inicio, fin, num)
  genera un arreglo con valores igualmente espaciados.

  Ejemplo: # ============================ # 6. Uso de
  np.linspace # ============================ print(“===
  Uso de np.linspace ===”) linea = np.linspace(0, 1, 5)
  # 5 valores entre 0 y 1 print(“np.linspace(0, 1,
  5):”, linea)

  Esto nos devuelve: === Uso de np.linspace ===
  np.linspace(0, 1, 5): [0. 0.25 0.5 0.75 1. ]
  -----------------------------------------------------

-   Propiedades de un arreglo Los arreglos en NumPy tienen propiedades
    que nos permiten conocer sus características:

.shape → Dimensiones del arreglo .size → Número total de elementos
.dtype → Tipo de datos de los elementos

Ejemplo: # ============================ # 7. Propiedades de un arreglo #
============================ print(“=== Propiedades de un arreglo ===”)
arr = np.array([[1, 2, 3], [4, 5, 6]]) print(“Arreglo:”, arr)
print(“Dimensiones (shape):”, arr.shape) print(“Número de elementos
(size):”, arr.size) print(“Tipo de datos (dtype):”, arr.dtype)

Esto nos devuelve: === Propiedades de un arreglo === Arreglo: [[1 2 3]
[4 5 6]] Dimensiones (shape): (2, 3) Número de elementos (size): 6 Tipo
de datos (dtype): int32
