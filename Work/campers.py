import json
import os
def limpiar_terminal():
    if os.name=="nt":
        os.system("clear")
    else:
        os.system("clear")



def add_campers():
    limpiar_terminal()
    print("""
            **********************
            *                    *
            * REGISTRO DE CAMPER *
            *                    *
            **********************
            """)
    # Cargar la lista de campers existente
    file_path = 'JSON/Campers.json'
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r') as archivo:
            campers_existente = json.load(archivo)
    else:
        campers_existente = []

    while True:
        # Solicitar datos
        C_id = input('Identificación: ')
        C_names = input('Nombres: ')
        C_lastName = input('Apellidos: ')
        C_dirección = input('Dirección: ')
        C_acudiente = input('Acudiente: ')
        C_contactom = input('Celular: ')
        C_contactof = input('Fijo: ')
        C_estado = input('Estado: ')
        C_riesgo = input('Riesgo: ')

        # Añadir los nuevos datos a la lista de campers existente
        nuevo_camper = {
            "id": C_id,
            "Nombres": C_names,
            "Apellidos": C_lastName,
            "Dirección": C_dirección,
            "Acudiente": C_acudiente,
            "Contacto celular": C_contactom,
            "Contacto fijo": C_contactof,
            "Estado": C_estado,
            "Riesgo": C_riesgo
        }
        campers_existente.append(nuevo_camper)

        respuesta = input("¿Desea añadir otro camper? (s/n): ")
        if respuesta.lower() != "s":
            break

    # Escribir la lista actualizada en el JSON
    with open(file_path, 'w') as archivo:
        json.dump(campers_existente, archivo, indent=4)


def actualizar_datos_camper(id_camper, datos_actualizados):
    print("""
            **********************
            *                    *
            * ACTUALIZAR  CAMPER *
            *                    *
            **********************
            """)
    
    # Abre el archivo JSON en modo lectura y escritura
    with open('JSON/Campers.json', 'r+') as archivo:
        # Carga los datos del archivo
        datos = json.load(archivo)
        
        # Busca al camper por su ID
        for index, camper in enumerate(datos['campers']):
            if camper['id'] == id_camper:
                # Actualiza los datos del camper
                datos['campers'][index].update(datos_actualizados)
                
                # Vuelve al principio del archivo
                archivo.seek(0)
                
                # Escribe los datos actualizados en el archivo
                json.dump(datos, archivo, indent=4)
                
                # Trunca el archivo para eliminar cualquier contenido previo
                archivo.truncate()
                return True  # Retorna True para indicar que la actualización fue exitosa
    return False  # Retorna False si no se encontró el camper con el ID proporcionado

def eliminar_camper(identificacion):
    file_path = 'JSON/Campers.json'
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r') as file:
            campers = json.load(file)
        
        if isinstance(campers, dict):
            if campers.get("id") == identificacion:
                # Si el ID coincide, se elimina el camper
                with open(file_path, 'w') as file:
                    file.write("{}")  # Escribir un JSON vacío para eliminar el contenido
                print(f"Camper con identificación {identificacion} eliminado correctamente.")
            else:
                print(f"No se encontró ningún camper con la identificación {identificacion}.")
        else:
            print("El archivo de campers no contiene un objeto JSON en el formato esperado.")
    else:
        print("El archivo de campers está vacío o no existe.")

def imprimir_todos_los_campers():
    print("""
            **********************
            *                    *
            *  IMPRIMIR CAMPERS  *
            *                    *
            **********************
            """)
    try:
        with open('JSON/Campers.json', 'r') as archivo:
            # Carga los datos del archivo
            datos = json.load(archivo)
            a=int(input("Ingresa (1) para continuar: "))
            if a==1:
                for camper in datos['campers']:
                    print(f"ID: {camper['id']}, Nombres: {camper['nombres']}, Apellidos: {camper['apellidos']}")
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")

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
        
        opciones_dict = {
            1: add_campers,
            2: lambda: eliminar_camper(input("Ingrese el ID del camper a eliminar: ")),
            3: lambda: actualizar_datos_camper(input("Ingrese el ID del camper a actualizar: "), 
                                       eval(input("Ingrese los datos actualizados del camper en formato de diccionario: "))),
            4: imprimir_todos_los_campers,
            5: lambda: print("Saliendo del menú de administración.")
        }
        
        if opcion.isdigit() and int(opcion) in range(1,  6):
            opciones_dict[int(opcion)]()
        elif opcion.lower() == '5':
            print("Saliendo del menú de administración.")
            break
        else:
            print("Ingrese una opción válida (1-5).")
            continue

camper_menu()