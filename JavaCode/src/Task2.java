import java.util.Scanner;

public class Task2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[][] a = new int[4][3];


        System.out.println("Введите матрицу 4x3:");
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 3; j++)
                a[i][j] = scanner.nextInt();

        scanner.close();
        int k1 = 0, k3 = 0;
        for (int i = 1; i < 4; i++) {
            if (a[i][0] > a[k1][0]) k1 = i;
            if (a[i][2] > a[k3][2]) k3 = i;
        }


        int t = a[k1][0];
        a[k1][0] = a[k3][2];
        a[k3][2] = t;

        System.out.println("Результат:");
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 3; j++)
                System.out.print(a[i][j] + " ");
            System.out.println();
        }
    }
}