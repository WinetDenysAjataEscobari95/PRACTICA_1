package INTRODUCCIONPOO.HERENCIA.EJER11;

public class Main {
    public static void main(String[] args) {
        JefePolicia j1 = new JefePolicia("Jaden Smith", 45, 5200, "Capitán", "Zona Sur");
        JefePolicia j2 = new JefePolicia("Jenna Ortega", 42, 6100, "Capitán", "Zona Norte");

        System.out.println("=== Datos del Jefe 1 ===");
        j1.mostrar();
        System.out.println("\n=== Datos del Jefe 2 ===");
        j2.mostrar();

        // b) Mayor sueldo
        System.out.println("\n--- Comparación de Sueldos ---");
        if (j1.getSueldo() > j2.getSueldo()) {
            System.out.println(j1.nombre + " tiene mayor sueldo.");
        } else if (j2.getSueldo() > j1.getSueldo()) {
            System.out.println(j2.nombre + " tiene mayor sueldo.");
        } else {
            System.out.println("Ambos tienen el mismo sueldo.");
        }

        // c) Mismo grado
        System.out.println("\n--- Comparación de Grado ---");
        if (j1.getGrado().equalsIgnoreCase(j2.getGrado())) {
            System.out.println("Ambos tienen el mismo grado.");
        } else {
            System.out.println("Tienen diferentes grados.");
        }
    }
}
