import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] balls = new int[n];

        for (int i=0; i<n; i++)
            balls[i] = 0;

        for (int x=0; x<m; x++){
            int i = sc.nextInt();
            int j = sc.nextInt();
            int k = sc.nextInt();

            for (int y=i-1; y<j; y++)
                balls[y] = k;
        }

        for (int i=0; i<n; i++) {
            System.out.print(balls[i]);
            if (i==(n-1))
                break;
            System.out.print(" ");
        }
    }
}
