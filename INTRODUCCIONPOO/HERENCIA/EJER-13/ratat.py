class Empleado:
    def __init__(self, nombre, sueldo_mes):
        self.nombre = nombre
        self.sueldo_mes = sueldo_mes

    def mostrar(self):
        print(f"Nombre: {self.nombre} - Sueldo mensual: {self.sueldo_mes}")

    def sueldo_total(self):
        return self.sueldo_mes


class Administrativo(Empleado):
    def __init__(self, nombre, sueldo_mes, cargo):
        super().__init__(nombre, sueldo_mes)
        self.cargo = cargo

    def mostrar(self):
        super().mostrar()
        print(f"Cargo: {self.cargo}")


class Chef(Empleado):
    def __init__(self, nombre, sueldo_mes, hora_extra, tipo, sueldo_hora):
        super().__init__(nombre, sueldo_mes)
        self.hora_extra = hora_extra
        self.tipo = tipo
        self.sueldo_hora = sueldo_hora

    def sueldo_total(self):
        return self.sueldo_mes + (self.hora_extra * self.sueldo_hora)

    def mostrar(self):
        super().mostrar()
        print(f"Tipo: {self.tipo} - Horas extra: {self.hora_extra} - Sueldo total: {self.sueldo_total()}")


class Mesero(Empleado):
    def __init__(self, nombre, sueldo_mes, propina, hora_extra, sueldo_hora):
        super().__init__(nombre, sueldo_mes)
        self.propina = propina
        self.hora_extra = hora_extra
        self.sueldo_hora = sueldo_hora

    def sueldo_total(self):
        return self.sueldo_mes + (self.hora_extra * self.sueldo_hora) + self.propina

    def mostrar(self):
        super().mostrar()
        print(f"Propina: {self.propina} - Horas extra: {self.hora_extra} - Sueldo total: {self.sueldo_total()}")


if __name__ == "__main__":
    chef1 = Chef("Remy", 2500, 10, "Principal", 30)
    mesero1 = Mesero("Linguini", 1800, 200, 5, 20)
    mesero2 = Mesero("Colette", 2000, 150, 3, 25)
    admin1 = Administrativo("Skinner", 3000, "Gerente")
    admin2 = Administrativo("Anton", 2800, "Supervisor")

    lista = [chef1, mesero1, mesero2, admin1, admin2]

    X = 2000
    print("\nEmpleados con sueldo mensual igual a", X)
    for e in lista:
        if e.sueldo_mes == X:
            e.mostrar()

    print("\n--- Sueldos Totales ---")
    for e in lista:
        e.mostrar()
        print("-" * 30)
