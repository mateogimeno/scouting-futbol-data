import ScraperFC
import pandas as pd

# 1. Inicializar el extractor para la página FBref
# FBref es como la biblia de los datos gratuitos de fútbol
scraper = ScraperFC.FBref()

print("Buscando datos en internet... (esto puede tardar un poquito)")

# 2. Pedir la tabla de posiciones de la liga argentina 2024 o 2025
# (Cambiamos el año según la temporada que queramos)
tabla = scraper.get_season_stats("Argentina", "2024", "Standard Stats")

# 3. Mostrar los primeros 5 equipos para ver si funcionó
print("--- DATOS EXTRAÍDOS CON ÉXITO ---")
print(tabla[['Squad', 'MP', 'W', 'D', 'L', 'Pts']].head(10)) 

# 4. GUARDARLO en tu carpeta de Datos para usarlo después
tabla.to_csv("Datos/tabla_argentina_real.csv", index=False)

print("\nArchivo 'tabla_argentina_real.csv' guardado en tu carpeta Datos.")

# Importante: Siempre cerrar el scraper al terminar
scraper.close()