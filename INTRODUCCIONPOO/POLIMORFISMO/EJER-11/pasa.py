class Pasajero:
    def __init__(self, nombre, edad, genero, nroHabitacion, costoPasaje):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nroHabitacion = nroHabitacion
        self.costoPasaje = costoPasaje

    def __str__(self):
        return f"{self.nombre} (Edad: {self.edad}, Género: {self.genero}, Hab: {self.nroHabitacion}, Costo: {self.costoPasaje})"


class Crucero:
    def __init__(self, nombre, paisOrigen, paisDestino):
        self.nombre = nombre
        self.paisOrigen = paisOrigen
        self.paisDestino = paisDestino
        self.pasajeros = []

    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)

    def __str__(self):
        return f"Crucero: {self.nombre}, Origen: {self.paisOrigen}, Destino: {self.paisDestino}, Pasajeros: {len(self.pasajeros)}"

    # operador == (mismo número de pasajeros)
    def __eq__(self, otro):
        return len(self.pasajeros) == len(otro.pasajeros)

    # operador + (suma de costos de pasajes de los pasajeros)
    def __add__(self, otro):
        total1 = sum(p.costoPasaje for p in self.pasajeros)
        total2 = sum(p.costoPasaje for p in otro.pasajeros)
        return total1 + total2

    # operador - (cuenta hombres y mujeres en el crucero)
    def __sub__(self, otro):
        hombres = sum(1 for p in self.pasajeros if p.genero.lower() == "m")
        mujeres = sum(1 for p in self.pasajeros if p.genero.lower() == "f")
        return f"Hombres: {hombres}, Mujeres: {mujeres}"


# MAIN DE PRUEBA
if __name__ == "__main__":
    # Instanciar 5 pasajeros
    p1 = Pasajero("Juan Vargas", 30, "M", 502, 500)
    p2 = Pasajero("Martina Vasques", 25, "F", 603, 1000)
    p3 = Pasajero("Wilmer Montero", 40, "M", 401, 925)
    p4 = Pasajero("Ana Lopez", 28, "F", 510, 700)
    p5 = Pasajero("Carlos Rios", 35, "M", 520, 600)

    # Instanciar 2 cruceros
    c1 = Crucero("Caribeño", "Bolivia", "Brasil")
    c2 = Crucero("Pacífico", "Chile", "México")

    # Agregar pasajeros
    c1.agregar_pasajero(p1)
    c1.agregar_pasajero(p2)
    c1.agregar_pasajero(p3)

    c2.agregar_pasajero(p4)
    c2.agregar_pasajero(p5)

    # Mostrar datos
    print(c1)
    for p in c1.pasajeros:
        print("  ", p)

    print(c2)
    for p in c2.pasajeros:
        print("  ", p)

    # Comparar cantidad de pasajeros (==)
    print("¿Tienen la misma cantidad de pasajeros?:", c1 == c2)

    # Suma de costos de pasajes (+)
    print("Suma de costos de todos los pasajes:", c1 + c2)

    # Restar (-) para contar hombres y mujeres en c1
    print("Conteo en crucero 1:", c1 - c2)
