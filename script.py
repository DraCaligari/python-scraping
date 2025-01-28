import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

init(autoreset=True)

banner = f"""
{Fore.CYAN}
  _____                          _       
 / ____|                        (_)      
| (___  _ __ ___ _ __   ___ _ __ _ _ __  
 \___ \| '__/ _ \ '_ \ / _ \ '__| | '_ \ 
 ____) | | |  __/ |_) |  __/ |  | | |_) |
|_____/|_|  \___| .__/ \___|_|  |_| .__/ 
                | |               | |    
                |_|               |_|    
{Style.RESET_ALL}
"""

print(banner)

url = 'https://dockerlabs.es'
respuesta = requests.get(url)

if respuesta.status_code == 200:
    respuesta.encoding = 'utf-8'
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    maquinas = soup.find_all('div', onclick=True)

    for maquina in maquinas:
        onclick_text = maquina['onclick']
        nombre = onclick_text.split("'")[1]
        dificultad = onclick_text.split("'")[3]
        autor = onclick_text.split("'")[7]

        peso_element = maquina.find('span', class_='size')
        if peso_element:
            peso = peso_element.get_text(strip=True)
        else:
            peso = "No disponible"

        enlace_descarga_element = maquina.find('button', class_='download')
        if enlace_descarga_element:
            enlace_descarga = enlace_descarga_element['onclick']
            enlace_descarga = enlace_descarga.split("'")[1]
        else:
            enlace_descarga = "No disponible"

        print(f"{Fore.CYAN}Nombre:{Style.RESET_ALL} {Fore.YELLOW}{nombre}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Dificultad:{Style.RESET_ALL} {Fore.MAGENTA}{dificultad}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Autor:{Style.RESET_ALL} {Fore.RED}{autor}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Peso:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}{peso}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Descargar:{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}{enlace_descarga}{Style.RESET_ALL}")
        print("-" * 40)

else:
    print(f'Error al obtener la respuesta {respuesta.status_code}')