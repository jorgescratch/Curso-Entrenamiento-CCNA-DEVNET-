def solicitar_datos():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    sede = input("Ingrese su sede: ")

    print("\nDatos ingresados:")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad}")
    print(f"Sede: {sede}")

if __name__ == "__main__":
    solicitar_datos()
