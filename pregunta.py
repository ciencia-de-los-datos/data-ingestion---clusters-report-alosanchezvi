"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import numpy as np
import re


def ingest_data():

    #
    # Inserte su código aquí
    path=r'clusters_report.txt'
    with open(path, 'r') as f:
        content = f.read()
    lineas = content.split('\n')

    indices_numeros=[]
    for i,elemento in enumerate(lineas):
        if any(caracter.isdigit() for caracter in elemento):
            indices_numeros.append(i)

    lista_concat=[]    
    for a,b in zip(indices_numeros, indices_numeros[1:]):
        lista_concat.append(' '.join(lineas[a:b]))

    contenido=[]
    for i in (lista_concat):
        pattern = r'(\d+)\s+(\d+)\s+([\d,]+\s%\s+)\s+(.*\s*)'
        contenido.append(re.findall(pattern, i))
    contenido001=[list(cont[0]) for cont in  contenido]
    for cont in range(len(contenido001)):
        contenido001[cont][3]=re.sub('\s+', ' ', contenido001[cont][3]).strip()
        columnas=lineas[:2]
    nombre_columnas=columnas[0].split('  ')[:2]+columnas[0].split('  ')[3:-2]
    nombre_columnas[1]=nombre_columnas[1]+' palabras clave'
    nombre_columnas[2]=nombre_columnas[2]+' palabras clave'
    nombre_columnas=[i.lower().strip().replace(' ','_') for i in nombre_columnas]
    
    df=pd.DataFrame(contenido001,columns=nombre_columnas)
    #

    return df
