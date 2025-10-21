import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] balls = new int[n];
        int temp;

        for (int i=0; i<n; i++)
            balls[i] = i+1;

        for (int x=0; x<m; x++){
            int i = sc.nextInt();
            int j = sc.nextInt();

            i--;
            j--;
            temp = balls[i];
            balls[i] = balls[j];
            balls[j] = temp;
        }

        for (int i=0; i<n; i++) {
            System.out.print(balls[i]);
            if (i==(n-1))
                break;
            System.out.print(" ");
        }
    }
}
