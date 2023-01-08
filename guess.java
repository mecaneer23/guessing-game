import java.util.Scanner;

public class guess {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = Math.floor(Math.random() * 99) + 1;
        int answer;
        int tries = 0;
        while (True) {
            System.out.println("Guess a number between 1 and 100");
            answer = scan.nextInt();
            tries++;
            if (answer > num) {
                System.out.println("Too high!");
            } else if (answer < num) {
                System.out.println("too low!");
            } else {
                System.out.println("You got it! It took you " + tries + " tries!");
                break;
            }
        }
        scan.close();
    }
}
