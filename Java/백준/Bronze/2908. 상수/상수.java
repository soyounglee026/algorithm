import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] input = sc.nextLine().split(" ");
        String[] numString1 = new String[3];
        String[] numString2 = new String[3];

        numString1 = input[0].split("");
        numString2 = input[1].split("");

        String s1 = "", s2 = "";
        int num1, num2;

        for (int i=2; i>=0; i--) {
            s1 += numString1[i];
            s2 += numString2[i];
        }

        num1 = Integer.parseInt(s1);
        num2 = Integer.parseInt(s2);

        if (num1 > num2)
            System.out.println(num1);
        else System.out.println(num2);

        sc.close();
    }
}
