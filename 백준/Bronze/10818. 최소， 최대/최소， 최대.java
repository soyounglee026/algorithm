import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] nums = new int[n];

        for (int i=0; i<n; i++)
            nums[i] = sc.nextInt();

        int max = nums[0];
        int min = nums[0];

        for (int i=0; i<n; i++){
            if (nums[i] > max)
                max = nums[i];
            if (nums[i] < min)
                min = nums[i];
        }

        System.out.println(min+" "+max);
    }
}
