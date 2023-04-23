
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
registros = []
AÑO_DE_PUBLICION = 

def menu():
    print("\n BIBLIOTECA ")
    print("\n MENÚ ")
    print("1. REGISTRAR")
    print("2. CONSULTAS")
    print("3. REPORTES (SEGUN EL AÑO)")
    print("4. SALIR.")
    
def buscarFECHA DE ADQUISICIÓN (AÑO DE ADQUISICIÓN_buscar):
    control=-1
    ind_retorno=-1
    for elemento in AÑO:
        control=+1
        if(elemento[:][0]==AÑO DE ADQUISICIÓN_buscar):
            ind_retorno=control
            break
    return ind_retorno
    
def buscarArt(Art_buscar):
    contador=-1
    indice_retorno=-1
    for elemento in ventas:
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
                    columnas = ("TITULO", "AUTOR", "GENERO", "AÑO DE PUBLICACION", "FECHA DE ADQUISICIÓN")

                    registros = registros + 1
                else:
                    Genero = (Genero)
                    ventas.append (["TITULO", "AUTOR", "GENERO", "AÑO DE PUBLICACION", "FECHA DE ADQUISICIÓN"])
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

CSV_A_Lista(columnas = ("GENERO", "AÑO DE PUBLICACION", "CANTIDAD", "PRECIO"))

while (True):
    menu()
    op = input("¿Qué opción deseas?: ")
    respuesta==1
    if op=="1":
        if ventas:
            while respuesta == 1:
                registro = []
                GENERO = input ("\nIngresa la GENERO del Libro: ")
                Fecha =input("\nIngresa la fecha (dd/mm/aaaa): ")
                Fecha=datetime.datetime.strptime(Fecha, "%d/%m/%Y").date()
                Cantidad = int(input("\nIngresa la cantidad de libros que deseas adquirir: "))
                Precio = int(input("\nIngresa el precio del libro: "))
                registro.append(GENERO)
                registro.append(AÑO DE PUBLICACION)
                registro.append(Cantidad)
                registro.append(AUTOR)
                ventas.append(registro)
                respuesta = int(input("\n¿Deseas capturar otro registro? \n (1.SI - 0.NO): ")) 
        else:
            while respuesta == 1:
                registro = []
                GENERO = input ("\nIngresa el genero del Libro: ")
                Fecha =input("\nIngresa la fecha (dd/mm/aaaa): ")
                Fecha=datetime.datetime.strptime(Fecha, "%d/%m/%Y").date()
                Cantidad = int(input("\nIngresa la cantidad de articulos: "))
                Precio = int(input("\nIngresa el precio del articulo: "))
                registro.append(GENERO)
                registro.append(AÑO DE PUBLICACION)
                registro.append(Cantidad)
                registro.append(AUTOR)
                ventas.append(registro)
                respuesta = int(input("\n¿Deseas capturar otro libro? \n (1.SI - 0.NO): "))
               
    elif op=="2":
        if ventas:
            GENERO_buscar =(input("\nIngresa el LIBRO que deseas consultar: "))
            indice_obtenido=buscarArt(GENERO_buscar)
            if indice_obtenido==-1:
                    print("Dicho artículo no está registrado")
            else:
                print(f"\nSU LIBRO ES: ")
                print(f"\nGENERO: {ventas[indice_obtenido][0]}")
                print(f"\nAÑO DE PUBLICACIÓN: {ventas[indice_obtenido][1]}")
                print(f"\nCantidad: {ventas[indice_obtenido][2]}")
                print(f"\nAUTOR: {ventas[indice_obtenido][3]}")
                print(f"\nSu TOTAL DE LIBROS ALQUILADOS es: ")
                resultado=int(input(Cantidad*Precio))
            
        else:
                    print("No hay registros para mostrar")
    elif op=="3":
        if Fecha:
            Fecha_buscar=datetime.datetime.strptime(input("Ingresa la fecha en la que se realizo la venta del articulo: ")).date()
            ind_obt=buscarFecha(Fecha_buscar)
            if ind_obt==-1:
                    print("Dicho articulo no está registrado")
            else:
                print(f"\ REPORTE DE VENTA")
                print(f"\SU LIBRO ES: ")
                print(f"\nGENERO: {ventas[indice_obtenido][0]}")
                print(f"\nAÑO DE PUBLICACIÓN: {ventas[indice_obtenido][1]}")
                print(f"\nCantidad: {ventas[indice_obtenido][2]}")
                print(f"\nAUTOR: {ventas[indice_obtenido][3]}")
                print(f"\nSu TOTAL DE LIBROS ALQUILADOS es: ")
                resultado=int(input(Cantidad*Precio))
    elif op=="4":
        print("SALIENDO...gracias")
        break
    else:
        print ("\n GRACIAS POR TU COMPRA")
        
