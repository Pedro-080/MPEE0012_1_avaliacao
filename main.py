import time
from selenium import webdriver
from PIL import Image
from io import BytesIO
import folium
import numpy as np

# Supondo que você tenha uma função que retorna um valor baseado na latitude e longitude
def sua_funcao(latitude, longitude):
    # Aqui você substitui com sua função real
    return np.random.rand()

# Criar um mapa centrado no Brasil
mapa = folium.Map(location=[-15.793889, -47.882778], zoom_start=4)

# Adicionar marcadores para cada ponto no Brasil
for lat in np.arange(-33.75, 5, 1.5):  # Varie de sul a norte
    for lon in np.arange(-73.5, -34, 1.5):  # Varie de oeste a leste
        valor = sua_funcao(lat, lon)
        # Define a cor com base no valor retornado pela sua função
        cor = 'red' if valor < 0.5 else 'blue'
        # Adiciona um marcador com a cor definida
        folium.CircleMarker(location=[lat, lon], radius=5, color=None, fill=True, fill_opacity=0.7, fill_color=cor).add_to(mapa)

# Salvar o mapa como uma imagem
browser = webdriver.Chrome()  # Use o driver correto para o seu navegador
mapa.save('mapa_temp.html')
browser.get('file:///path/to/mapa_temp.html')  # Substitua com o caminho para o seu arquivo HTML
time.sleep(2)  # Aguarde o carregamento da página
screenshot = browser.get_screenshot_as_png()

# Converter a captura de tela para imagem PIL
image = Image.open(BytesIO(screenshot))

# Exibir a imagem
image.show()

# Fechar o navegador
browser.quit()