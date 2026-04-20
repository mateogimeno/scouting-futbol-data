import pandas as pd

# 1. URL directa de la tabla de España en FBref
url = "https://fbref.com/es/comps/12/Estadisticas-de-La-Liga"

print("Intentando leer la tabla directamente desde la web...")

try:
    # 2. Le pedimos a Pandas que busque todas las tablas de esa página
    tablas = pd.read_html(url)
    
    # La primera tabla (index 0) suele ser la de posiciones
    df = tablas[0]
    
    print("\n--- ¡DATOS OBTENIDOS DIRECTAMENTE! ---")
    # Limpiamos un poco los nombres de las columnas si vienen raros
    print(df[['Equipo', 'PJ', 'PG', 'PE', 'PP', 'Ptos']].head(10))

    # 3. Guardar en la carpeta
    df.to_csv("Datos/tabla_espana_directa.csv", index=False)
    print("\n¡Listo! Archivo guardado en Datos/tabla_espana_directa.csv")

except Exception as e:
    print(f"No se pudo leer la web: {e}")
    print("Probablemente FBref bloqueó el acceso temporal. ¡No te preocupes, mañana intentamos con otro método!")