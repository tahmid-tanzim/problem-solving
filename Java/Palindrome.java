import java.util.ArrayList;
import java.util.List;

public class Palindrome {

    private boolean isPalindrome(String s) {
        return true;
    }

    public static void main(String[] args) {
        ArrayList<String> validList = List.of("civic", "racecar", "02/02/2020");
        ArrayList<String> invalidList = List.of("swims", "mad", "wifi");
        Palindrome p = new Palindrome();
        System.out.println("Hello World - ");
        System.out.println(p.isPalindrome("AS"));
    }
}