import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Day6 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String temp = "", odd = "", even = "";
        String[] container = new String[n];
        char c;
        
        for(int i = 0; i < n; i++) {
            temp = in.next();
            odd = "";
            even = "";
            for (int j = 0; j < temp.length(); j++) {
                c = temp.charAt(j);        
                
                 if ( j % 2 == 0 ) {
                     even += c;
                 } else {
                     odd += c;
                 }
            }
            container[i] = even + " " + odd;
        }
        
        for(int i = 0; i < n; i++) {
            System.out.println(container[i]);
        }
    }
}