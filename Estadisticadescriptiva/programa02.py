import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel('./Estadisticadescriptiva/proyecto1.xlsx')
print(df.head())

ventas_totales= df["ventas_tot"].sum()
print("Total de Ventas: ", ventas_totales)

adeudos=df["adeudo_actual"]