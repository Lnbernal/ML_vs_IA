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