import csv
import os
import datetime

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

def consulta_libro(isbn):
    for libro in libros:
        if libro[6] == isbn:
            return libro
    return None

def reporte_por_año(año):
    reporte = []
    for libro in libros:
        if libro[3] == año:
            reporte.append(libro)
    return reporte

CSV_A_Lista()

while True:
    menu()
    op = input("¿Qué opción deseas?: ")
    if op == "1":
        respuesta = 1
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
        Lista_A_CSV()
    elif op == "2":
        isbn_buscar = input("\nIngresa el ISBN del libro que deseas consultar: ")
        libro = consulta_libro(isbn_buscar)
        if libro:
            print("\nLibro encontrado:")
            print("Título:", libro[0])
            print("Autor:", libro[1])
            print("Género:", libro[2])
            print("Año de Publicación:", libro[3])
            print("Fecha de Adquisición:", libro[4])
            print("Cantidad:", libro[5])
            print("ISBN:", libro[6])
        else:
            print("\nNo se encontró un libro con ese ISBN.")
    elif op == "3":
        año_consulta = input("\nIngresa el año para generar el reporte: ")
        reporte = reporte_por_año(año_consulta)
        if reporte:
            print("\nReporte de libros publicados en el año", año_consulta)
            for libro in reporte:
                print("\nTítulo:", libro[0])
                print("Autor:", libro[1])
                print("Género:", libro[2])
                print("Año de Publicación:", libro[3])
                print("Fecha de Adquisición:", libro[4])
                print("Cantidad:", libro[5])
                print("ISBN:", libro[6])
        else:
            print("\nNo se encontraron libros publicados en el año", año_consulta)
    elif op == "4":
        print("\n¡Hasta luego!")
        break
