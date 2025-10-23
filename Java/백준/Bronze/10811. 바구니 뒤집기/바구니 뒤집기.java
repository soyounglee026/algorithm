import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] nums = new int[n];
        int m = sc.nextInt();
        int tmp;

        for (int i=1; i<=n; i++)
            nums[i-1] = i;

        for (int i=0; i<m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            for (int j=0; j<=(y-x)/2; j++) {
                tmp = nums[x+j-1];
                nums[x+j-1] = nums[y-j-1];
                nums[y-j-1] = tmp;
            }
        }

        for (int i=0; i<n; i++) {
            System.out.print(nums[i]);
            if (i == n-1)
                break;
            System.out.print(" ");
        }
    }
}
