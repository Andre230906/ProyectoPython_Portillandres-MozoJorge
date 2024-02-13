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
    with open("JSON/Campers.json", "r") as outfile:
        Data = json.load(outfile)


    nuevo_camper = {}
    nuevo_camper["ID"] = int(input("*Ingrese el ID (numero de documento) del camper que deseas agregar: "))
    nuevo_camper["nombres"] = input("*Ingrese los nombres del camper                                  : ")
    nuevo_camper["apellido"] = input("*Ingresa los apellidos del camper                               : ")
    nuevo_camper["ciudad"] = input("*Ingrese la ciudad del  camper que deseas agregar                 : ")
    nuevo_camper["Direccion"] = input("*Ingrese la Dirección del camper que deseas agregar            : ")
    nuevo_camper["Acudiente"] = input("*Ingrese El nombre del acudiente del nuevo camper              : ")
    nuevo_camper["N_celular"] = input("*Ingrese el numero de celular del nuevo camper                 : ")
    nuevo_camper["N_fijo"] = input("*Ingrese el numero de teléfono fijo del nuevo camper              : ")
    nuevo_camper["Estado"] = "Inscrito"

    Data["Campers"].append(nuevo_camper)

    with open("JSON/Campers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)
        
        


def actualizar_datos_camper():
    with open("JSON/Campers.json", "r+") as editacion:
        Data = json.load(editacion)
        campers = Data["Campers"]
        ID_camper = int(input("Ingresa el id del Camper que quieras actualizar: "))
        for camper in campers:
            if camper["ID"] == ID_camper:
                # Solicitar los nuevos datos al usuario
                camper["ID"] = input("Ingresa el nuevo numero de documento: ")
                camper["nombres"] = input("Ingresa los nuevos nombres: ")
                camper["apellido"] = input("Ingresa los nuevos apellidos: ")
                camper["ciudad"] = input("Ingresa la nueva ciudad: ")
                camper["Direccion"] = input("Ingrese la nueva direccion: ")
                camper["Acudiente"] = input("Ingresa el nuevo nombre del acudiente: ")
                camper["N_celular"] = input("Ingresa el nuevo numero de celular: ")
                camper["N_fijo"] = input("Ingresa el nuevo numero de teléfono fijo: ")
                camper["Estado"] = input("Ingresa el nuevo estado del camper: ")

                
                # Volver al principio del archivo y escribir los datos actualizados
                editacion.seek(0)
                json.dump(Data, editacion, indent=4)
                editacion.truncate()
                print("Los datos del camper han sido actualizados exitosamente.")
                return
        print("No se encontró un camper con el ID proporcionado.")

def eliminar_camper(identificacion):
    file_path = 'JSON/Campers.json'
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0: #Verifica si la ruta existe y si su tamaño es mayor que 0 para saber que no esta vacio
        with open(file_path, 'r') as file: #modo lectur
            campers = json.load(file) #
        
        if isinstance(campers, dict): #verifica si es un dict
            if campers.get("ID") == identificacion:
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
            a = int(input("Ingresa (1) para continuar: "))
            if a == 1:
                for camper in datos['Campers']:
                    print("ID: ", camper['ID']) # Agrega una línea en blanco entre cada camper
                    print("Nombres: ", camper['nombres'])
                    print("Apellido:", camper['apellido'])
                    print("Ciudad:", camper['ciudad'])
                    print("Direccion:", camper['Direccion'])
                    print("Acudiente:", camper['Acudiente'])
                    print("N_celular:", camper['N_celular'])
                    print("N_fijo:", camper['N_fijo'])
                    print("Estado:", camper['Estado'])
                    print("")

                  # print(f"ID: {camper['ID']}, nombres: {camper['nombres']}, Apellido: {camper['apellido']}, ciudad: {camper['ciudad']}, direccion: {camper['Direccion']}, Acudiente: {camper['Acudiente']}, Ncelular: {camper['N_celular']}, Nfijo: {camper['N_fijo']}, Estado: {camper['Estado']}")
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