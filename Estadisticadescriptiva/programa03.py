import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance

puntos = {
    'A': (2, 3),
    'B': (5, 4),
    'C': (1, 1),
    'D': (6, 7),
    'E': (3, 5),
    'F': (8, 2),
    'G': (4, 6),
    'H': (2, 1)
}

df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']

print(' Coordenadas de los puntos:\n')
print(df_puntos)

dist_euclidiana = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
dist_manhattan = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
dist_chebyshev = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)

for i in df_puntos.index:
    for j in df_puntos.index:
        dist_euclidiana.loc[i, j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
        dist_manhattan.loc[i, j] = distance.cityblock(df_puntos.loc[i], df_puntos.loc[j])
        dist_chebyshev.loc[i, j] = distance.chebyshev(df_puntos.loc[i], df_puntos.loc[j])

# Mostrar resultados
print('\n Distancia Euclidiana entre cada par de puntos:\n')
print(dist_euclidiana)

print('\n Distancia Manhattan entre cada par de puntos:\n')
print(dist_manhattan)

print('\n Distancia Chebyshev entre cada par de puntos:\n')
print(dist_chebyshev)

plt.figure(figsize=(8, 8))
for label, (x, y) in puntos.items():
    plt.plot(x, y, 'bo')  
    plt.text(x + 0.1, y + 0.1, label, fontsize=12) 

# Conexiones opcionales (por ejemplo, más cercanos o lejanos)
# Más cercano (C-H)
plt.plot([puntos['C'][0], puntos['H'][0]], [puntos['C'][1], puntos['H'][1]], 'g--', label='Más cercano (C-H)')
# Más lejano (C-D)
plt.plot([puntos['C'][0], puntos['D'][0]], [puntos['C'][1], puntos['D'][1]], 'r-', label='Más lejano (C-D)')
# Chebyshev máximo (C-F)
plt.plot([puntos['C'][0], puntos['F'][0]], [puntos['C'][1], puntos['F'][1]], 'm:', label='Chebyshev máximo (C-F)')

plt.title('Distribución de puntos en el plano')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
