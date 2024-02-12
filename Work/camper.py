import json
def camper_menu():
    while True:   
        print("""
            *********************
            *                   *
            *MENU ADMINISTRACION*
            *                   *
            *********************
            """)
        print("*Agregar Camper    (1)")
        print("*Eliminar Camper   (2)")
        print("*Actualizar Camper (3)")
        print("*Listar Campers    (4)")
        print("*Atras             (5)")
        
        opcion = input("Ingrese la opción deseada: ")
        
        opcion = input("Ingrese la opción deseada: ")
        
        try:
            opcion = int(opcion)
            if opcion == 1:
                # Lógica para agregar Camper
                add_campers()
            elif opcion == 2:
                # Lógica para eliminar Camper
                eliminar_camper
            elif opcion == 3:
                # Lógica para actualizar Camper
                print("Actualizando Camper...")
            elif opcion == 4:
                # Lógica para listar Campers
                print("Listando Campers...")
            elif opcion == 5:
                print("Saliendo del menú de administración.")
                break
            else:
                print("Ingrese una opción válida (1-5).")
                continue  # Vuelve al inicio del bucle para pedir la opción nuevamente
        except ValueError:
            print("Error: Ingrese un número entero.")
            continue  # Vuelve al inicio del bucle para pedir la opción nuevamente
        except:
            print("Ha ocurrido un error inesperado.")
            continue  # Vuelve al inicio del bucle para pedir la opción nuevamente
        return int(opcion)




def add_campers():
    

    print("""
            **********************
            *                    *
            * REGISTRO DE CAMPER *
            *                    *
            **********************
            """)
    #Cargar el diccionario existente 
    with open('campers.json', 'r') as archivo:
        datos_guardados = json.load(archivo)
    
    #Solicitar datos 
    C_id = input('Identificación: '), 
    C_names = input('Nombres: '),
    C_lastName = input('Apellidos: '),
    C_dirección = input('direccion: '),
    C_acudiente = input('Acudiente: '),
    C_contactom = input('Celular: '),
    C_contactof = input('Fijo: '),
    C_estado = input('Estado: ','(En proceso de ingreso, Inscrito, Aprobado,Cursando, Graduado, Expulsado, Retirado)'),
    C_riesgo = input('Riesgo: ')
    #Guardar datos
    data_new = {
        "id": C_id,
        "Nombres": C_names,
        "Apellidos": C_lastName,
        "Dirección": C_dirección,
        "Acudiente": C_acudiente,
        "Contacto celular": C_contactom,
        "Contacto fijo"   : C_contactof,
        "Estado": C_estado,
        "Riesgo": C_riesgo
    }
    
    #Escribir los datos en el json 
    with open('campers.json', 'w') as outfile:
        json.dump(data_new, archivo)
        
def eliminar_camper(id_camper):
    # Paso 1: Leer campers.json
    with open('campers.json', 'r') as file:
        campers = json.load(file)

    # Buscar y eliminar el camper por su ID
    camper_eliminado = None
    for camper in campers['campers']:
        if camper['id'] == id_camper:
            camper_eliminado = camper
            campers['campers'].remove(camper)
            break

    if camper_eliminado:
        # Paso 4: Leer historial.json
        with open('historial.json', 'r') as file:
            historial = json.load(file)

        # Paso 5: Agregar el camper eliminado al historial
        historial['historial'].append(camper_eliminado)

        # Paso 6: Guardar el historial actualizado en historial.json
        with open('historial.json', 'w') as file:
            json.dump(historial, file, indent=2)

        # Paso 7: Guardar la lista de campers actualizada en campers.json
        with open('campers.json', 'w') as file:
            json.dump(campers, file, indent=2)
    else:
        print("El camper con el ID especificado no fue encontrado.")

# Uso de la función para eliminar un camper por su ID
eliminar_camper("id_a_eliminar")
    

