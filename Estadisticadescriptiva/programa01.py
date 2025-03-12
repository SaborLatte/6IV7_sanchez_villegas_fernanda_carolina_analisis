import pandas as pd
import matplotlib.pyplot as plt

def housing(fichero):
    df = pd.read_csv(fichero, sep=',', thousands='.', dtype={'ocean_proximity': str})  
    df_numeric = df.select_dtypes(include=['number'])  
    return pd.DataFrame([df_numeric.min(), df_numeric.max(), df_numeric.mean(), df_numeric.std(),df_numeric.mode().iloc[0],df_numeric.max() - df_numeric.min(),df_numeric.var(),], 
                        index=['Minimo', 'Maximo', 'Media', 'Desviación estándar','Moda','Rango','Varianza'])

pd.set_option('display.max_columns', None)

print(housing('./Estadisticadescriptiva/housing.csv'))

dt = pd.read_csv('./Estadisticadescriptiva/housing.csv')

dt["population_range"] = pd.cut(dt["population"], bins=10)
grouped = dt.groupby("population_range")["median_house_value"].mean()

mean_value = dt["median_house_value"].mean()

plt.figure(figsize=(15, 7))
plt.bar(grouped.index.astype(str), grouped.values, color='purple', width=0.8)

plt.axhline(mean_value, color='blue', linestyle='-', linewidth=2, label=f'Promedio: {mean_value:.2f}')

# Etiquetas
plt.xlabel('Rango de Población')
plt.ylabel('Valor Medio de la Casa')
plt.title('Gráfico de Barras: Rango de Población vs Valor Medio de la Casa')

plt.xticks(rotation=45)

plt.legend()

plt.show()