import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class CamelCase {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        int l = s.length(), i, count = 1;
        for(i = 0; i < l - 1; i++) {
            if(Character.isUpperCase(s.charAt(i))) {
                count++;
            }
        }

        System.out.println(count);
    }
}
