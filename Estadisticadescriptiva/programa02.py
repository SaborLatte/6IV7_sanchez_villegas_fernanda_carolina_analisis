import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel('./Estadisticadescriptiva/proyecto1.xlsx')
print(df.head())

ventas_totales= df["ventas_tot"].sum()
print("Total de Ventas: ", ventas_totales)

adeudos=df["adeudo_actual"]
desv_pagos = df["pagos_tot"].std()
print('Desviacion de los pagos', desv_pagos)

adeudo = df["adeudo_actual"].sum()
print('El adeudo total es:', adeudo)

Utilidad= ((df['ventas_tot'] - df['adeudo_actual']) / df['ventas_tot']) * 100
Utilidad1 = Utilidad.round(2)

print(Utilidad, ' La utilidad')

adeudo_si = df[df['B_adeudo'] == 'Con adeudo'].shape[0]  # Número de socios con adeudo
adeudo_no = df[df['B_adeudo'] == 'Sin adeudo'].shape[0]  # Número de socios sin adeudo

# Total de socios
total_socios = df.shape[0]

porcentaje_adeudo_si = (adeudo_si / total_socios) * 100
porcentaje_adeudo_no = (adeudo_no / total_socios) * 100

print(f"Socios con adeudo: {adeudo_si} ({porcentaje_adeudo_si:.2f}%)")
print(f"Socios sin adeudo: {adeudo_no} ({porcentaje_adeudo_no:.2f}%)")

df['B_mes'] = pd.to_datetime(df['B_mes'])

ventas_por_tiempo = df.groupby(df['B_mes'].dt.to_period('M'))['ventas_tot'].sum()
print(ventas_por_tiempo)


plt.figure(figsize=(10, 6))
ventas_por_tiempo.plot(kind='bar')
plt.title('Ventas Totales por Mes')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df['B_mes'] = pd.to_datetime(df['B_mes'])
desviacion_estandar = df.groupby(df['B_mes'].dt.to_period('M'))['pagos_tot'].std()

plt.figure(figsize=(10, 6))
desviacion_estandar.plot(kind='bar')

plt.title('Desviación Estándar de los Pagos Realizados por Mes')
plt.xlabel('Mes')
plt.ylabel('Desviación Estándar')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Porcentaje de utilidad del comercio
porcentaje_utilidad = ((ventas_totales - adeudo) / ventas_totales) * 100

# 7. Gráfico circular de ventas por sucursal
ventas_por_sucursal = df.groupby("suc")["ventas_tot"].sum()

plt.figure(figsize=(8, 8))
plt.pie(ventas_por_sucursal, labels=ventas_por_sucursal.index, autopct="%1.1f%%", startangle=140)
plt.title("Distribución de Ventas por Sucursal")
plt.show()

# 8. Gráfico de deudas totales por sucursal respecto del margen de utilidad
deudas_por_sucursal = df.groupby("suc")["adeudo_actual"].sum()
margen_utilidad_por_sucursal = (ventas_por_sucursal - deudas_por_sucursal) / ventas_por_sucursal * 100

fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.bar(deudas_por_sucursal.index, deudas_por_sucursal, color="#0f2b48", label="Deuda Total")
ax1.set_xlabel("Sucursal")
ax1.set_ylabel("Deuda Total", color="#0f2b48")
ax1.tick_params(axis="y", labelcolor="#0f2b48")

ax2 = ax1.twinx()
ax2.plot(margen_utilidad_por_sucursal.index, margen_utilidad_por_sucursal, marker="o", linestyle="--", color="#38b6ff", label="Margen de Utilidad")
ax2.set_ylabel("Margen de Utilidad (%)", color="#38b6ff")
ax2.tick_params(axis="y", labelcolor="#38b6ff")

plt.title("Deuda Total por Sucursal vs Margen de Utilidad")
fig.tight_layout()
plt.show()
