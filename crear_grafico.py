import pandas as pd
import matplotlib.pyplot as plt  # Esta es la herramienta de dibujo

# 1. Cargar los datos (usamos la misma ruta que te funcionó antes)
ruta_archivo = "Datos/promesas.csv"
df = pd.read_csv(ruta_archivo)

# 2. Limpiar los datos: Convertir "15M" en el número 15.0
# Esto es necesario porque Python no puede sumar "letras".
df['Valor_Numerico'] = df['Valor_Mercado'].str.replace('M', '').astype(float)

# 3. Configurar el gráfico
plt.figure(figsize=(10, 6))  # Tamaño de la "hoja" de dibujo

# Crear un gráfico de barras (Nombres en X, Valores en Y)
plt.bar(df['Nombre'], df['Valor_Numerico'], color='skyblue', edgecolor='black')

# Añadir títulos y etiquetas para que se entienda
plt.title('Valor de Mercado de Promesas (en Millones de EUR)', fontsize=16)
plt.xlabel('Jugador', fontsize=12)
plt.ylabel('Valor (M€)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Líneas horizontales de guía

# 4. GUARDAR el gráfico en tu carpeta "Graficos"
plt.savefig('Graficos/valor_mercado_promesas.png', dpi=300, bbox_inches='tight')

print("--- GRÁFICO GENERADO CON ÉXITO ---")
print("Revisá tu carpeta 'Graficos' para ver el resultado.")