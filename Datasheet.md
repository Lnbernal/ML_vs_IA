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
