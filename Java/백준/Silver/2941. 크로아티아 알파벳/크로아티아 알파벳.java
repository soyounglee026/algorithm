import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();
        char c;
        char cp = '.';
        int i = 0;
        int sum = 0;

        while(true) {
            if (i >= str.length())
                break;
            else if (i <= str.length()-2)
                cp = str.charAt(i+1);
            c = str.charAt(i);

            if(c == 'c' && (cp == '=' || cp == '-')) {
                sum++;
            }
            else if (c == 'd' && cp == '-') {
                sum++;
            }
            else if (c == 'd' && i < str.length() - 2 && cp == 'z' && str.charAt(i + 2) == '=') {
                sum++;
                i++;
            }
            else if (c == 'l' && cp == 'j') {
                sum++;
            }
            else if (c == 'n' && cp == 'j') {
                sum++;
            }
            else if (c == 's' && cp == '=') {
                sum++;
            }
            else if (c == 'z' && cp == '=') {
                sum++;
            }
            else {
                sum++;
                i--;
            }
            i += 2;
        }

        System.out.println(sum);

        sc.close();
    }
}
