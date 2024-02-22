import java.util.Scanner;

public class Actividad4 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese el número de filas: ");
        int filas = scanner.nextInt();
        System.out.print("Ingrese el número de columnas: ");
        int columnas = scanner.nextInt();

        int[][] array = new int[filas][columnas];

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                System.out.print("Ingrese el elemento en la posición [" + i + "][" + j + "]: ");
                array[i][j] = scanner.nextInt();
            }
        }

        int contNeg = 0, contPos = 0, contCero = 0;

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (array[i][j] < 0) {
                    contNeg++;
                } else if (array[i][j] > 0) {
                    contPos++;
                } else {
                    contCero++;
                }
            }
        }

        System.out.println("Números menores de cero: " + contNeg);
        System.out.println("Números mayores de cero: " + contPos);
        System.out.println("Números iguales a cero: " + contCero);
    }
}
