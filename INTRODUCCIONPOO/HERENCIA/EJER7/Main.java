package INTRODUCCIONPOO.HERENCIA.EJER7;

public class Main {
    public static void main(String[] args) {
        Estudiante e1 = new Estudiante("Carlos", "Gomez", "Luna", 20, "RU123", "MAT456");
        Estudiante e2 = new Estudiante("Ana", "Perez", "Rojas", 22, "RU789", "MAT101");
        Docente d1 = new Docente("Luis", "Torrez", "Mora", 22, 3500, "RP998");

        System.out.println("=== Estudiantes ===");
        e1.mostrar();
        System.out.println();
        e2.mostrar();

        System.out.println("\n=== Docente ===");
        d1.mostrar();

        double promedio = e1.promedioEdad(e2);
        System.out.println("\nPromedio edad estudiantes: " + promedio);

        e1.modificarEdad(23);
        System.out.println("\nEdad modificada de e1:");
        e1.mostrar();

        if (e2.edad == d1.edad) {
            System.out.println("\nEl estudiante 2 tiene la misma edad que el docente.");
        } else {
            System.out.println("\nNo tienen la misma edad.");
        }
    }
}
