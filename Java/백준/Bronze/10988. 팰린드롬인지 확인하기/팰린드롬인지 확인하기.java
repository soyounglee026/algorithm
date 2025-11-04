import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.nextLine();
        int size = word.length();
        int tf = 1;

        for (int i=0; i<size/2; i++) {
            if (word.charAt(i) != word.charAt(size-i-1)) {
                tf = 0;
                break;
            }
        }

        System.out.println(tf);

        sc.close();
    }
}
