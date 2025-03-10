#vamos a crear un programa que pregunte al usuario por las ventas de un rango de años que muestre

import pandas as pd
inicio= int(input('introduce el año inicial en ventas: '))
fin= int(input('Introduce el año final de ventas: '))

ventas={}

for i in range (inicio, fin+1):
    ventas[i]= float(input('Introduce las ventas del año ' +str(i) + ':'))
    
ventas= pd.Series(ventas)
print('Ventas \n', ventas)
print('Ventas con Descuento \n', ventas*0.9)