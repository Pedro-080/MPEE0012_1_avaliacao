import matplotlib.pyplot as plt
import numpy as np

# Definir a função para gerar as curvas
def sua_funcao(latitude, longitude):
    return np.sin(latitude) + np.cos(longitude)

# Gerar valores de latitude e longitude para o Brasil
latitudes = np.linspace(-33.75, 5, 100)
longitudes = np.linspace(-73.5, -34, 100)

# Calcular os valores da função para cada ponto
valores = sua_funcao(latitudes[:, None], longitudes)

# Plotar as curvas sobre o mapa do Brasil
plt.figure(figsize=(10, 8))
plt.contour(longitudes, latitudes, valores, levels=20)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Curvas sobre o Mapa do Brasil')
plt.grid(True)
plt.show()