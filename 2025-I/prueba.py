# Mi primer programa en Python en Visual Studio Code

# Se debe en primer lugar descargar el editor Visual Studio Code (https://code.visualstudio.com/) 
# Luego instalar la extensión de Python en Visual Studio Code
# También se debe instalar Python en el sistema operativo desde Microsoft Store (Windows) 
# o desde la página oficial de Python (https://www.python.org/downloads/)
# Una vez instalado Python y Visual Studio Code, se debe crear un nuevo archivo con extensión .py
# y escribir el código en ese archivo

# Extensiones importante de Python para Visual Studio Code:
# error lens: para ver errores en el código
# excel viewer: para ver archivos excel
# image preview: para ver imágenes
# jupyter: para trabajar con notebooks de Jupyter
# live share: para compartir el código en vivo con otras personas
# live server: para ver los mapas en vivo

# A diferencia de Google Colab, en Visual Studio Code no se puede ejecutar una celda de código
# por lo que se debe ejecutar todo el script a la vez 

# El output de la ejecución aparecerá en la terminal 

# Para ejecutar el script debes dar clic al botón "Run Python File" 
# que aparece en la parte superior derecha en forma de un triángulo
# o puedes usar el atajo de teclado Ctrl + F5 (Windows) o Cmd + F5 (Mac)

# Imprimir un mensaje
# print("Hola Mundo")

# Variables
x = 5
y = 10.5
z = "Luisa"
q = True

# Imprimir variables
#print(x)
#print(y)
#print(z)

# Operamos con los valores de las variables
#print("El valor de x es: ", x)
#print("El valor de y es: ", y)
#print("El valor de z es: ", z)
#print("El valor de q es: ", q)

# print(x + y)
# print(z * x)
# print((x == y) != q)

# type(): nos dice el tipo de dato de una variable
# print(type(x))
# help(): te ofrece información sobre un objeto
#help("int")

# Listas
lista = [1, 2, 3, 4, 5]
# print(lista)

# print(lista[0])
# print(lista[1])

# print(lista[-1])

# lista.append(6)
# print(lista)

# Diccionarios
diccionario = {'nombre': 'Cristina', 'edad': 25, 'ciudad': 'Santiago'}
# print(diccionario)

# print(diccionario['nombre'])
# print(diccionario['edad'])

diccionario['edad'] = 26
# print(diccionario)

# Convertir nuestro diccionario en un DataFrame
import pandas as pd
df_1 = pd.DataFrame(diccionario, index=[0])
#print(df_1)

# agregar una nueva fila
diccionario2 = {'nombre': 'Luisa', 'edad': 27, 'ciudad': 'Valparaíso'}
df_2 = pd.concat([df_1, pd.DataFrame([diccionario2])], ignore_index=True)
#print(df_2)

# agregar latitud y longitud
df_2['latitud'] = [-33.45, -33.05]
df_2['longitud'] = [-70.65, -71.62]
#print(df_2)

# Cuando trabajamos con datos geográficos, podemos usar la librería folium para crear mapas interactivos
# Primero debemos instalar la librería folium en el terminal de Visual Studio Code
# pip install folium

# importamos la libreria folium
import folium

# Creamos un mapa centrado en Santiago
m = folium.Map(location=[-33.45, -70.65], zoom_start=10, tiles="OpenStreetMap")

# Agregamos un marcador
for _, row in df_2.iterrows():
    folium.Marker(
        location=[row["latitud"], row["longitud"]],
        popup=row["nombre"],
        tooltip=row["ciudad"]
    ).add_to(m)

# Procedemos a guardar y mostrar el mapa
#m.save("mapa.html")
# Para ver el mapa, abre el archivo mapa.html en tu navegador web
# o dale clic derecho en el archivo y selecciona "Open with Live Server" si tienes la extensión instalada



# Ahora vamos a trabajar con un archivo Excel que contiene información de f1
import pandas as pd

