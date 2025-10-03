package INTRODUCCIONPOO.POLIMORFISMO.EJER7;

public class Parada {
        private String nombreP;
    private String[] admins;
    private String[][] autos;
    private int adminIndex;
    private int autoIndex;

    public Parada(String nombreP) {
        this.nombreP = nombreP;
        this.admins = new String[10];
        this.autos = new String[10][3];
        this.adminIndex = 0;
        this.autoIndex = 0;
    }

    public void mostrar() {
        System.out.println("Nombre de la parada: " + nombreP);
        System.out.println("Administradores:");
        for (String admin : admins) {
            if (admin != null) {
                System.out.println(admin);
            }
        }
        System.out.println("Autos:");
        for (String[] auto : autos) {
            if (auto[0] != null) {
                System.out.println("Modelo: " + auto[0] + ", Conductor: " + auto[1] + ", Placa: " + auto[2]);
            }
        }
    }

    public void adicionarAdmin(String admin) {
        if (adminIndex < admins.length) {
            admins[adminIndex] = admin;
            adminIndex++;
        } else {
            System.out.println("No hay más espacio para administradores");
        }
    }

    public void adicionarAuto(String modelo, String conductor, String placa) {
        if (autoIndex < autos.length) {
            autos[autoIndex][0] = modelo;
            autos[autoIndex][1] = conductor;
            autos[autoIndex][2] = placa;
            autoIndex++;
        } else {
            System.out.println("No hay más espacio para autos");
        }
    }

    public static void main(String[] args) {
        Parada parada = new Parada("Parada 1");
        parada.adicionarAdmin("Admin 1");
        parada.adicionarAuto("Toyota", "Juan", "ABC123");
        parada.mostrar();
    }
}

