import json
import os
def limpiar_terminal():
    if os.name=="nt":
        os.system("cls")
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
    
    edad = int(input("Ingrese la edad del camper: "))
    if edad < 16 or edad > 28:
        print("Lo siento, el camper debe tener entre 16 y 28 años para ser registrado.")
        return  # Volver al inicio del menú
    
    with open("JSON/Campers.json", "r") as outfile:
        Data = json.load(outfile)

    newc = {}
    newc["ID"] = int(input("*Ingrese el ID (numero de documento) del camper que deseas agregar: "))
    newc["nombres"] = input("*Ingrese los nombres del camper                                   : ")
    newc["apellido"] = input("*Ingresa los apellidos del camper                                 : ")
    newc["ciudad"] = input("*Ingrese la ciudad del  camper que deseas agregar                 : ")
    newc["Direccion"] = input("*Ingrese la Dirección del camper que deseas agregar               : ")
    newc["Acudiente"] = input("*Ingrese El nombre del acudiente del nuevo camper                 : ")
    newc["N_celular"] = input("*Ingrese el numero de celular del nuevo camper                    : ")
    newc["N_fijo"] = input("*Ingrese el numero de teléfono fijo del nuevo camper              : ")
    newc["Estado"] = "inscrito"
    newc["Nota"] = "1"
    newc["Ruta General"] = "a"
    newc["Ruta Especifica"] = "a"
    newc["Salon"] = "a"
    newc["Grupo"] = "a"



    Data["Campers"].append(newc)

    with open("JSON/Campers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)
      
def actualizar_datos_camper():
    limpiar_terminal()
    print("""
            **********************
            *                    *
            *ACTUALIZAR  CAMPERS *
            *                    *
            **********************
            """)
    edit = open("JSON/Campers.json")
    Data = json.load(edit)
    campers = Data["Campers"]
    IDi_camper = int(input("Ingresa el id del Camper que quieras actualizar: "))
    for camper in campers:
        if camper["ID"] == IDi_camper:
            
            nombres = input("Ingresa los nuevos nombres: ") 
            apellidos = input("Ingresa los nuevos apellidos: ")
            ciudad = input("Ingresa la ciudad a cambiar: ")
            Direccion = input("Ingrese la direccion a cambiar: ")
            Acudiente = input("Ingresa el acudiente a cambiar : ")
            N_celular = input("Ingresa el nuevo numero de celular: ")
            N_fijo = input("Ingresa el nuevo numero de teléfono fijo: ")
            
            camper["nombres"] = nombres
            camper["apellido"] = apellidos
            camper["ciudad"] = ciudad
            camper["Direccion"] = Direccion
            camper["Acudiente"] = Acudiente
            camper["N_celular"] = N_celular
            camper["N_fijo"] = N_fijo
            camper["Estado"] = N_fijo

    
    with open("JSON/Campers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

def ev_camper():
    limpiar_terminal()
    print("""
            **********************
            *                    *
            *  NOTAS    CAMPERS  *
            *                    *
            **********************
            """)
    edit = open("JSON/Campers.json")
    Dat = json.load(edit)
    camp = Dat["Campers"]
    ID_camper = int(input("Ingrese el número de identificación del camper que desea hallar su calificacion final:"))
    for camp in camp:
        if camp["ID"] == ID_camper:  
            teo = float(input("Ingrese promedio de notas de la teorica: "))
            pra = float(input("Ingrese promedio de notas de la practica: "))
            pro = float(input("Ingrese promedio da la procedimental: "))
            final = (teo *  0.3) + (pra *  0.6) + (pro *  0.1)
            if final >=  60:
                    camp['Estado'] = "Aprobado"  
                    camp["nota"] = ("",final) 
                    print("¡Este camper ha aprobado el filtro mensual con una nota final de", final)
            else:
                    camp['Estado'] = "Reprobado"   
                    camp["nota"] = "la nota es",final
                    print("El camper no ha aprobado, Su nota final es", final)
        else:
           print("Camper no encontrado.")  
           break   
                         
                    
                      
    with open("JSON/Campers.json", "w") as outfile:
        json.dump(Dat, outfile, indent=4)

def imprimir_todos_los_campers():
    limpiar_terminal()
    print("""
            **********************
            *                    *
            *  IMPRIMIR CAMPERS  *
            *                    *
            **********************
            """)
    try:
        with open('JSON/Campers.json', 'r') as archivo:
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

def listar_campers_por_estado(estado):
    limpiar_terminal()
    print("""
            **********************
            *                    *
            * LISTAR POR ESTADO  *
            *                    *
            **********************
            """)
    with open('JSON/Campers.json') as f:
        data = json.load(f)
        campers = data['Campers']

    campers_segun_estado = [camper for camper in campers if camper['Estado'] == estado]

    if campers_segun_estado:
        print(f"Campers con estado '{estado}':")
        for camper in campers_segun_estado:
            print("")
            print("ID:", camper['ID'])
            print("Nombre:", camper['nombres'])
            print("Apellido:", camper['apellido'])
            print("Ciudad:", camper['ciudad'])
            print("Dirección:", camper['Direccion'])
            print("Acudiente:", camper['Acudiente'])
            print("Número celular:", camper['N_celular'])
            print("Número fijo:", camper['N_fijo'])
            print("Estado:", camper['Estado'])
            print("Nota:", camper['nota'])
            print()  # Imprimir una línea en blanco entre cada camper
    else:
        print(f"No hay campers con estado '{estado}'.")

def listar_campers_por_estado_opcion():
    estado = input("Ingrese el estado para listar campers: ")
    listar_campers_por_estado(estado)

def modificar_ruta_general(ruta_json):
    limpiar_terminal()
    print("""
            **********************
            *                    *
            *  MODIFICAR  RUTA   *
            *                    *
            **********************
            """)    
    camper_id = int(input("Ingrese el ID del camper: "))

    with open(ruta_json, 'r') as file:
        data = json.load(file)
        campers = data['Campers']

        for camper in campers:
            if camper['ID'] == camper_id:
                print("Rutas de Entrenamiento Disponibles:")
                print("1. Java")
                print("2. NodeJS")
                print("3. NetCore")

                opcion = int(input("Seleccione la ruta de entrenamiento (1, 2 o 3): "))

                if opcion == 1:
                    camper['Ruta General'] = "Java"
                elif opcion == 2:
                    camper['Ruta General'] = "NodeJS"
                elif opcion == 3:
                    camper['Ruta General'] = "NetCore"
                else:
                    print("Opción no válida. Por favor seleccione 1, 2 o 3.")
                    return

        with open(ruta_json, 'w') as file:
            json.dump(data, file, indent=4)

    ruta_json = 'JSON/Campers.json'


def asignar_a_salon(camper, salones):
    for salon in salones:
        if salones[salon] < 33:  # Verifica si el salón tiene capacidad
            if camper["Estado"] == "Aprobado":  # Verifica si el estado del camper es "Aprobado"
                if camper["Ruta General"] == "NetCore":
                    camper["Salon"] = "Sputnik"
                elif camper["Ruta General"] == "Java":
                    camper["Salon"] = "Artemis"
                elif camper["Ruta General"] == "NodeJS":
                    camper["Salon"] = "Apollo"
                else:
                    nuevo_salon = f"Salon-{len(salones) + 1}"
                    camper["Salon"] = nuevo_salon
                    salones[nuevo_salon] = 1
                salones[camper["Salon"]] += 1  # Incrementa la cantidad de campers en el salón correspondiente
                print(f"El camper con ID {camper['ID']} ha sido asignado al salón {camper['Salon']}.")
                return
    # Si no se encontró ningún salón con capacidad, se crea uno nuevo
    nuevo_salon = f"Salon-{len(salones) + 1}"
    camper["Salon"] = nuevo_salon
    salones[nuevo_salon] = 1  # Se agrega el nuevo salón a la lista de salones y se asigna el camper a este nuevo salón
    print(f"El camper con ID {camper['ID']} ha sido asignado al nuevo salón {camper['Salon']}.")

def asignar_campers_a_salones(file_path):
    with open(file_path) as file:
        data = json.load(file)

    campers = data["Campers"]
    salones = {"Sputnik": 30}  # Ejemplo de salón con capacidad inicial

    for camper in campers:
        asignar_a_salon(camper, salones)

    data["Campers"] = campers
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        

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
        print("*Notas Camper      (2)")
        print("*Actualizar Camper (3)")
        print("*Listar Campers    (4)")
        print("*Listar por Estado (5)")
        print("*Modificar Ruta    (6)")
        print("*Asignar Salones   (7)")  # Nueva opción para asignar campers a salones
        print("*Atras             (8)")

        opcion = input("Ingrese la opción deseada: ")

        opciones_dict = {
            1: add_campers,
            2: ev_camper,
            3: actualizar_datos_camper,
            4: imprimir_todos_los_campers,
            5: listar_campers_por_estado_opcion,
            6: modificar_ruta_general,
            7: asignar_campers_a_salones,  # Llama a la función que asigna campers a salones
            8: lambda: print("Saliendo del menú de administración.")
        }

        if opcion.isdigit() and int(opcion) in range(1, 9):
            if int(opcion) == 7:
                opciones_dict[int(opcion)]('JSON/Campers.json')  # Pasa el archivo JSON como argumento a la función seleccionada
            else:
                opciones_dict[int(opcion)]()
        elif opcion.lower() == '0':
            print("Saliendo del menú de administración.")
            break
        else:
            print("Ingrese una opción válida (1-8).")
            continue

camper_menu()
