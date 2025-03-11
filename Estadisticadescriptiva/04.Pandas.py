import pandas as pd

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