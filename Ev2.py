
import csv
import os
import datetime


respuesta = 1
CANTIDAD = 0
GENERO = ""
AUTOR = ""
resultado = 0
TITULO = ""
columnas = ("TITULO", "AUTOR", "GENERO", "AÑO DE PUBLICACION", "FECHA DE ADQUISICIÓN", "CANTIDAD", "ISBN")
ISBN = []
registro = []
AÑO_DE_PUBLICACION = datetime.datetime.strptime("AÑO_DE_PUBLICACION", "%d/%m/%Y").date()
FECHADEADQUISICIÓN = datetime.datetime.strptime("FECHADEADQUISICION", "%d/%m/%Y").date()

def menu():
    print("\n BIBLIOTECA ")
    print("\n MENÚ ")
    print("1. REGISTRAR")
    print("2. CONSULTAS")
    print("3. REPORTES (SEGUN EL AÑO)")
    print("4. SALIR.")
    
def buscarAÑO_DE_PUBLICACION (AÑO_DE_PUBLICACION_buscar):
    control=-1
    ind_retorno=-1
    for elemento in AÑO_DE_PUBLICACION:
        control=+1
        if(elemento[:][0]==AÑO_DE_PUBLICACION_buscar):
            ind_retorno=control
            break
    return ind_retorno
    
def buscarArt(Art_buscar):
    contador=-1
    indice_retorno=-1
    for elemento in ISBN:
        contador+=1
        if (elemento[:][0] == Art_buscar):
            indice_retorno=contador
            break
    return indice_retorno

def CSV_A_Lista(columnas = list()):
    ruta = os.path.abspath(os.getcwd())
    archivo_trabajo=ruta+"\\datos.csv"
    if os.path.exists(archivo_trabajo):
        with open("datos.csv", "r") as archivo: 
            lector = csv.reader(archivo, delimiter=',')
            registros = 1
            for GENERO, Cantidad, AUTOR in lector:
                if registros == 0:
                    columnas = ("TITULO", "AUTOR", "GENERO", "AÑO DE PUBLICACION", "FECHA DE ADQUISICIÓN", "CANTIDAD", "ISBN")

                    registros = registros + 1
                else:
                    Genero = (GENERO)
                    ventas.append (["TITULO", "AUTOR", "GENERO", "AÑO DE PUBLICACION", "FECHA DE ADQUISICIÓN", "CANTIDAD", "ISBN"])
        archivo.close()
    else:
        with open("datos.csv", "w", newline="") as archivo:
            registrador = csv.writer(archivo)
            registrador.writerow(columnas)
            archivo.close()

def Lista_A_CSV():
    ruta = os.path.abspath(os.getcwd())
    archivo_trabajo=ruta+"\\datos.csv"
    if os.path.exists(archivo_trabajo):
        with open("datos.csv", "w", newline="") as archivo: 
            registrador = csv.writer(archivo)
            registrador.writerow(columnas)
            registrador.writerows()
        archivo.close()

CSV_A_Lista(columnas = ("TITULO", "AUTOR", "GENERO", "AÑO DE PUBLICACION", "FECHA DE ADQUISICIÓN", "CANTIDAD", "ISBN"))

