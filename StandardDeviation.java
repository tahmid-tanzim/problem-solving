import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class StandardDeviation {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), i;
        float sum = 0, x[] = new float[n];
        for(i = 0; i < n; i++){
            x[i] = in.nextInt();
            sum += x[i];
        }
        
        float mean = sum / n;
        sum = 0;
        
         for(i = 0; i < n; i++){
            sum += Math.pow(x[i] - mean, 2);
         }
       
        System.out.printf("%.1f", Math.sqrt(sum/n));
    }
}
