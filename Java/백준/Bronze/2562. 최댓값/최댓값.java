import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] nums = new int[9];

        for (int i=0; i<9; i++)
            nums[i] = sc.nextInt();

        int max = nums[0];
        int count = 0;

        for (int i=0; i<9; i++){
            if (nums[i] > max) {
                max = nums[i];
                count = i;
            }
        }

        System.out.println(max+"\n"+(count+1));
    }
}
