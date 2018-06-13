import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class BreakingRecords {
    

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), i, s;

        int [][] high = new int[1][2], low = new int[1][2];
        for(i = 0; i < n; i++){
            s = in.nextInt();

            if(i == 0) {
                high[0][0] = low[0][0] = s;
            } else {
            
                if (s > high[0][0]) {
                    high[0][0] = s;
                    high[0][1]++;
                }

                if (s < low[0][0]) {
                    low[0][0] = s;
                    low[0][1]++;
                }   
            }
        }

        System.out.println(high[0][1] + " " + low[0][1]);
    }
}
