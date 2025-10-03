

public class Celular {
    private String nroTel;
    private String dueño;
    private int espacio;
    private int ram;
    private int nroApp;

    public Celular(String nroTel, String dueño, int espacio, int ram, int nroApp) {
        this.nroTel = nroTel;
        this.dueño = dueño;
        this.espacio = espacio;
        this.ram = ram;
        this.nroApp = nroApp;
    }

    public void incrementarApp() {
        this.nroApp += 10;
    }

    public void decrementarEspacio() {
        this.espacio -= 5;
        if (this.espacio < 0) {
            this.espacio = 0;
        }
    }

    @Override
    public String toString() {
        return "Número de teléfono: " + nroTel + ", Dueño: " + dueño + ", Espacio: " + espacio + " GB, RAM: " + ram + " GB, Número de aplicaciones: " + nroApp;
    }

    public static void main(String[] args) {
        Celular celular = new Celular("123456789", "Juan", 128, 8, 10);
        System.out.println("Antes de los operadores:");
        System.out.println(celular);

        celular.incrementarApp();
        celular.decrementarEspacio();
        System.out.println("\nDespués de los operadores:");
        System.out.println(celular);
    }
}