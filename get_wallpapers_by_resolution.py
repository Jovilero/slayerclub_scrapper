#descargar todos los wallpapers de doom del slayersclub
#web scrapper:
import requests
from bs4 import BeautifulSoup
import os
import re
import shutil
import socket
import zipfile

# URL de la página de fondos de pantalla
URL = "https://slayersclub.bethesda.net/"

# Directorio base para almacenar las imágenes
base_dir = 'fondos_de_pantalla'

# Función para crear un directorio si no existe
def create_dir(directory):
    # print((directory))
    if not os.path.exists(directory):
        print(directory)
        os.makedirs(directory)
    else:
        print(fr'Directory {directory} already exists.')
        
# Función para descargar una imagen
def download_image(image_url, path):
    print(image_url)
    print(path)
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(path, 'wb+') as file:
        # print(response.content)
            file.write(response.content)
        print(f'Descargado: {path}')
    else:
        print(f'Error al descargar {image_url}')

# Obtener el contenido de la página web
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')


def zip_files(tempFolder, baseFolder,zip_filename='', files_to_zip=''):
    # Name of the zip file you want to create
    zip_filename = f"{baseFolder}/{zip_filename}"
    if tempFolder[-1]!='/':
        tempFolder+='/'
    # Create a zip file
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        for file in files_to_zip:
            # Add each file to the zip archive
            try:
                zipf.write(f"{tempFolder}{file}", arcname=f"{file}")
            except:
                print.writeline(baseFolder, fr'Unable to zip {file} from {tempFolder}')

    print.writeline(baseFolder,f"{tempFolder}/{file}")

# Encontrar los elementos que contienen los enlaces de las imágenes
wallpaper_sections = soup.find_all(class_='w-full font-heading text-3xl')
# print(wallpaper_sections)
# Procesar cada sección de fondo de pantalla
for section in wallpaper_sections:
    # Obtener el nombre del fondo de pantalla para el nombre de la carpeta
    
    # print(section)
    for each in str(section).split('"'):
        if each.startswith('/') and each.endswith('.jpg'):
            picture_name_and_resolution=each.split('/')[-1]
            name, resolution=picture_name_and_resolution.split('Wallpaper')
            create_dir(name)
            path=fr'{name}/{name}{resolution}'
            download_image(fr'{URL}{each[1:]}',path)

    # zip_files(name,name)
    print("\n")

 

print('Done.')

