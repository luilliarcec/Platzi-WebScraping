import requests
from bs4 import BeautifulSoup
import urllib.request


def run():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))  # Se obtiene la página
        soup = BeautifulSoup(response.content, 'html.parser')  # Se obtiene el contenido a parsear (Html en este caso)
        image_container = soup.find(id='comic')  # Se obtiene con el id el contenedor del tag img

        image_url = image_container.find('img')['src']  # Se obtiene el tag img y su atributo src
        image_name = image_url.split('/')[-1]  # Obtenemos el nmbre de la imagen de la url separada por el ultimo /
        urllib.request.urlretrieve('https:{}'.format(image_url), image_name)  # Se guarda la imagen


if __name__ == '__main__':
    run()
