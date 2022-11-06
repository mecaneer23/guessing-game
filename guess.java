import java.util.Scanner;

public class guess {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        boolean won = false;
        // int num = (int) Math.random() * 100;
        int num = 50;
        while (won == false) {
            System.out.println("Guess a number between 1 and 100");
            int answer = scan.nextInt();
            if (answer > num) {
                System.out.println("too high");
            } else if (answer < num) {
                System.out.println("too low");
            } else {
                System.out.println("equal");
                won = true;
            }
        }
        scan.close();
    }
}