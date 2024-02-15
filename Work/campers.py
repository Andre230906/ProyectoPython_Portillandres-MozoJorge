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
    newc["N_fijo"] = input("*Ingrese el numero de teléfono fijo del nuevo camper               : ")
    newc["N_fijo"] = input("*Ingrese la fecha de inicio del camper                             : ")
    newc["N_fijo"] = input("*Ingrese la fecha final del camper                                 : ")
    newc["Estado"] = "inscrito"
    newc["Nota"] = "1"
    newc["Ruta General"] = "a"
    newc["Ruta Especifica"] = "a"
    newc["Salon"] = "a"
    newc["Grupo"] = "a"
    newc["Modulo"] = "a"



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
            if final >=  65:
                    camp['Estado'] = "Aprobado"  
                    camp["nota"] = ("",final) 
                    print("¡Este camper ha aprobado el filtro mensual con una nota final de", final)
            elif final >59 & final < 65:
                    camp['Estado'] = "Bajo rendimiento"   
                    camp["nota"] = "la nota es",final
                    print("El camper esta en riego, Su nota final es", final)
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
                    print("nota:", camper['nota'])
                    print("Ruta General:", camper['Ruta General'])
                    print("Ruta Especifica:", camper['Ruta Especifica'])
                    print("Salon:", camper['Salon'])
                    print("Grupo:", camper['Grupo'])
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

