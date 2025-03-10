import pandas as pd 
# crear una funcion que  se encargue de recibir un diccionario de las notas de los estudiantes de analisis de datos 
# que vana a reprobar y obtener su min, max y med, y desviacion est

def estadisticas_notas(notas):
    notas= pd.Series(notas)
    estadistica= pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min','Max', 'Media', 'Desviación estandar'])
    return estadistica
notas={'Juan':9, 'Juanita':5.9,'Pedro': 8.2, 'Rosalba':6.9, 'Federico':4.5,'Alberto': 7.5}
print(estadisticas_notas(notas))