package INTRODUCCIONPOO.HERENCIA.EJER11;

public class JefePolicia extends Persona implements Empleado {
    private double sueldo;
    private String grado;
    private String zona;

    public JefePolicia(String nombre, int edad, double sueldo, String grado, String zona) {
        super(nombre, edad);
        this.sueldo = sueldo;
        this.grado = grado;
        this.zona = zona;
    }

    @Override
    public double getSueldo() {
        return sueldo;
    }

    @Override
    public void mostrarEmpleado() {
        System.out.println("Sueldo: " + sueldo);
    }

    public void mostrarPolicia() {
        System.out.println("Grado: " + grado);
        System.out.println("Zona: " + zona);
    }

    @Override
    public void mostrar() {
        super.mostrar();
        mostrarEmpleado();
        mostrarPolicia();
    }

    public String getGrado() {
        return grado;
    }
}