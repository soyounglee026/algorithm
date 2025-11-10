import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        int count = 0;

        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();

            boolean[] b = new boolean[26];
            boolean isGroup = true;

            char a = str.charAt(0);
            b[a - 'a'] = true;

            for (int j = 0; j < str.length(); j++) {
                if (a != str.charAt(j)) {
                    if (b[str.charAt(j) - 'a']) {
                        isGroup = false;
                        break;
                    }
                    b[a - 'a'] = true;
                }
                a = str.charAt(j);
            }
            if (isGroup)
                count++;
        }
        System.out.println(count);

        sc.close();
    }
}
