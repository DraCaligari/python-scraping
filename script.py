import requests
from bs4 import BeautifulSoup

url = 'https://dockerlabs.es'
respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    maquinas = soup.find_all('div', onclick=True)
    conteo_maquinas = 1

    autores = set()

    for maquina in maquinas:
        onclick_text = maquina['onclick']
        autor = onclick_text.split("'")[7]
        autores.add(autor)
        nombre_maquina = onclick_text.split("'")[1]
        conteo_maquinas += 1


    for maquina in maquinas:
        onclick_text = maquina['onclick']
        nombre = onclick_text.split("'")[1]
        dificultad = onclick_text.split("'")[3]
        autor = onclick_text.split("'")[7]

        print(nombre, dificultad, autor)


else:
    print(f'Error al obtener la respuesta {respuesta.status_code}')
