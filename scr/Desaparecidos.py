#enconding = 'utf8'
import csv
from collections import namedtuple, Counter
import matplotlib.pyplot as plt
from datetime import datetime



Almacenamiento_de_datos = namedtuple('Almacenamiento_de_datos', 'Tipo_de_sangre,Nombres,Genero,Cuerpo,Distrito,'

                                                                'DENUNCIADO,Estatura,Edad,Fecha')


def abrir_csv(Doc):
    with open(Doc, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        contenido = [Almacenamiento_de_datos(Tipo_de_sangre, Nombres, Genero, Cuerpo, Distrito, DENUNCIADO,
                                             float(Estatura), int(Edad), Fecha) for
                     Tipo_de_sangre, Nombres, Genero, Cuerpo, Distrito, DENUNCIADO, Estatura, Edad, Fecha in
                     lector]
        return contenido


"""
abre el archivo csv y lo almacena en un namedtuple ('Almacenamiento_de_datos',
'Tipo_de_sangre,Nombres,Genero,Cuerpo,Distrito,'DENUNCIADO,Estatura,Edad,Cuando_Desparecio')
ENTRADA: RUTA DEL ARCHIVO CSV 
@:param contenido :es la lista de tuplas donde se guarda las columnas de los archivos csv  
SALIDA : TUPLAS PARA ITERAR CON LOS DATOS DEL FICHERO.
@:type [str,str,str,str,str,str,float,int,str,]
"""

#bloque III funcion 1
def MujeresDesaparecidas (Doc):
    Datos= [s.Fecha[6:10] for s in Doc if s.Genero == "Female"]
    Contador = Counter(Datos)
    Agrupacion = Contador.items()
    MujeresDesaparecidas = dict(Agrupacion)
    Resultado = print("\n ","MUJERES DESAPARECIDAS DUARNTE LOS AÑOS :{}".format(MujeresDesaparecidas),"\n")
    return Resultado

#Bloque III funcion 2:

def Iniciales (Doc):
    Nombres = [Nombres[0] for Tipo_de_sangre, Nombres, Genero, Cuerpo, Distrito, DENUNCIADO, Estatura, Edad, Fecha in Doc
               if Tipo_de_sangre == "O+" and Genero == "Male"]
    Contador = Counter(Nombres)
    a = max(Contador.items() , key= lambda x:x[1])
    return a

#bloque III funcion 3:

def porcentaje (Doc):
    Totaldepersonas = len([s.Nombres for s in Doc])
    DatosBool_str = [s.DENUNCIADO for s in Doc]
    Convertidor_A_Bool =[True if "true" in s else False for s in DatosBool_str]
    Datos = [s.Cuerpo for s in Doc if Convertidor_A_Bool[0] == False]
    CC = {Ca: Datos.count(Ca) * 100 / Totaldepersonas for Ca in Datos if Ca != ""}
    Contador = Counter(CC)
    Agrupador = Contador.items()
    Diccionario = dict(Agrupador)
    Resultado = ("{}".format(Diccionario))

    return Resultado
#funcion 4
def PERSONAS_SEGUNTIPODESANGRE(Doc, n ):
    dicc = dict()
    for s in Doc:
        if s.Tipo_de_sangre in dicc:
            dicc[s.Tipo_de_sangre].append(s)
        else:
            dicc[s.Tipo_de_sangre] = [s]

    for s in dicc:
        ordenado = sorted(dicc[s], key=lambda x:x.Estatura, reverse=True)[:n]
        dicc[s] = [(s.Nombres, s.Estatura) for s in ordenado]

    return dicc

def Grafico (Doc):
    a = [r.Tipo_de_sangre for r in Doc ]
    b = [r.Genero for r in Doc if r.Genero == "Male" ]
    suma = a+b
    contar = Counter(suma)

    labels = list(contar.keys())
    labels.pop(-1)
    valor = list(contar.values())
    valor.pop(-1)
    fig , ax1 = plt.subplots()
    ax1.pie(valor, labels=labels ,autopct='%1.1f%%',
            shadow=False, startangle=90 )
    ax1.axis("image")
    plt.title("PORCENTAJE DE HOMBRES SEGUN EL TIPO DE SANGRE ")
    plt.show()
    return
