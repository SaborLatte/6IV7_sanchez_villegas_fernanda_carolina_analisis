import pandas as pd
import re

df = pd.read_csv("./Estadisticadescriptiva/Afectaciones_temblor.csv", encoding="latin1")

df = df.dropna(subset=["lat", "lon"])

def limpiar_texto(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto).strip().lower()
    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i")
    texto = texto.replace("ó", "o").replace("ú", "u").replace("ñ", "n")
    texto = re.sub(r'[^\w\s]', '', texto)  
    return texto


for col in ["lugar", "tipo_daño", "delegacion"]:
    df[col] = df[col].apply(limpiar_texto)


correcciones = {
    "derrumbe barba": "derrumbe barda",
    "derrumbe parcialxccz": "derrumbe parcial",
    "contacto eden 5591056316": "",  
    "dano mayor": "daño mayor",  
}
df["tipo_daño"] = df["tipo_daño"].replace(correcciones)

df = df[
    (df["lugar"] != "") &
    (df["tipo_daño"] != "") &
    (df["delegacion"] != "")
]

df.rename(
    columns={
        "lugar": "lugar_afectado",
        "tipo_daño": "tipo_dano",
        "delegacion": "zona"
    },
    inplace=True
)

columnas_utiles = ["lugar_afectado", "tipo_dano", "zona", "lat", "lon"]
df_final = df[columnas_utiles]

df_final.to_csv("Afectaciones_temblor_limpio.csv", index=False, encoding="utf-8")

print("Archivo limpio generado: Afectaciones_temblor_limpio.csv")
