def mostrar_alumno(alumno):
    print("Nombre:", alumno["Nombre"])

    print("Apellido:", alumno["Apellido"])

    print("DNI:", alumno["DNI"])

    print("Fecha de nacimiento:", alumno["Fecha de nacimiento"])

    print("Tutor:", alumno["Tutor"])

    print("Notas:", alumno["Notas"])

    print("Faltas:", alumno["Faltas"])

    print("Amonestaciones:", alumno["amonestaciones"])
    
    print("-" * 30)

def mostrar_todos(datos):
    if len(datos["Alumnos"]) == 0:
        print("No hay alumnos registrados.")
    else:
        for alumno in datos["Alumnos"]:
            mostrar_alumno(alumno)

def modificar_alumno(datos):
    dni_buscar = input("Ingrese el DNI del alumno que desea modificar: ")
    encontrado = False
    
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni_buscar:
            encontrado = True
            print("Alumno encontrado. ¿Qué desea modificar?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Tutor")
            print("4. Cantidad de faltas")
            print("5. Cantidad de amonestaciones")
            opcion = int(input("Elija una opción (1-5): "))
            
            if opcion == 1:
                alumno["Nombre"] = input("Ingrese el nuevo nombre: ")
            elif opcion == 2:
                alumno["Apellido"] = input("Ingrese el nuevo apellido: ")
            elif opcion == 3:
                alumno["Tutor"] = input("Ingrese el nuevo tutor: ")
            elif opcion == 4:
                alumno["Faltas"] = int(input("Ingrese la nueva cantidad de faltas: "))
            elif opcion == 5:
                alumno["amonestaciones"] = int(input("Ingrese la nueva cantidad de amonestaciones: "))
            else:
                print("Opción no válida.")
                return
            
            print("Datos modificados con éxito")
            break
            
    if not encontrado:
        print("No se encontró ningún alumno con ese DNI.")

def agregar_alumno(datos):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    dni = input("Ingrese DNI: ")
    fecha_nac = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
    tutor = input("Ingrese nombre del tutor: ")
    
    
    notas = []
    cantidad_notas = int(input("¿Cuántas notas desea cargar?: "))
    for i in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
        
    faltas = int(input("Ingrese cantidad de faltas iniciales: "))
    amonestaciones = int(input("Ingrese cantidad de amonestaciones iniciales: "))
    
    nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nac,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "amonestaciones": amonestaciones
    }
    
    datos["Alumnos"].append(nuevo_alumno)
    print("¡Alumno agregado con éxito!")

def expulsar_alumno(datos):
    dni_a_buscar = input("Ingrese el DNI del alumno a expulsar: ")
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni_a_buscar:
            datos["Alumnos"].remove(alumno)
            print("El alumno ha sido expulsado correctamente.")
            return
    print("No se encontró un alumno con ese DNI.")


datos_escuela = {
    "Alumnos": [
        {
            "Nombre": "gino",
            "Apellido": "laspina",
            "DNI": "50844279",
            "Fecha de nacimiento": "23/02/2011",
            "Tutor": "Juan Pablo",
            "Notas": [8, 9, 10],
            "Faltas": 2,
            "amonestaciones": 0
        }
    ]
}


def menu():
    while True:
        print("\n--- SISTEMA DE GESTIÓN ESCOLAR ---")
        print("1. Mostrar todos los alumnos")
        print("2. Agregar un alumno")
        print("3. Modificar los datos de un alumno")
        print("4. Expulsar un alumno")
        print("5. Salir")
        
        opcion = int(input("Elija una opción: "))
        
        if opcion == 1:
            print("\n--- LISTA DE ALUMNOS ---")
            mostrar_todos(datos_escuela)
        elif opcion == 2:
            print("\n--- AGREGAR ALUMNO ---")
            agregar_alumno(datos_escuela)
        elif opcion == 3:
            print("\n--- MODIFICAR ALUMNO ---")
            modificar_alumno(datos_escuela)
        elif opcion == 4:
            print("\n--- EXPULSAR ALUMNO ---")
            expulsar_alumno(datos_escuela)
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()