def asignar_horario_a_camper():
    with open("JSON/Campers.json", "r") as edit:
        data = json.load(edit)
    campers = data["Campers"]
    camper_encontrado = False
    camper_id = int(input("Ingrese el número de identificación del camper que desea añadir al grupo:"))
    for camper in campers:
        if camper["ID"] == camper_id:
            camper_encontrado = True
            salon = camper["Salon"]
            if salon == "Sputnik":
                horario = input(f"¿Qué horario asignado desea elegir para el camper {camper['ID']} en el salón Sputnik?\n"
                                "1. Horario 6:00 a 10:00\n"
                                "2. Horario 10:00 a 14:00\n"
                                "3. Horario de 14:00 a 18:00\n"
                                "4. Horario de 18:00 a 22:00\n"
                                "Ingrese el número correspondiente al horario deseado: ")
                if horario == "1":
                    camper["Grupo"] = "P1"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 6:00 a 10:00 en el grupo P1")
                    
                elif horario == "2":
                    camper["Grupo"] = "P2"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 10:00 a 14:00 en el grupo P2")
                    
                elif horario == "3":
                    camper["Grupo"] = "P3"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 14:00 a 18:00 en el grupo P3")
                    
                elif horario == "4":
                    camper["Grupo"] = "P4"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 18:00 a 22:00 en el grupo P4")

                else:
                    print("Opción inválida. No se asignará un grupo para este camper.")
            elif salon == "Artemis":
                horario = input(f"¿Qué horario asignado desea elegir para el camper {camper['ID']} en el salón Artemis?\n"
                                "1. Horario 6:00 a 10:00\n"
                                "2. Horario 10:00 a 14:00\n"
                                "3. Horario de 14:00 a 18:00\n"
                                "4. Horario de 18:00 a 22:00\n"
                                "Ingrese el número correspondiente al horario deseado: ")
                if horario == "1":
                    camper["Grupo"] = "M1"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 6:00 a 10:00 en el grupo M1")
                    
                elif horario == "2":
                    camper["Grupo"] = "M2"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 10:00 a 14:00 en el grupo M2")
                    
                elif horario == "3":
                    camper["Grupo"] = "M3"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 14:00 a 18:00 en el grupo M3")
                    
                elif horario == "4":
                    camper["Grupo"] = "M4"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 18:00 a 22:00 en el grupo M4")

                else:
                    print("Opción inválida. No se asignará un grupo para este camper.")
            elif salon == "Apollo":
                horario = input(f"¿Qué horario asignado desea elegir para el camper {camper['ID']} en el salón Apollo?\n"
                                "1. Horario 6:00 a 10:00\n"
                                "2. Horario 10:00 a 12:00\n"
                                "3. Horario de 14:00 a 18:00\n"
                                "4. Horario de 18:00 a 22:00\n"
                                "Ingrese el número correspondiente al horario deseado: ")
                if horario == "1":
                    camper["Grupo"] = "J1"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 6:00 a 10:00 en el grupo J1")
                    
                elif horario == "2":
                    camper["Grupo"] = "J2"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 10:00 a 14:00 en el grupo J2")
                    
                elif horario == "3":
                    camper["Grupo"] = "J3"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 14:00 a 18:00 en el grupo J3")
                    
                elif horario == "4":
                    camper["Grupo"] = "J4"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 18:00 a 22:00 en el grupo J4")
                else:
                    print("Opción inválida. No se asignará un grupo para este camper.")
            else:
                print(f"No se reconoce el salón {salon}. No se asignará un grupo para el camper {camper['ID']}.")
            break

    if not camper_encontrado:
        print(f"No se encontró ningún camper con el ID {camper_id}.")

    with open("JSON/Campers.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

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

def agregar_modulos_a_camper_desde_consola():
    modulos_disponibles = [
        "Fundamentos de Programacion",
        "Programacion Web (HTML, CSS, B)",
        "Programacion Formal",
        "Bases de datos",
        "Backend"
    ]

    id_camper = int(input("Ingrese el ID del camper al que desea agregar los módulos: "))
    ruta_general = input("Ingrese la ruta general del camper (Java, NodeJs o NetCore): ")

    # Obtener el camper con el ID especificado
    with open('JSON/Campers.json') as f:
        data = json.load(f)
        campers = data['Campers']
        camper_encontrado = next((c for c in campers if c['ID'] == id_camper), None)

    if camper_encontrado:
        if camper_encontrado['Ruta General'] == ruta_general:
            print(f"Camper encontrado: {camper_encontrado['nombres']} {camper_encontrado['apellido']}")
            print(f"Ruta General: {ruta_general}")
            
            modulos_seleccionados = []
            agregar_mas_modulos = True
            while agregar_mas_modulos:
                print("Modulos disponibles para agregar:")
                for i, modulo in enumerate(modulos_disponibles, 1):
                    print(f"{i}. {modulo}")
                
                modulo_seleccionado = int(input("Ingrese el número del módulo que desea agregar: "))
                modulos_seleccionados.append(modulos_disponibles[modulo_seleccionado - 1])

                respuesta = input("¿Desea agregar otro módulo? (s/n): ")
                if respuesta.lower() != "s":
                    agregar_mas_modulos = False
            
            print(f"Añadiendo los siguientes módulos al camper {camper_encontrado['nombres']} {camper_encontrado['apellido']}:")
            for modulo in modulos_seleccionados:
                print(modulo)
            camper_encontrado['Modulo'] = modulos_seleccionados
            with open('JSON/Campers.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
            # Aquí podrías actualizar el registro del camper en el JSON con los nuevos módulos
            # Por cuestiones de simplicidad, no se muestra el código para actualizar el JSON en este ejemplo
        else:
            print(f"El camper encontrado no tiene la ruta general {ruta_general}")
    else:
        print(f"No se encontró un camper con el ID {id_camper}")
        

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

def asignar_horario_a_camper():
    with open("JSON/Campers.json", "r") as edit:
        data = json.load(edit)
    campers = data["Campers"]
    camper_encontrado = False
    camper_id = int(input("Ingrese el número de identificación del camper que desea añadir al grupo:"))
    for camper in campers:
        if camper["ID"] == camper_id:
            camper_encontrado = True
            salon = camper["Salon"]
            if salon == "Sputnik":
                horario = input(f"¿Qué horario asignado desea elegir para el camper {camper['ID']} en el salón Sputnik?\n"
                                "1. Horario 6:00 a 10:00\n"
                                "2. Horario 10:00 a 14:00\n"
                                "3. Horario de 14:00 a 18:00\n"
                                "4. Horario de 18:00 a 22:00\n"
                                "Ingrese el número correspondiente al horario deseado: ")
                if horario == "1":
                    camper["Grupo"] = "P1"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 6:00 a 10:00 en el grupo P1")
                    
                elif horario == "2":
                    camper["Grupo"] = "P2"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 10:00 a 14:00 en el grupo P2")
                    
                elif horario == "3":
                    camper["Grupo"] = "P3"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 14:00 a 18:00 en el grupo P3")
                    
                elif horario == "4":
                    camper["Grupo"] = "P4"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 18:00 a 22:00 en el grupo P4")

                else:
                    print("Opción inválida. No se asignará un grupo para este camper.")
            elif salon == "Artemis":
                horario = input(f"¿Qué horario asignado desea elegir para el camper {camper['ID']} en el salón Artemis?\n"
                                "1. Horario 6:00 a 10:00\n"
                                "2. Horario 10:00 a 14:00\n"
                                "3. Horario de 14:00 a 18:00\n"
                                "4. Horario de 18:00 a 22:00\n"
                                "Ingrese el número correspondiente al horario deseado: ")
                if horario == "1":
                    camper["Grupo"] = "M1"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 6:00 a 10:00 en el grupo M1")
                    
                elif horario == "2":
                    camper["Grupo"] = "M2"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 10:00 a 14:00 en el grupo M2")
                    
                elif horario == "3":
                    camper["Grupo"] = "M3"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 14:00 a 18:00 en el grupo M3")
                    
                elif horario == "4":
                    camper["Grupo"] = "M4"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 18:00 a 22:00 en el grupo M4")

                else:
                    print("Opción inválida. No se asignará un grupo para este camper.")
            elif salon == "Apollo":
                horario = input(f"¿Qué horario asignado desea elegir para el camper {camper['ID']} en el salón Apollo?\n"
                                "1. Horario 6:00 a 10:00\n"
                                "2. Horario 10:00 a 12:00\n"
                                "3. Horario de 14:00 a 18:00\n"
                                "4. Horario de 18:00 a 22:00\n"
                                "Ingrese el número correspondiente al horario deseado: ")
                if horario == "1":
                    camper["Grupo"] = "J1"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 6:00 a 10:00 en el grupo J1")
                    
                elif horario == "2":
                    camper["Grupo"] = "J2"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 10:00 a 14:00 en el grupo J2")
                    
                elif horario == "3":
                    camper["Grupo"] = "J3"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 14:00 a 18:00 en el grupo J3")
                    
                elif horario == "4":
                    camper["Grupo"] = "J4"
                    print(f"El camper con el id {camper_id} ha sido añadido al horario de 18:00 a 22:00 en el grupo J4")
                else:
                    print("Opción inválida. No se asignará un grupo para este camper.")
            else:
                print(f"No se reconoce el salón {salon}. No se asignará un grupo para el camper {camper['ID']}.")
            break

    if not camper_encontrado:
        print(f"No se encontró ningún camper con el ID {camper_id}.")

    with open("JSON/Campers.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

def camper_menu():

    while True:
        print("""
            *********************
            *                   *
            *MENU ADMINISTRACION*
            *                   *
            *********************
            """)
        print("*Agregar Camper       (1)")
        print("*Notas Camper         (2)")
        print("*Actualizar Camper    (3)")
        print("*Listar Campers       (4)")
        print("*Listar por Estado    (5)")
        print("*Modificar Ruta       (6)")
        print("*Asignar Salones      (7)")  # Nueva opción para asignar campers a salones
        print("*Asignar Hora/Grupo   (8)")
        print("*Agregar Modulo       (9)")  # Nueva opción para asignar horario a camper# Nueva opción para asignar horario a camper
        print("*Atras                (10)")

        opcion = input("Ingrese la opción deseada: ")

        opciones_dict = {
            1: add_campers,
            2: ev_camper,
            3: actualizar_datos_camper,
            4: imprimir_todos_los_campers,
            5: listar_campers_por_estado_opcion,
            6: modificar_ruta_general,
            7: asignar_campers_a_salones,  # Llama a la función que asigna campers a salones
            8: asignar_horario_a_camper,
            9: agregar_modulos_a_camper_desde_consola,# Llama a la función que asigna horario a camper
            10: lambda: print("Saliendo del menú de administración.")
        }

        if opcion.isdigit() and int(opcion) in range(1, 10):
            if int(opcion) in [7, 8]:
                opciones_dict[int(opcion)]('JSON/Campers.json')  # Pasa el archivo JSON como argumento a la función seleccionada
            else:
                opciones_dict[int(opcion)]()
        elif opcion.lower() == '0':
            print("Saliendo del menú de administración.")
            break
        else:
            print("Ingrese una opción válida (1-9).")
            continue

camper_menu()
