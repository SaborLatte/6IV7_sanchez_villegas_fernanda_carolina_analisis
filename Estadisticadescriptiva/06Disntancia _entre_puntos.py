import numpy as np
import pandas as pd
from scipy.spatial import distance

# Definimos las coordenadas de neustro sistema de tiendas
tiendas= {
        'tienda A': (1,1),
          'tienda B': (1,5),
          'tienda C': (7,1),
          'tienda D': (3,3),
          'tienda E': (4,8)
          }
#CONVERTIR LAS COORDENADAS EN UN FRAME PARA FACILITAR EL CALCULO 

df_tiendas=pd.DataFrame(tiendas).T
df_tiendas.columns=['X','Y']
print('Coordenadas de las teindas')
print(df_tiendas)
#inicializamos los data frame de lo que vamos a obtener para el calculo de distancias

distancias_punto1=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)

distancias_punto2=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)

distancias_punto3=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)

#aplicar el recorrido, vamos a calcular las distancias
for i in df_tiendas.index:
    for j in df_tiendas.index:
        #defino la distancia euclidiana delprimer punto
        distancias_punto1.loc[i,j]=distance.euclidean(df_tiendas.loc[i],df_tiendas.loc[j])
        distancias_punto2.loc[i,j]=distance.cityblock(df_tiendas.loc[i],df_tiendas.loc[j])
        distancias_punto3.loc[i,j]=distance.chebyshev(df_tiendas.loc[i],df_tiendas.loc[j])
        
#Mostrar resultados
print('/n Distancia euclideana entre cada una de las tiendas:' )
print(distancias_punto1)

print('/n Distancia Manhatthan entre cada una de las tiendas:' )
print(distancias_punto2)

print('/n Distancia Chebyshev entre cada una de las tiendas:' )
print(distancias_punto3)
