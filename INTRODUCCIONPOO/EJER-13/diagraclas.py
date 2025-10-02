class Fruta:
    def __init__(self, nombre, tipo, nro_vitaminas, vitaminas):
        self.nombre = nombre
        self.tipo = tipo
        self.nro_vitaminas = nro_vitaminas
        self.vitaminas = vitaminas

    def get_nombre(self):
        return self.nombre

    def get_tipo(self):
        return self.tipo

    def get_nro_vitaminas(self):
        return self.nro_vitaminas

    def get_vitaminas(self):
        return self.vitaminas

def main():
    # Instanciar 3 frutas con al menos 2 vitaminas cada una
    fruta1 = Fruta("Kiwi", "Subtropical", 3, ["K", "C", "E"])
    fruta2 = Fruta("Naranja", "Cítrica", 2, ["C", "A"])
    fruta3 = Fruta("Fresa", "Cítrica", 2, ["C", "K"])

    # Verificar cuál es la fruta con más vitaminas
    frutas = [fruta1, fruta2, fruta3]
    fruta_con_mas_vitaminas = max(frutas, key=lambda x: x.get_nro_vitaminas())
    print(f"La fruta con más vitaminas es {fruta_con_mas_vitaminas.get_nombre()} con {fruta_con_mas_vitaminas.get_nro_vitaminas()} vitaminas")

    # Mostrar las vitaminas que tiene la fruta x
    print(f"Las vitaminas de {fruta1.get_nombre()} son: {', '.join(fruta1.get_vitaminas())}")

    # Cuantas vitaminas son cítricas
    vitaminas_citricas = [vitamina for fruta in frutas for vitamina in fruta.get_vitaminas() if fruta.get_tipo() == "Cítrica"]
    print(f"Hay {len(vitaminas_citricas)} vitaminas cítricas")

    # Ordenar las frutas alfabéticamente según el nombre de sus vitaminas
    frutas_ordenadas = sorted(frutas, key=lambda x: sorted(x.get_vitaminas()))
    for fruta in frutas_ordenadas:
        print(f"{fruta.get_nombre()}: {', '.join(fruta.get_vitaminas())}")

if __name__ == "__main__":
    main()
