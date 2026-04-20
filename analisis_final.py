import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargamos el CSV que bajaste de Google Sheets
ruta = "Datos/tabla_manual.csv.csv"

try:
    # Leemos el archivo
    df = pd.read_csv(ruta)

    # 2. Limpieza rápida (A veces FBref trae filas de encabezados repetidos)
    # Nos quedamos solo con las columnas que nos interesan
    # IMPORTANTE: Revisá cómo se llaman en tu archivo, suelen ser 'Squad' y 'Pts'
    print("Columnas encontradas:", df.columns.tolist())
    
    # Supongamos que se llaman 'Squad' y 'Pts' (o 'Equipo' y 'Ptos')
    # Ajustá estos nombres según lo que leas arriba
    col_equipo = 'Squad' 
    col_puntos = 'Pts'

    # 3. ¡Hacemos un gráfico de barras real!
    plt.figure(figsize=(12, 6))
    # Buscá esta línea en tu código y reemplazala:
    plt.bar(df[col_equipo].head(10), df[col_puntos].head(10), color='#034694', edgecolor='white')
    plt.grid(axis='y', linestyle='--', alpha=0.7) # Agrega líneas de guía horizontales
    
    plt.title('Top 10 Equipos por Puntos', fontsize=16)
    plt.xlabel('Equipo')
    plt.ylabel('Puntos')
    plt.xticks(rotation=45) # Rotamos los nombres para que se lean bien
    
    # Guardamos el gráfico
    plt.tight_layout()
    plt.savefig('Graficos/ranking_puntos.png')
    print("\n--- ¡GRÁFICO GENERADO! ---")
    print("Revisá tu carpeta 'Graficos/ranking_puntos.png'")

except Exception as e:
    print(f"Error: {e}")
    print("Fijate si los nombres de las columnas en el print de arriba coinciden con el código.")