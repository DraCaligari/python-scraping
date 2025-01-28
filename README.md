# Web Scraper Script

Este script utiliza `requests`, `BeautifulSoup` y `colorama` para extraer información de una página web específica y presentarla en la terminal con un formato claro y colores llamativos.

## Descripción

El script realiza las siguientes tareas:

1. Muestra un banner decorativo en la terminal al iniciar.
2. Envía una solicitud HTTP a la página web `https://dockerlabs.es`.
3. Extrae información de las máquinas disponibles en la página, incluyendo:
   - **Nombre**
   - **Dificultad**
   - **Autor**
   - **Peso** (si está disponible)
   - **Enlace de descarga** (si está disponible)
4. Presenta los datos extraídos en la terminal, organizados y con colores para facilitar la lectura.

---

## Requisitos

Para ejecutar este script, asegúrate de tener instalados los siguientes paquetes de Python:

- `requests`
- `beautifulsoup4`
- `colorama`

Puedes instalarlos ejecutando el siguiente comando:

```bash
pip install requests beautifulsoup4 colorama
```
## Uso

Sigue estos pasos para ejecutar el script:

1. Clona este repositorio o descarga el archivo del script en tu máquina local.
   
   ```bash
   git clone https://github.com/DraCaligari/python-scraping.git
    ```

2. Asegúrate de tener Python 3 instalado. Puedes verificar tu versión de Python con el siguiente comando:

   ```bash
   python --version
   ```

3. Instala las dependencias necesarias utilizando pip:

   ```bash
   pip install requests beautifulsoup4 colorama
   ```

4. Ejecuta el script:

   ```bash
   python script.py
   ```

5. Si la página web está disponible y su estructura no ha cambiado, el script mostrará los datos extraídos en la terminal.

6. Observa la salida en la terminal, donde se listarán las máquinas con los siguientes datos:

   - Nombre
   - Dificultad
   - Autor
   - Peso (si está disponible)
   - Enlace de descarga (si está disponible)

   Ejemplo de salida:
   ```bash
     _____                          _       
    / ____|                        (_)      
   | (___  _ __ ___ _ __   ___ _ __ _ _ __  
    \___ \| '__/ _ \ '_ \ / _ \ '__| | '_ \ 
    ____) | | |  __/ |_) |  __/ |  | | |_) |
   |_____/|_|  \___| .__/ \___|_|  |_| .__/ 
                   | |               | |    
                   |_|               |_|    
   
   Nombre: Maquina1
   Dificultad: Media
   Autor: Usuario1
   Peso: 2.5 GB
   Descargar: https://dockerlabs.es/descargar/maquina1
   ----------------------------------------
   Nombre: Maquina2
   Dificultad: Alta
   Autor: Usuario2
   Peso: 3.0 GB
   Descargar: https://dockerlabs.es/descargar/maquina2
   ----------------------------------------
   ```
   
## Notas
- Este script está diseñado específicamente para la página https://dockerlabs.es. Si la estructura del HTML cambia, es posible que necesites actualizar el código para adaptarlo.
- Asegúrate de tener una conexión a Internet activa para acceder a la página web.
- Si encuentras errores relacionados con el código de estado HTTP o elementos no encontrados, verifica que la página esté disponible y que no haya cambios en su diseño.

## Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.