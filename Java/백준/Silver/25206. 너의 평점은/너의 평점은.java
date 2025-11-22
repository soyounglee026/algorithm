import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String subject, score;
        double creditDouble;
        int credit;
        int[] total = new int[8];
        int totalCredit = 0;
        double sum = 0;

        for (int i = 0; i < 20; i++) {
            subject = sc.next();
            creditDouble = sc.nextDouble();
            credit = (int) creditDouble;
            score = sc.next();
            sc.nextLine();

            switch (score) {
                case "A+":
                    total[0] += credit;
                    break;
                case "A0":
                    total[1] += credit;
                    break;
                case "B+":
                    total[2] += credit;
                    break;
                case "B0":
                    total[3] += credit;
                    break;
                case "C+":
                    total[4] += credit;
                    break;
                case "C0":
                    total[5] += credit;
                    break;
                case "D+":
                    total[6] += credit;
                    break;
                case "D0":
                    total[7] += credit;
                    break;
                case "F":
                    totalCredit += credit;
                    break;
            }
        }

        for (int i = 0; i < 8; i++) {
            sum += total[i] * (4.5 - (0.5 * i));
            totalCredit += total[i];
        }

        System.out.println((float) sum/totalCredit);

        sc.close();
    }
}
