# main.py
from src.cita import CitaMedica
from src.gestion_datos import cargar_citas, guardar_citas

RUTA_DATOS = "data/citas.json"


def mostrar_menu():
    print("\n===========================================")
    print("   SISTEMA DE GESTIÓN DE CITAS (MEDISENA)")
    print("===========================================")
    print("1. Listar citas")
    print("2. Registrar nueva cita")
    print("3. Consultar total de ingresos proyectados")
    print("4. Salir")


def registrar_cita(citas: list):
    print("\n--- REGISTRO DE NUEVA CITA ---")
    id_cita = input("Ingrese el ID de la cita (ej: CIT-2026-01): ").strip()

    # Validar duplicados
    for item in citas:
        if item["id_cita"].upper() == id_cita.upper():
            print("Error: Ya existe una cita con este ID.")
            return

    paciente = input("Ingrese el nombre del paciente: ").strip()
    especialidad = input("Ingrese la especialidad: ").strip()
    medico_asignado = input("Ingrese el nombre del médico asignado: ").strip()

    try:
        costo_consulta = float(input("Ingrese el costo de la consulta (COP): "))
    except ValueError:
        print("Error: El costo debe ser un valor numérico válido.")
        return

    urgencia_input = input("¿Es urgencia? (S/N): ").strip().upper()
    es_urgencia = urgencia_input == "S"

    # Instanciación y adición
    nueva_cita = CitaMedica(
        id_cita, paciente, especialidad, medico_asignado, costo_consulta, es_urgencia
    )
    citas.append(nueva_cita.a_diccionario())

    # Persistencia automática
    if guardar_citas(RUTA_DATOS, citas):
        print("Cita registrada y guardada exitosamente en el JSON.")


def listar_citas(citas: list):
    """Muestra el listado actual de citas almacenadas."""
    print("\n--- LISTADO DE CITAS ---")
    if not citas:
        print("No hay citas registradas.")
        return

    print(
        f"{'ID CITA':<12} | {'PACIENTE':<20} | {'ESPECIALIDAD':<15} | {'MÉDICO':<20} | {'COSTO FINAL':<12} | {'URGENCIA':<8}"
    )
    print("-" * 95)
    for c in citas:
        print(
            f"{c['id_cita']:<12} | {c['paciente']:<20} | {c['especialidad']:<15} | {c['medico_asignado']:<20} | ${c['costo_final']:<11,.2f} | {c['es_urgencia']!s:<8}"
        )


def calcular_ingresos_proyectados(citas: list):
    total = sum(c.get("costo_final", 0) for c in citas)
    print(f"\nEl total de ingresos proyectados es: ${total:,.2f} COP")


def main():
    citas = cargar_citas(RUTA_DATOS)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            listar_citas(citas)
        elif opcion == "2":
            registrar_cita(citas)
        elif opcion == "3":
            calcular_ingresos_proyectados(citas)
        elif opcion == "4":
            print("\nSaliendo del sistema. ¡Datos asegurados!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
