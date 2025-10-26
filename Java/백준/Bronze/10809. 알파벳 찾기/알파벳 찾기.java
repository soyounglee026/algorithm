import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();
        int[] alphabets = new int[26];
        String[] word = new String[str.length()];
        int a = 0;

        word = str.split("");

        for (int i=0; i<26; i++) {
            alphabets[i] = -1;
        }

        for (int i=0; i<str.length(); i++) {
            a = (int)word[i].charAt(0) - 'a';

            if (alphabets[a] == -1) {
                alphabets[a] = i;
            }
        }

        for (int i=0; i<26; i++) {
            System.out.print(alphabets[i]);

            if (i != 26)
                System.out.print(" ");
        }
    }
}
