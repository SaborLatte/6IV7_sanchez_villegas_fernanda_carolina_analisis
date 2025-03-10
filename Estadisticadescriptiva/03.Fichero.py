import pandas as pd

#vamos a hacer un ejemplo de catga de un archivo y aplicar el min, max, media, desviación estandar

def cotizacion(fichero):
    df= pd.read_csv(fichero, sep=';',
        decimal=',', thousands=',',
        index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean(), df.std()], 
    index=['Minimo','Maximo','Media', 'Desviación estandar'])

print(cotizacion('./Estadisticadescriptiva/cotizacion.csv'))
