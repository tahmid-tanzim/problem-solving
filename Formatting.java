import java.util.Scanner;

public class Formatting {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String output = new String();
        for (int i = 0; i < 3; i++) {
            String s1 = sc.next();
            int x = sc.nextInt();
            output += String.format("%-15s", s1) + String.format("%03d", x) + "\n";
        }
        System.out.println("================================\n" + output + "================================");
    }
}
