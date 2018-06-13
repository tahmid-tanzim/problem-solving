import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class WeightedMean {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), i, numerator = 0, denominator = 0, temp;
        int x[] = new int[n];
        for(i = 0; i < n; i++){
            x[i] = in.nextInt();
        }
        for(i = 0; i < n; i++){
            temp = in.nextInt();
            numerator +=  x[i] * temp;
            denominator += temp;
        }
       
        System.out.printf("%.1f", (float) numerator / denominator);
    }
}
