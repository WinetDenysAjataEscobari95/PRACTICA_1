# Clase Carta
class Carta:
    def __init__(self, codigo, remitente, destinatario, descripcion):
        self.codigo = codigo
        self.remitente = remitente
        self.destinatario = destinatario
        self.descripcion = descripcion

    def __str__(self):
        return f"Código: {self.codigo}, Remitente: {self.remitente}, Destinatario: {self.destinatario}"


# Clase Buzon
class Buzon:
    def __init__(self, nro):
        self.nro = nro
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def eliminar_carta(self, codigo):
        self.cartas = [c for c in self.cartas if c.codigo != codigo]

    def contar_cartas_para(self, destinatario):
        return sum(1 for c in self.cartas if c.destinatario == destinatario)

    def buscar_por_palabra(self, palabra):
        resultados = []
        for c in self.cartas:
            if palabra.lower() in c.descripcion.lower():
                resultados.append(c)
        return resultados

if __name__ == "__main__":
    # b) Instanciar 3 cartas con sus respectivas descripciones
    c1 = Carta("C123", "Taylor Swift", "Ariana Grande", "Querido amigo, espero que estés bien.")
    c2 = Carta("C456", "Mora", "Feid", "Te escribo para decirte que ella no te ama.")
    c3 = Carta("C789", "Emilia Mernez", "Mora", "Con mucho amor y cariño, te mando saludos.")

    # a) Instanciar 3 buzones diferentes, cada uno con al menos 3 cartas
    b1 = Buzon(1)
    b2 = Buzon(2)
    b3 = Buzon(3)

    b1.agregar_carta(c1)
    b1.agregar_carta(c2)
    b1.agregar_carta(c3)

    # Para que cada buzón tenga al menos 3 cartas
    b2.agregar_carta(c1)
    b2.agregar_carta(c2)
    b2.agregar_carta(c3)

    b3.agregar_carta(c1)
    b3.agregar_carta(c2)
    b3.agregar_carta(c3)

    # c) Verificar cuántas cartas recibió el destinatario “Pepe Mujica”
    total_para_pepe = b1.contar_cartas_para("Mora")
    print(f"Mora recibió {total_para_pepe} carta(s) en el buzón 1")

    # d) Eliminar la carta cuyo código sea "C456"
    print("\nEliminando carta C456...")
    b1.eliminar_carta("C456")
    for c in b1.cartas:
        print(c)

    # e) Verificar si algún remitente ha recibido alguna carta
    print("\nRemitentes que también recibieron cartas:")
    remitentes = [c.remitente for c in b1.cartas]
    destinatarios = [c.destinatario for c in b1.cartas]
    for r in remitentes:
        if r in destinatarios:
            print(f"El remitente {r} también recibió una carta.")

    # f) Buscar palabra clave "amor"
    print("\nBuscando la palabra 'amor' en las cartas del buzón 1:")
    resultados = b1.buscar_por_palabra("amor")

    # g) Mostrar coincidencias
    for carta in resultados:
        print(f"Código: {carta.codigo}, Remitente: {carta.remitente}, Destinatario: {carta.destinatario}")
