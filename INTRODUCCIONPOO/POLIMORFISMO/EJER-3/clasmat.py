class Matriz:
    def __init__(self, matriz=None):
        if matriz is None:
            self.matriz = [[1 if i == j else 0 for j in range(10)] for i in range(10)]
        else:
            self.matriz = matriz

    @classmethod
    def crear_matriz(cls, matriz):
        return cls(matriz)

    def sumar(self, otra_matriz):
        if len(self.matriz) != len(otra_matriz.matriz) or len(self.matriz[0]) != len(otra_matriz.matriz[0]):
            raise ValueError("Las matrices deben tener el mismo tamaño")
        resultado = [[self.matriz[i][j] + otra_matriz.matriz[i][j] for j in range(len(self.matriz[0]))] for i in range(len(self.matriz))]
        return Matriz(resultado)

    def restar(self, otra_matriz):
        if len(self.matriz) != len(otra_matriz.matriz) or len(self.matriz[0]) != len(otra_matriz.matriz[0]):
            raise ValueError("Las matrices deben tener el mismo tamaño")
        resultado = [[self.matriz[i][j] - otra_matriz.matriz[i][j] for j in range(len(self.matriz[0]))] for i in range(len(self.matriz))]
        return Matriz(resultado)

    def igual(self, otra_matriz):
        if len(self.matriz) != len(otra_matriz.matriz) or len(self.matriz[0]) != len(otra_matriz.matriz[0]):
            return False
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if self.matriz[i][j] != otra_matriz.matriz[i][j]:
                    return False
        return True

    def __str__(self):
        return '\n'.join([' '.join([str(num) for num in fila]) for fila in self.matriz])

def main():
    # Instanciar un objeto con valores predeterminados
    matriz1 = Matriz()

    # Instanciar un objeto matriz
    matriz2 = Matriz.crear_matriz([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                   [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                                   [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                                   [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                   [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                                   [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
                                   [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                                   [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                                   [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
                                   [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]])

    # Sumar matrices
    matriz3 = matriz1.sumar(matriz2)
    print("Matriz 1:")
    print(matriz1)
    print("\nMatriz 2:")
    print(matriz2)
    print("\nMatriz 1 + Matriz 2:")
    print(matriz3)

    # Restar matrices
    matriz4 = matriz2.restar(matriz1)
    print("\nMatriz 2 - Matriz 1:")
    print(matriz4)

    # Comprobar si las matrices son iguales
    print("\n¿Matriz 1 es igual a Matriz 2?", matriz1.igual(matriz2))

if __name__ == "__main__":
    main()
