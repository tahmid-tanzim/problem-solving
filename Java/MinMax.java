import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class MinMax {
    //256741038 623958417 467905213 714532089 938071625
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = 5, i = 0;
        long total = 0;
        long[] arr = new long[n];
        
        while(i < n) {
            arr[i] = in.nextLong();
            total += arr[i];
            i++;
        }
        
        i = 1;
        long max = total - arr[0], min = total - arr[0], diff;          
        while(i < n) {
            diff = total - arr[i];
            if(diff > max) {
                max = diff;
            }
            
            if(diff < min) {
                min = diff;
            }
            i++;
        }
        
        System.out.println(min + " " + max);
    }
}
