import pandas as pd

# Le decimos a Python dónde está el archivo de datos
# Cambiamos la ruta para que sea directa desde donde estás parado
ruta_archivo = "Datos/promesas.csv"

# Leer el archivo
df = pd.read_csv(ruta_archivo)

print("--- BASE DE DATOS DE SCOUTING CARGADA ---")
print(df)  # Esto muestra toda la tabla en la consola
print("-----------------------------------------")

# Un pequeño filtro: ¿Quiénes tienen 18 años?
mayores = df[df['Edad'] == 18]
print("\nJugadores con 18 años encontrados:")
print(mayores['Nombre'])