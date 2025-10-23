import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] nums = new int[10];
        int count = 0;

        for (int i=0; i<10; i++) {
            boolean tf = true;
            nums[i] = -1;
            int n = sc.nextInt();

            for (int j=0; j<=i; j++) {
                if (nums[j] == n%42) {
                    tf = false;
                    break;
                }
            }
            if (tf){
                nums[i] = n%42;
                count++;
            }

        }

        System.out.print(count);
    }
}
