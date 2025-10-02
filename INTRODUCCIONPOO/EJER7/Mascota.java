package INTRODUCCIONPOO.EJER7;

public class Mascota {
    
     private String nombre;
    private String tipo;
    private int energia;

    public Mascota(String nombre, String tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.energia = 100;
    }

    public void alimentar() {
        this.energia = Math.min(100, this.energia + 20);
        System.out.println(nombre + " ha sido alimentado. Energía actual: " + energia);
    }

    public void jugar() {
        this.energia = Math.max(0, this.energia - 15);
        System.out.println(nombre + " ha jugado. Energía actual: " + energia);
    }

    public int getEnergia() {
        return energia;
    }

    public String getNombre() {
        return nombre;
    }

    public static void main(String[] args) {
        Mascota mascota1 = new Mascota("Linda", "Perro");
        Mascota mascota2 = new Mascota("Garfield", "Gato");

        System.out.println("Energía inicial de " + mascota1.getNombre() + ": " + mascota1.getEnergia());
        mascota1.alimentar();
        mascota1.jugar();

        System.out.println("\nEnergía inicial de " + mascota2.getNombre() + ": " + mascota2.getEnergia());
        mascota2.alimentar();
        mascota2.jugar();
        mascota2.jugar();
        mascota2.jugar();
        mascota2.jugar();
        mascota2.jugar();
        mascota2.jugar();
    }
}
