import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        for (int i=0; i<n; i++) {
            String s = sc.nextLine();
            String[] str = new String[s.length()];
            str = s.split("");
            System.out.println(str[0]+str[s.length()-1]);
        }
    }
}
