import pandas as pd
import requests

# 1. La URL de la liga que queremos (puedes probar con España o Argentina)
url = "https://fbref.com/es/comps/12/Estadisticas-de-La-Liga"

# 2. EL DISFRAZ (User-Agent)
# Esto le dice a la web que somos un navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Iniciando Operativo Camuflaje...")

try:
    # 3. Hacemos la petición con el disfraz puesto
    respuesta = requests.get(url, headers=headers)
    
    # 4. Si la respuesta es 200 (OK), le pasamos el texto a Pandas
    if respuesta.status_code == 200:
        tablas = pd.read_html(respuesta.text)
        df = tablas[0]
        
        print("\n--- ¡INFILTRACIÓN EXITOSA! ---")
        print(df[['Equipo', 'PJ', 'Ptos']].head(10))
        
        # 5. Guardamos el botín
        df.to_csv("Datos/tabla_liga_real.csv", index=False)
        print("\nDatos guardados en Datos/tabla_liga_real.csv")
    else:
        print(f"Error de infiltración: Código {respuesta.status_code}")

except Exception as e:
    print(f"Error inesperado: {e}")