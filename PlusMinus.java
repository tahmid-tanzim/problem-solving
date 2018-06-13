import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class PlusMinus {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), pos = 0, neg = 0, zero = 0, x;
       
        for(int r = 0; r < n; r++){
          x = in.nextInt();   
          if(x > 0) {
            pos++;
          } else if(x < 0) {
            neg++;
          } else {
              zero++;
          }
        }

        System.out.printf("%.6f\n", (float) pos/n);
        System.out.printf("%.6f\n", (float) neg/n);
        System.out.printf("%.6f\n", (float) zero/n);        
    }
}
