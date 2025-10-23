import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] subjects = new int[n];
        int max = 0;
        float sum = 0;

        for (int i=0; i<n; i++) {
            int score = sc.nextInt();
            subjects[i] = score;

            if (score > max)
                max = score;
        }

        for (int i=0; i<n; i++) {
            sum += ((float) subjects[i] / max) * 100;
        }
        System.out.print(sum/n);
    }
}
