class Persona:
    def __init__(self, nombre, paterno, materno, edad, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci

    def mostrarDatos(self):
        print(f"Nombre: {self.nombre} {self.paterno} {self.materno}")
        print(f"Edad: {self.edad}")
        print(f"CI: {self.ci}")

    def mayorDeEdad(self):
        return self.edad >= 18

    def modificarEdad(self, nuevo):
        self.edad = nuevo

def main():
    persona1 = Persona("Juan", "Pérez", "García", 25, "123456")
    persona2 = Persona("María", "Pérez", "Rodríguez", 30, "789012")

    print("Persona 1:")
    persona1.mostrarDatos()
    print(f"Mayor de edad: {persona1.mayorDeEdad()}")

    print("\nPersona 2:")
    persona2.mostrarDatos()
    print(f"Mayor de edad: {persona2.mayorDeEdad()}")

    print(f"\nTienen el mismo apellido paterno: {persona1.paterno == persona2.paterno}")

    persona1.modificarEdad(35)
    print(f"\nNueva edad de persona 1: {persona1.edad}")

if __name__ == "__main__":
    main()