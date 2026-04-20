import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargamos el CSV
ruta = "Datos/efectividad_punteria.csv"

try:
    # Leemos el archivo completo
    df = pd.read_csv(ruta)

    # --- MÉTODO INFALIBLE: POSICIÓN DE COLUMNAS ---
    # Según la lista, las posiciones son:
    # Columna 1 (index 1) -> Jugador
    # Columna 8 (index 8) -> Goles
    # Columna 10 (index 10) -> Remates al arco (SoT)

    df['Jugador'] = df.iloc[:, 1]
    df['Goles'] = pd.to_numeric(df.iloc[:, 8], errors='coerce').fillna(0)
    df['SoT'] = pd.to_numeric(df.iloc[:, 10], errors='coerce').fillna(0)

    # 2. Limpieza de filas "basura" (encabezados que se cuelan)
    # Filtramos para que el nombre no sea 'Player' ni esté vacío
    df = df[df['Jugador'].notna()]
    df = df[df['Jugador'] != 'Player'].copy()

    # 3. Solo jugadores que patearon al arco al menos una vez
    df = df[df['SoT'] > 0].copy()

    # 4. Cálculo de Efectividad
    df['Efectividad'] = df['Goles'] / df['SoT']

    # Ordenamos y agarramos el Top 10
    df_top = df.sort_values(by='Efectividad', ascending=False).head(10)

    # 5. Gráfico Final
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    
    # Color verde flúor tipo "Data Scout"
    plt.barh(df_top['Jugador'], df_top['Efectividad'], color='#00FF41')
    
    plt.title('Top 10: Efectividad de Remate (Goles / Tiros al arco)', color='white', pad=20)
    plt.xlabel('Efectividad (G/SoT)')
    plt.gca().invert_yaxis()
    
    plt.tight_layout()
    plt.savefig('Graficos/efectividad_final_v2.png')
    
    print("\n--- ¡ANÁLISIS COMPLETADO EXITOSAMENTE! ---")
    print(df_top[['Jugador', 'Goles', 'SoT', 'Efectividad']].head(5))

except Exception as e:
    print(f"Ups, algo falló: {e}")