import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] s = new String[100];
        int i = 0;

        while (sc.hasNextLine()) {
            String input = sc.nextLine();
            if (input.isEmpty())
                break;
            s[i++] = input;
        }

        for (int j=0; j<i; j++) {
            System.out.println(s[j]);
        }

        sc.close();
    }
}
