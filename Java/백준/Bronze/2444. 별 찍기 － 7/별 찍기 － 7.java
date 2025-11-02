import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String blank = " ";
        String star = "*";

        for (int i = 1; i <= (2 * n - 1); i++) {
            if (i <= n) {
                for (int j = 0; j < n - i; j++)
                    System.out.print(blank);
                for (int k = 0; k < 2 * i - 1; k++)
                    System.out.print(star);
            }
            else {
                for (int j = 0; j < i - n; j++)
                    System.out.print(blank);
                for (int k = 0; k < (4 * n - 2 * i) - 1; k++)
                    System.out.print(star);
            }
            System.out.println();
        }

        sc.close();
    }
}
