import pandas as pd
from mplsoccer import Pitch
import matplotlib.pyplot as plt

# 1. Cargar los DATOS reales (el GPS de los pases)
ruta_datos = "Datos/promesas.csv"
df = pd.read_csv(ruta_datos)

# 2. Configurar la Cancha (Estilo "Scouting Profesional")
cancha = Pitch(pitch_type='statsbomb', pitch_color='#2c3e50', line_color='#ecf0f1', stripe=True)
fig, ax = cancha.draw(figsize=(12, 8))

# Le decimos: "Creá una lista nueva que SOLO tenga los datos de Echeverri"
solo_diablito = df[df['Nombre'] == 'Claudio Echeverri']

# Ahora dibujamos las flechas usando SOLO esa lista filtrada
cancha.arrows(solo_diablito.x_inicio, solo_diablito.y_inicio, 
              solo_diablito.x_fin, solo_diablito.y_fin,
              width=3, color='red', ax=ax, label='Pases de Echeverri')


# 4. Ponemos un título y lo guardamos
plt.title('Mapa de Pases Progresivos - Promesas Sub-18', fontsize=22, color='white', fontweight='bold')
plt.legend(facecolor='#2c3e50', edgecolor='white', labelcolor='white')
fig.set_facecolor('#2c3e50') # Fondo oscuro alrededor de la cancha

# Guardar en la carpeta "Graficos"
plt.savefig('Graficos/mapa_pases_profundos.png', dpi=300, bbox_inches='tight')
print("--- MAPA DE PASES GENERADO CON ÉXITO ---")
print("Revisá tu carpeta 'Graficos' para ver el informe.")