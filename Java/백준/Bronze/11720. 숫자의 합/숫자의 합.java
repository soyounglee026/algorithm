import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int sum = 0;
        sc.nextLine();

        String s = sc.nextLine();
        String[] nums = new String[n];

        nums = s.split("");

        for (int i=0; i<n; i++) {
            sum += (int)nums[i].charAt(0) - (int)'0';
        }

        System.out.println(sum);
    }
}
