class Persona:
    def __init__(self, nombre, paterno, materno, edad):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre} {self.paterno} {self.materno}")
        print(f"Edad: {self.edad}")


class Docente(Persona):
    def __init__(self, nombre, paterno, materno, edad, sueldo, reg_prof):
        super().__init__(nombre, paterno, materno, edad)
        self.sueldo = sueldo
        self.reg_prof = reg_prof

    def mostrar(self):
        super().mostrar()
        print(f"Sueldo: {self.sueldo}")
        print(f"Registro Profesional: {self.reg_prof}")


class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, edad)
        self.ru = ru
        self.matricula = matricula

    def mostrar(self):
        super().mostrar()
        print(f"RU: {self.ru}")
        print(f"Matrícula: {self.matricula}")

    def modificarEdad(self, nuevaEdad):
        self.edad = nuevaEdad

    def promedioEdad(self, otro):
        return (self.edad + otro.edad) / 2

if __name__ == "__main__":
    e1 = Estudiante("Carlos", "Gómez", "Luna", 20, "RU123", "MAT456")
    e2 = Estudiante("Ana", "Pérez", "Rojas", 22, "RU789", "MAT101")
    d1 = Docente("Luis", "Torrez", "Mora", 22, 3500, "RP998")

    print("=== Datos de los estudiantes ===")
    e1.mostrar()
    print()
    e2.mostrar()

    print("\n=== Datos del docente ===")
    d1.mostrar()

    prom = e1.promedioEdad(e2)
    print(f"\nPromedio de edad de estudiantes: {prom}")

    e1.modificarEdad(23)
    print("\nEdad modificada del primer estudiante:")
    e1.mostrar()

    if e2.edad == d1.edad:
        print("\nEl estudiante 2 tiene la misma edad que el docente.")
    else:
        print("\nNo tienen la misma edad.")
