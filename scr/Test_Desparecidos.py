#enconding = 'utf8'
from Desaparecidos import *

def mostar_diccionario_ordenados(dicc):
    for key in dicc:
        print (key, dicc[key])

def TestMujeresDesaparecidas (contenido):
    titulo ="NUMERO DE DESAPARECIDOS DE MUJERES EN EL AÑO"
    print(titulo + "█" * 1000, "\n")
    print(MujeresDesaparecidas(sorted(contenido)))

def TestIniciales(contenido):
    titulo = "INICIALES DE LOS NOMBRES"
    print(titulo + "█" * 1000, "\n")
    print("Iniciales que tiene relacion Tipo de sangre O+ y sexo :Male : ", Iniciales(sorted(contenido)),"\n")

def TestPromedio(contenido):
    titulo = "PORCENTAJE DE ASPECTO FISICO QUE NO FUERON DENUNCIADOS"
    print(titulo + "█" * 1000,"\n")
    print("Se han encontrado estos resultados : {}".format(porcentaje(sorted(contenido))),"\n")

def TestPERSONAS_SEGUNTIPODESANGRE(contenido):
    titulo = "LISTA DE LAS PERSONAS CON SU TIPO DE SANGRE Y ESTATURA "
    print(titulo + "█" * 1000, "\n")
    print(mostar_diccionario_ordenados(PERSONAS_SEGUNTIPODESANGRE(contenido,10)))

def TestGRAFICAS (Doc):
    print(Grafico(Doc))


Doc = abrir_csv('../data/DESAPARECIDOS_INDIA_2018_2020.csv')
#1
MujeresDesaparecidas(Doc)

#2
TestIniciales(Doc)

#3
TestPromedio(Doc)

#4
TestPERSONAS_SEGUNTIPODESANGRE(Doc)

#5
TestGRAFICAS(Doc)