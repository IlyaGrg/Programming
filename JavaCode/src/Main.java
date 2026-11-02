import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите n: ");
        int n = scanner.nextInt();

        int[][] a = new int[n][n];
        int[][] b = new int[n][n];
        int[][] d = new int[n][n];

        System.out.println("Введите матрицу A (" + n + "x" + n + "):");
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                a[i][j] = scanner.nextInt();

        System.out.println("Введите матрицу B (" + n + "x" + n + "):");
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                b[i][j] = scanner.nextInt();
        scanner.close();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int s1 = 0;
                int s2 = 0;
                for (int k = 0; k < n; k++) {
                    s1 += a[i][k] * b[k][j];
                    s2 += b[i][k] * a[k][j];
                }
                d[i][j] = s1 - s2;
            }
        }

        System.out.println("Матрица D = A*B - B*A:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                System.out.print(d[i][j] + " ");
            System.out.println();
        }
    }
}