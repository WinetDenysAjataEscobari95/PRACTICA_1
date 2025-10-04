package INTRODUCCIONPOO.HERENCIA.EJER11;

public class Policia {
    protected String grado;
    protected String zona;

    public Policia(String grado, String zona) {
        this.grado = grado;
        this.zona = zona;
    }

    public void mostrarPolicia() {
        System.out.println("Grado: " + grado);
        System.out.println("Zona: " + zona);
    }

    public String getGrado() {
        return grado;
    }
}
