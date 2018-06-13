import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class BonAppetit {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt(), i, b_charged, b_actual, sum=0;
        int [] c = new int[n];
        for(i = 0; i < n; i++){
            c[i] = in.nextInt();
            sum += c[i];
        }
        b_charged = in.nextInt();
        b_actual = (sum - c[k]) / 2;
        System.out.println(b_charged == b_actual ? "Bon Appetit" : b_charged - b_actual);
    }
}
