import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('./Estadisticadescriptiva/housing.csv')

print(df.head())

print(df.tail())

print(df.iloc[7])

print(df["ocean_proximity"])

mediacuartos= df["total_rooms"].mean()
print('Media de cuartos', mediacuartos)

medianapopularidad= df["population"].median()
print('Mediana de plpularidad: ', medianapopularidad)

std_age=df["housing_median_age"].std()
print('Desviacion estandar de los años: ', std_age)

filtrodeloceano= df[df["ocean_proximity"] == "ISLAND"]
print("Filro de proximidad del oceano: ", filtrodeloceano)

# vamos a crear un grafico de dispersion entre los registros de la proximidad del oceano vs los precios

plt.scatter(df["ocean_proximity"][:10], df["median_house_value"][:10])

# hay que definir a x y y
plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title('Grafico de dispersion de proximidad al oceano vs el precio')
plt.show()