import json
import csv
from ServicioYOLA import *

#Se crea un menù con las diferentes opciones
def menú():
    while True:#se crea un while true para que traiga las opciones

        print ("menú principal")
        print("Opcion 1   agregar producto " )
        print ("Opción 2   mostrar producto " )
        print ("opción 3   buscar producto " )
        print ("opción 4   actulizar producto " )
        print ("opción 5    Eliminar producto " )
        print ("opción 6     Calcular estadistica " )
        print ("opción 7  guardar y cargar .JSON  "  )
        print ("opción 8  expotatar.CSV  "  )
        print ("opción 9  guradar .CSV " )
        print ("opcion 10 salir "  )
        opciones = int(input ("Ingrese la opción que desee    "))
        #se 
        if opciones == 10:
            print ("salir del programa")
            break
        if opciones ==1:
            agregar_producto()
        if opciones == 2:
            mostrar_prodcutos(lista_inventario)
        if opciones == 3:
            buscar_producto(lista_inventario)
        if opciones == 4:
            actualizar_producto(lista_inventario)
        if opciones == 5:
            eliminar_producto(lista_inventario)
        if opciones == 6:
            calcular_estadistica(lista_inventario)
        if opciones == 7:
            guardar_json()
            cargarJSON()
            cargarJSON_en_lista()
        if opciones == 8:
            exportarCSV()
        if opciones == 9:
            cargarCSV()
        if opciones == 10:
            print("saliendo")
            break




menú() 


