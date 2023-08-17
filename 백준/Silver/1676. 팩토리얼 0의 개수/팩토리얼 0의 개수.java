import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int temp = 0;
        Scanner in = new Scanner(System.in);
        int x = in.nextInt();

        for (int i = 1; i <= x; i++) {
            int num = i;
            while (num % 5 == 0) {
                temp++;
                num /= 5;
            }
        }

        System.out.println(temp);
    }
}
