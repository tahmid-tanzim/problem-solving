import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Diagonal {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[][] val = new int[n][n];

        for(int r = 0; r < n; r++){
            for(int c = 0; c < n; c++){
                val[r][c] = in.nextInt();
            }   
        }

        int x = 0, y = 0;
        for(int c = 0; c < n; c++){
            y += val[0 + c][c];
            x += val[n - 1 - c][c];
        }  
        System.out.println(Math.abs(y - x));        
    }
}
