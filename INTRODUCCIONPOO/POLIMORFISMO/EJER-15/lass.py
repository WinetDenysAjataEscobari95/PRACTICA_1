class Ordenador:
    def __init__(self, codigo_serial, numero, memoria_ram, procesador, estado):
        self.codigo_serial = codigo_serial
        self.numero = numero
        self.memoria_ram = memoria_ram
        self.procesador = procesador
        self.estado = estado

    def __str__(self):
        return f"Código serial: {self.codigo_serial}, Número: {self.numero}, Memoria RAM: {self.memoria_ram} GB, Procesador: {self.procesador}, Estado: {self.estado}"

class Laboratorio:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.ordenadores = []

    def agregar_ordenador(self, ordenador):
        if len(self.ordenadores) < self.capacidad:
            self.ordenadores.append(ordenador)
        else:
            print("No hay más espacio para ordenadores")

    def informacion(self, estado=None):
        if estado is None:
            for ordenador in self.ordenadores:
                print(ordenador)
        else:
            for ordenador in self.ordenadores:
                if ordenador.estado == estado:
                    print(ordenador)

    def informacion_ordenadores_ram(self, ram):
        for ordenador in self.ordenadores:
            if ordenador.memoria_ram > ram:
                print(ordenador)

    def trasladar_ordenadores(self, laboratorio_destino, cantidad):
        ordenadores_trasladados = self.ordenadores[:cantidad]
        self.ordenadores = self.ordenadores[cantidad:]
        laboratorio_destino.ordenadores.extend(ordenadores_trasladados)
        return ordenadores_trasladados

# Crear laboratorios y ordenadores
laboratorio1 = Laboratorio("Lasin 1", 10)
laboratorio2 = Laboratorio("Lasin 2", 10)

ordenador1 = Ordenador("12345", 1, 16, "Intel Core i7", "activo")
ordenador2 = Ordenador("67890", 2, 8, "Intel Core i5", "activo")
ordenador3 = Ordenador("34567", 3, 32, "AMD Ryzen 9", "inactivo")
ordenador4 = Ordenador("90123", 4, 16, "Intel Core i7", "activo")
ordenador5 = Ordenador("45678", 5, 8, "Intel Core i5", "inactivo")
ordenador6 = Ordenador("23456", 6, 32, "AMD Ryzen 9", "activo")

# Agregar ordenadores a los laboratorios
laboratorio1.agregar_ordenador(ordenador1)
laboratorio1.agregar_ordenador(ordenador2)
laboratorio1.agregar_ordenador(ordenador3)
laboratorio2.agregar_ordenador(ordenador4)
laboratorio2.agregar_ordenador(ordenador5)
laboratorio2.agregar_ordenador(ordenador6)

# Mostrar información antes del traslado
print("Estado antes del traslado:")
print("Laboratorio 1:")
laboratorio1.informacion()
print("Laboratorio 2:")
laboratorio2.informacion()

# Trasladar ordenadores
laboratorio1.trasladar_ordenadores(laboratorio2, 2)

# Mostrar información después del traslado
print("\nEstado después del traslado:")
print("Laboratorio 1:")
laboratorio1.informacion()
print("Laboratorio 2:")
laboratorio2.informacion()

# Mostrar ordenadores con más de 8 GB de RAM
print("\nOrdenadores con más de 8 GB de RAM en Laboratorio 2:")
laboratorio2.informacion_ordenadores_ram(8)

# Mostrar ordenadores activos en Laboratorio 2
print("\nOrdenadores activos en Laboratorio 2:")
laboratorio2.informacion("activo")
