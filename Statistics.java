import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Statistics {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), 
            sum = 0,
            index = n/2;
        int x[] = new int[n];
        int[][] frequency = new int[n][2]; // row number; column = frequency
        float median;
        for(int i = 0; i < n; i++){
            x[i] = in.nextInt();
            sum += x[i];
        }
        
        Arrays.sort(x);
        
        if(n % 2 == 0) {
            median = (float) (x[index] + x[index - 1]) / 2;
        } else {
            median = (float) x[index] / 2;
        }
      
        int flag = 0, count = 1, mode = x[0];
        for(int i = 0; i < n; i++) {
            if(x[i] == frequency[flag][0]) {
                frequency[flag][1] += 1;
            } else if (flag == 0 && i == 0) {
                frequency[flag][0] = x[i];
                frequency[flag][1] += 1;
            } else {
                flag++;
                frequency[flag][0] = x[i];
                frequency[flag][1] += 1;    
            }
            
            if(frequency[flag][1] > count) {
                count = frequency[flag][1];
                mode = frequency[flag][0];
            }
        }

        System.out.println((float) sum / n);
        System.out.println(median);
        System.out.println(mode);
    }
}
