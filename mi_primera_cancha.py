from mplsoccer import Pitch
import matplotlib.pyplot as plt

# 1. Creamos la "hoja" con la cancha dibujada
# 'statsbomb' es el tipo de medidas que usa la cancha (0 a 120 de largo)
cancha = Pitch(pitch_color='#aabb97', line_color='white')
fig, ax = cancha.draw(figsize=(10, 7))

# 2. Dibujamos un "Tiro" (un punto)
# x = 105 (cerca del arco rival), y = 40 (centro de la cancha)
cancha.scatter(105, 40, s=500, c='red', edgecolors='black', ax=ax, label='Gol de Messi')

# 3. Ponemos un título
plt.title('Mi primer mapa de tiros con Python FC', fontsize=20)
plt.legend()

# 4. Lo guardamos en tu carpeta de Gráficos
plt.savefig('Graficos/mi_primera_cancha.png')
print("¡Cancha generada en la carpeta Graficos!")