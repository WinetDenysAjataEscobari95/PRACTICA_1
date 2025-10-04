class Politico:
    def __init__(self, profesion, años_exp):
        self.profesion = profesion
        self.años_exp = años_exp

class Partido:
    def __init__(self, nombre_p, rol):
        self.nombre_p = nombre_p
        self.rol = rol

class Presidente(Politico, Partido):
    def __init__(self, nombre, apellido, profesion, años_exp, nombre_p, rol):
        Politico.__init__(self, profesion, años_exp)
        Partido.__init__(self, nombre_p, rol)
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Presidente: {self.nombre} {self.apellido}, Profesión: {self.profesion}, Años de experiencia: {self.años_exp}, Partido: {self.nombre_p}, Rol: {self.rol}"

presidente1 = Presidente("Armando", "Mendoza", "Abogado", 10, "Partido Azul", "Líder")
presidente2 = Presidente("Beatriz", "Pinzon", "Economista", 15, "Partido Rojo", "Dirigente")

print(presidente1)
print(presidente2)

presidentes = [
    Presidente("Armando", "Mendoza", "Abogado", 10, "Partido Azul", "Líder"),
    Presidente("Beatriz", "Pinzon", "Economista", 15, "Partido Rojo", "Dirigente"),
    Presidente("Nicolas", "Mora", "Ingeniero", 12, "Partido Verde", "Representante")
]

nombre_buscar = "Armando"
for presidente in presidentes:
    if presidente.nombre == nombre_buscar:
        print(f"Presidente encontrado: {presidente.nombre} {presidente.apellido}")
        print(f"Partido político: {presidente.nombre_p}")
        print(f"Profesión: {presidente.profesion}")
        break