import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.nextLine();
        int[] alphabet = new int[26];
        int max = 0;
        int index = 0;
        boolean q = false;

        for (int i=0; i<26; i++)
            alphabet[i] = 0;

        for (int i=0; i<word.length(); i++) {
            int idx = (int)word.charAt(i);

            if (idx >= 97)
                idx -= (int)'a';
            else idx -= (int)'A';

            alphabet[idx]++;
        }

        for (int i=0; i<26; i++) {
            if (alphabet[i] == max)
                q = true;
            else if (alphabet[i] > max) {
                max = alphabet[i];
                index = i;
                q = false;
            }
        }

        if (q)
            System.out.println("?");
        else
            System.out.println((char)(index+65));


        sc.close();
    }
}
