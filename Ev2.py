import csv
import os
import datetime

respuesta = 1
columnas = ("TITULO", "AUTOR", "GENERO", "AÑO DE PUBLICACION", "FECHA DE ADQUISICIÓN", "CANTIDAD", "ISBN")
libros = []

def menu():
    print("\n BIBLIOTECA ")
    print("\n MENÚ ")
    print("1. REGISTRAR")
    print("2. CONSULTAS")
    print("3. REPORTES (SEGUN EL AÑO)")
    print("4. SALIR.")

def CSV_A_Lista():
    ruta = os.path.abspath(os.getcwd())
    archivo_trabajo = ruta + "\\datos.csv"
    if os.path.exists(archivo_trabajo):
        with open("datos.csv", "r") as archivo: 
            lector = csv.reader(archivo, delimiter=',')
            next(lector)  # Saltar la fila de encabezados
            for fila in lector:
                libros.append(tuple(fila))
        archivo.close()
    else:
        with open("datos.csv", "w", newline="") as archivo:
            registrador = csv.writer(archivo)
            registrador.writerow(columnas)
            archivo.close()

def Lista_A_CSV():
    ruta = os.path.abspath(os.getcwd())
    archivo_trabajo = ruta + "\\datos.csv"
    if os.path.exists(archivo_trabajo):
        with open("datos.csv", "w", newline="") as archivo: 
            registrador = csv.writer(archivo)
            registrador.writerow(columnas)
            registrador.writerows(libros)
        archivo.close()

CSV_A_Lista()

while True:
    menu()
    op = input("¿Qué opción deseas?: ")
    if op == "1":
        while respuesta == 1:
            registro = []
            TITULO = input("\nIngresa el titulo del libro: ")
            AUTOR = input("\nIngresa el autor del libro: ")
            GENERO = input("\nIngresa el GENERO del Libro: ")
            AÑO_DE_PUBLICACION = input("\nIngresa el año de su publicacion: ")
            FECHADEADQUISICION = input("\nIngresa la fecha de adquisicion (dd/mm/aaaa): ")
            CANTIDAD = int(input("\nIngresa la cantidad de libros que deseas adquirir: "))
            ISBN = input("\nIngresa el ISBN del libro: ")
            registro.append(TITULO)
            registro.append(AUTOR)
            registro.append(GENERO)
            registro.append(AÑO_DE_PUBLICACION)
            registro.append(FECHADEADQUISICION)
            registro.append(CANTIDAD)
            registro.append(ISBN)
            libros.append(tuple(registro))
            respuesta = int(input("\n¿Deseas capturar otro registro? \n (1.SI - 0.NO): "))
    elif op == "4":
        break

    Lista_A_CSV()
