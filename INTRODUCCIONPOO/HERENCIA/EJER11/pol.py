class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Empleado:
    def get_sueldo(self):
        pass

    def mostrar_empleado(self):
        pass


class Policia:
    def __init__(self, grado, zona):
        self.grado = grado
        self.zona = zona

    def mostrar_policia(self):
        print(f"Grado: {self.grado}")
        print(f"Zona: {self.zona}")


class JefePolicia(Persona, Empleado):
    def __init__(self, nombre, edad, sueldo, grado, zona):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        self.grado = grado
        self.zona = zona

    def get_sueldo(self):
        return self.sueldo

    def mostrar_empleado(self):
        print(f"Sueldo: {self.sueldo}")

    def mostrar(self):
        super().mostrar()
        self.mostrar_empleado()
        print(f"Grado: {self.grado}")
        print(f"Zona: {self.zona}")


if __name__ == "__main__":
    j1 = JefePolicia("Jaden Smith", 45, 5200, "Capitán", "Zona Sur")
    j2 = JefePolicia("Jenna Ortega", 42, 6100, "Capitán", "Zona Norte")

    print("=== Datos Jefe 1 ===")
    j1.mostrar()
    print("\n=== Datos Jefe 2 ===")
    j2.mostrar()

    print("\n--- Comparación de Sueldos ---")
    if j1.get_sueldo() > j2.get_sueldo():
        print(f"{j1.nombre} tiene mayor sueldo.")
    elif j2.get_sueldo() > j1.get_sueldo():
        print(f"{j2.nombre} tiene mayor sueldo.")
    else:
        print("Ambos tienen el mismo sueldo.")

    print("\n--- Comparación de Grado ---")
    if j1.grado.lower() == j2.grado.lower():
        print("Ambos tienen el mismo grado.")
    else:
        print("Tienen grados diferentes.")
