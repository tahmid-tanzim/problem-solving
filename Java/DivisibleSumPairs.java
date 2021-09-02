import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class DivisibleSumPairs {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt(), i, j, count = 0;
        int [] a = new int[n];
        for(i = 0; i < n; i++){
            a[i] = in.nextInt();
        }

        for(i = 0; i < n; i++) {
            for(j = i + 1; j < n; j++) {
                if((a[i] + a[j]) % k == 0) {
                    count++;
                     // System.out.println("(" + i + ", " + j + ")");
                }
            }
        }
        System.out.println(count);
    }
}
