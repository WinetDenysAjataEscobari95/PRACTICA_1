public class Persona {
    private String nombre;
    private String paterno;
    private String materno;
    private int edad;
    private String ci;

    public Persona(String nombre, String paterno, String materno, int edad, String ci) {
        this.nombre = nombre;
        this.paterno = paterno;
        this.materno = materno;
        this.edad = edad;
        this.ci = ci;
    }

    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre + " " + paterno + " " + materno);
        System.out.println("Edad: " + edad);
        System.out.println("CI: " + ci);
    }

    public boolean mayorDeEdad() {
        return edad >= 18;
    }

    public void modificarEdad(int nuevo) {
        this.edad = nuevo;
    }

    public String getPaterno() {
        return paterno;
    }

    public int getEdad() {
        return edad;
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Hailey", " Rhode", "Baldwin", 28, "123456");
        Persona persona2 = new Persona("Justin", "Drew", "Bieber", 31, "789012");

        System.out.println("Persona 1:");
        persona1.mostrarDatos();
        System.out.println("Mayor de edad: " + persona1.mayorDeEdad());

        System.out.println("\nPersona 2:");
        persona2.mostrarDatos();
        System.out.println("Mayor de edad: " + persona2.mayorDeEdad());

        System.out.println("\nTienen el mismo apellido paterno: " + persona1.getPaterno().equals(persona2.getPaterno()));

        persona1.modificarEdad(35);
        System.out.println("\nNueva edad de persona 1: " + persona1.getEdad());
    }
}