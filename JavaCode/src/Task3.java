import java.util.Scanner;

public class Task3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите k: ");
        int k = scanner.nextInt();
        scanner.close();
        double w = 0;
        double z = 1;
        double f = 1;

        for (int i = -2; i <= k; i++) {
            if (i != 4)
                w += z * f / (i - 4);
            z = -z;
            f *= (i + 4);
        }

        System.out.println("W = " + w);
    }
}