while (True):
    menu()
    op = input("¿Qué opción deseas?: ")
    respuesta==1
    if op=="1":
        if ISBN:
            while respuesta == 1:
                registro = []
                TITULO = input("\nIngresa el titulo del libro: ")
                AUTOR = input("\nIngresa el autor del libro: ")
                GENERO = input("\nIngresa el GENERO del Libro: ")
                AÑO_DE_PUBLICACION = input("\nIngresa el año de su publicacion: ")
                AÑO_DE_PUBLICACION = datetime.datetime.strptime(Fecha, "%d/%m/%Y").date()
                FECHADEADQUISICION = input("\nIngresa la fecha de adquisicion (dd/mm/aaaa): ")
                FECHADEADQUISICION = datetime.datetime.strptime(Fecha, "%d/%m/%Y").date()
                CANTIDAD = int(input("\nIngresa la cantidad de libros que deseas adquirir: "))
                ISBN = int(input("\nIngresa el ISBN del libro: "))
                registro.append(TITULO)
                registro.append(AUTOR)
                registro.append(GENERO)
                registro.append(AÑO_DE_PUBLICACION)
                registro.append(FECHA_DE_ADQUISICION)
                registro.append(CANTIDAD)
                registro.append(ISBN)
                ventas.append(registro)
                respuesta = int(input("\n¿Deseas capturar otro registro? \n (1.SI - 0.NO): ")) 
        else:
            while respuesta == 1:
                registro = []
                TITULO = input("\nIngresa el titulo del libro: ")
                AUTOR = input("\nIngresa el autor del libro: ")
                GENERO = input("\nIngresa el GENERO del Libro: ")
                AÑO_DE_PUBLICACION = input("\nIngresa el año de su publicacion: ")
                AÑO_DE_PUBLICACION = datetime.datetime.strptime(Fecha, "%d/%m/%Y").date()
                FECHADEADQUISICION = input("\nIngresa la fecha de adquisicion (dd/mm/aaaa): ")
                FECHADEADQUISICION = datetime.datetime.strptime(Fecha, "%d/%m/%Y").date()
                CANTIDAD = int(input("\nIngresa la cantidad de libros que deseas adquirir: "))
                ISBN = int(input("\nIngresa el ISBN del libro: "))
                registro.append(TITULO)
                registro.append(AUTOR)
                registro.append(GENERO)
                registro.append(AÑO_DE_PUBLICACION)
                registro.append(FECHA_DE_ADQUISICION)
                registro.append(CANTIDAD)
                registro.append(ISBN)
                ventas.append(registro)
                respuesta = int(input("\n¿Deseas capturar otro registro? \n (1.SI - 0.NO): ")) 
               
    elif op=="2":
        if ISBN:
            GENERO_buscar =(input("\nIngresa el LIBRO que deseas consultar: "))
            indice_obtenido=buscarArt(GENERO_buscar)
            if indice_obtenido==-1:
                    print("Dicho artículo no está registrado")
            else:
                print(f"\nSU LIBRO ES: ")
                print(f"\nGENERO: {ISBN[indice_obtenido][0]}")
                print(f"\nAÑO DE PUBLICACIÓN: {ISBN[indice_obtenido][1]}")
                print(f"\nCantidad: {ISBN[indice_obtenido][2]}")
                print(f"\nAUTOR: {ISBN[indice_obtenido][3]}")
                print(f"\nSu TOTAL DE LIBROS ALQUILADOS es: ")
                resultado=int(input(CANTIDAD))
            
        else:
                    print("No hay registros para mostrar")
    elif op=="3":
        if FECHADEADQUISICION:
            FECHADEADQUISICION_buscar = datetime.datetime.strptime(input("Ingresa la fecha en la que se realizo la venta del articulo: ")).date()
            ind_obt = buscarFECHADEADQUISICION (FECHADEADQUISICION_buscar)
            if ind_obt==-1:
                    print("Dicho libro aún no está adquirido")
            else:
                print(f"\ REPORTE DE VENTA")
                print(f"\SU LIBRO ES: ")
                print(f"\nGENERO: {CANTIDAD[indice_obtenido][0]}")
                print(f"\nAÑO DE PUBLICACION: {CANTIDAD[indice_obtenido][1]}")
                print(f"\nCantidad: {CANTIDAD[indice_obtenido][2]}")
                print(f"\nAUTOR: {CANTIDAD[indice_obtenido][3]}")
                print(f"\nSu TOTAL DE LIBROS ALQUILADOS es: ")
                resultado=int(input(CANTIDAD))
    elif op=="4":
        print("SALIENDO...gracias")
        break
    else:
        print ("\n GRACIAS POR TU COMPRA")
        