# abrir un archivo excel con pandas
f1 = pd.read_excel('f1_nuevo.xlsx')
#print(f1.head())

# contar los valores de una columna
escuderia = f1['Car'].value_counts()
#print(escuderia)

# Realizaremos un pie chart con matplotlib para visualizar la cantidad de autos por escudería
# Primero debemos instalar la librería matplotlib en el terminal de Visual Studio Code
# pip install matplotlib

# importamos la librería matplotlib
import matplotlib.pyplot as plt

#help(plt.pie)

# tamaño de la figura
plt.figure(figsize=(10, 5))

# colores
colors = ['pink', 'skyblue', 'yellow']

plt.pie(escuderia, labels=escuderia.index, autopct='%1.1f%%', colors=colors)
plt.title('Escuderías de F1')

# guardar la imagen
#plt.savefig('pie_chart.png')

#plt.show()

# hacer un buscador con los datos de df "f1"
# tomaremos en cuenta los url de las imágenes y url de videos de YouTube

# importaremos la librería requests para hacer peticiones HTTP
import requests
# importaremos la librería BeautifulSoup para hacer web scraping
from bs4 import BeautifulSoup

# Generaremos una solicitud al usuario para que ingrese el nombre del auto que desea buscar
#car_name = input("Ingrese el nombre del auto que desea buscar: ")
# Filtramos el DataFrame para encontrar el auto ingresado por el usuario
#f1_filtered = f1[f1['Car'].str.contains(car_name, case=False, na=False)]
# Si el auto no se encuentra en el DataFrame, mostramos un mensaje
#if f1_filtered.empty:
    #print(f"No se encontró el auto '{car_name}' en la base de datos.")
#else:
    # Si el auto se encuentra, mostramos la información del auto
    #print(f1_filtered)
    # Obtenemos la URL de la imagen del auto
    #image_url = f1_filtered['Imagen'].values[0]
    # Obtenemos la URL del video de YouTube del auto
    #video_url = f1_filtered['Video'].values[0]
    # Mostramos la URL de la imagen del auto
    #print(f"URL de la imagen del auto: {image_url}")
    # Mostramos la URL del video de YouTube del auto
    #print(f"URL del video de YouTube del auto: {video_url}")

# Usemos IPython para hacer una búsqueda en Google
#from IPython.display import display, HTML

# Usamos los url de f1 para hacer un buscador de las imagenes y cuentas de Instagram
# Generamos un buscador con el nombre de los pilotos de f1
#piloto = input("Ingrese el nombre del piloto que desea buscar: ")
# Filtramos el DataFrame para encontrar el piloto ingresado por el usuario
#f1_piloto = f1[f1['Drivers'].str.contains(piloto, case=False, na=False)]
# Si el piloto no se encuentra en el DataFrame, mostramos un mensaje
#if f1_piloto.empty:
    #print(f"No se encontró el piloto '{piloto}' en la base de datos.")
#else:
    #print(f1_piloto)
    # Obtenemos la URL de la imagen del piloto
    #image_url = f1_piloto['Imagen'].values[0]
    # Obtenemos la URL del Instagram del piloto
    #instagram_url = f1_piloto['IG'].values[0]
    # Mostramos la URL de la imagen del piloto
    #print(f"URL de la imagen del piloto: {image_url}")
    # Mostramos la URL del Instagram del piloto
    #print(f"URL del Instagram del piloto: {instagram_url}")
    # Mostramos la imagen del piloto
    #display(HTML(f'<img src="{image_url}" width="300">'))


# Es muy importante instalar las librerías primero para que todo los códigos se puedan ejecutar
# Las librerías se instalan en la terminal
# Nombre de la caperta _ ingresas cada una de los siguientes códigos esperando que se complete la instalación
# pip install pandas
# pip install matplotlib
# pip install folium
# pip install bs4
# pip install ipython 
# pip install openpyxl

    

    


