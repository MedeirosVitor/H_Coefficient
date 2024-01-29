import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Dados fornecidos
temperatura = np.array([-40, -30, -20, -10, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200])
prandtl = np.array([0.7436, 0.7425, 0.7408, 0.7387, 0.7362, 0.7350, 0.7336, 0.7323, 0.7309, 0.7296, 0.7282, 0.7268, 0.7255, 0.7241, 0.7228, 0.7202, 0.7177, 0.7154, 0.7132, 0.7111, 0.7073, 0.7041, 0.7014, 0.6992, 0.6974])
densidade = np.array([1.514, 1.4513, 1.394, 1.341, 1.292, 1.269, 1.246, 1.225, 1.204, 1.184, 1.164, 1.145, 1.127, 1.109, 1.092, 1.059, 1.028, 0.999, 0.972, 0.946, 0.898, 0.854, 0.815, 0.779, 0.746])
viscosidade_dinamica = np.array([0.00001527, 0.00001579, 0.0000163, 0.0000168, 0.00001729, 0.00001754, 0.00001778, 0.00001802, 0.00001825, 0.00001849, 0.00001872, 0.0000189, 0.00001918, 0.00001941, 0.00001963, 0.00002008, 0.00002052, 0.00002096, 0.00002139, 0.00002181, 0.00002264, 0.00002345, 0.0000242, 0.00002504, 0.00002577])
condutividade = np.array([0.02057, 0.02134, 0.02211, 0.02288, 0.02364, 0.02401, 0.02439, 0.02476, 0.02514, 0.02551, 0.02588, 0.02625, 0.02662, 0.02699, 0.02735, 0.02808, 0.02881, 0.02953, 0.03024, 0.03095, 0.03235, 0.03374, 0.03511, 0.03646, 0.03779])
L = 0.16

# Função para calcular o número de Reynolds
def calcular_reynolds(velocidade, temp):
    densidade_temp = np.interp(temp, temperatura, densidade)
    viscosidade_temp = np.interp(temp, temperatura, viscosidade_dinamica)
    return densidade_temp * velocidade * L / viscosidade_temp

# Gerando valores de temperatura e velocidade
velocidade = np.linspace(0.1, 10, 100)
temp, vel = np.meshgrid(temperatura, velocidade)

# Calculando Reynolds para cada combinação de temperatura e velocidade
Re = calcular_reynolds(vel, temp)

# Plotando gráfico 3D do número de Reynolds
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(temp, vel, Re, cmap='viridis')
ax.set_xlabel('Temperatura (°C)')
ax.set_ylabel('Velocidade (m/s)')
ax.set_zlabel('Número de Reynolds')
ax.set_title('Número de Reynolds em função de Temperatura e Velocidade')
plt.show()
