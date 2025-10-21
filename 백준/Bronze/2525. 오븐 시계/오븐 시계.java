import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        b += c;

        int m = b%60;
        int h = a+(b/60);

        System.out.println(h%24+" "+m);
    }
}
