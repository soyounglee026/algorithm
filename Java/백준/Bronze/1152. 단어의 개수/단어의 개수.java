import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine().trim();
        String[] words = input.split(" ");

        if (input.isEmpty())
            System.out.println(0);
        else System.out.println(words.length);
        sc.close();
    }
}
