class Cancion:
    def __init__(self, nombre, artista, pesoKb):
        self.nombre = nombre
        self.artista = artista
        self.pesoKb = pesoKb

    def __str__(self):
        return f"Canción: {self.nombre} - {self.artista} ({self.pesoKb}Kb)"


class Video:
    def __init__(self, nombre, artista, pesoMb):
        self.nombre = nombre
        self.artista = artista
        self.pesoMb = pesoMb

    def __str__(self):
        return f"Video: {self.nombre} - {self.artista} ({self.pesoMb}Mb)"


class Mp4:
    def __init__(self, marca, capacidadGb):
        self.marca = marca
        self.capacidadGb = capacidadGb  # en GB
        self.canciones = []
        self.videos = []

    # Calcular espacio usado (en MB)
    def espacio_usado(self):
        totalCanciones = sum(c.pesoKb for c in self.canciones) / 1024  # pasar a MB
        totalVideos = sum(v.pesoMb for v in self.videos)
        return totalCanciones + totalVideos

    def espacio_disponible(self):
        return self.capacidadGb * 1024 - self.espacio_usado()  # todo en MB

    # Método para borrar canción
    def borrar_cancion(self, nombre, artista, pesoKb):
        for c in self.canciones:
            if c.nombre == nombre and c.artista == artista and c.pesoKb == pesoKb:
                self.canciones.remove(c)
                print("Canción eliminada:", c)
                return
        print("No se encontró la canción a borrar.")

    # Sobrecargar operador + para añadir canción
    def __add__(self, cancion):
        if isinstance(cancion, Cancion):
            if cancion not in self.canciones and self.espacio_disponible() >= cancion.pesoKb / 1024:
                self.canciones.append(cancion)
                print("Canción añadida:", cancion)
            else:
                print("No se pudo añadir canción (ya existe o sin espacio).")
        return self

    # Sobrecargar operador * para añadir video
    def __mul__(self, video):
        if isinstance(video, Video):
            if video not in self.videos and self.espacio_disponible() >= video.pesoMb:
                self.videos.append(video)
                print("Video añadido:", video)
            else:
                print("No se pudo añadir video (ya existe o sin espacio).")
        return self

    def __str__(self):
        return f"MP4 {self.marca}, Capacidad: {self.capacidadGb}Gb, " \
               f"Canciones: {len(self.canciones)}, Videos: {len(self.videos)}"


# MAIN DE PRUEBA
if __name__ == "__main__":
    # Crear Mp4
    mp4 = Mp4("Sony", 1)  # 1GB = 1024 MB

    # Canciones
    c1 = Cancion("Back To Black", "Amy Winehouse", 100)
    c2 = Cancion("Lost On You", "LP", 150)

    # Videos
    v1 = Video("Heathens", "twenty one pilots", 50)
    v2 = Video("Harmonica Andromeda", "KSHMR", 70)

    # Agregar canciones con operador +
    mp4 = mp4 + c1
    mp4 = mp4 + c2

    # Agregar videos con operador *
    mp4 = mp4 * v1
    mp4 = mp4 * v2

    # Mostrar datos
    print(mp4)

    # Borrar una canción
    mp4.borrar_cancion("Back To Black", "Amy Winehouse", 100)

    # Mostrar espacio disponible
    print("Espacio disponible (MB):", mp4.espacio_disponible())
