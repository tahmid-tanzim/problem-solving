import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class TwoDArray {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = 6, max = 0, sum = 0, r, c;
        int arr[][] = new int[n][n];

        for(r = 0; r < n; r++) {
            for(c = 0; c < n; c++){
                arr[r][c] = in.nextInt();
            }
        }
        in.close();

        for(r = 1; r < n - 1; r++) {
            for(c = 1; c < n - 1; c++){
                sum = 0;
                sum += arr[r][c];
                for(int c0 = -1; c0 <= 1; c0++) {
                    for(int r0 = -1; r0 <= 1; r0 += 2) {
                        sum += arr[r + r0][c + c0];
                    }
                }
                if(sum > max || (r == 1 && c == 1)) {
                    max = sum;
                }
            }
        }

        System.out.println(max);
    }
}

/*
0 -4 -6 0 -7 -6
-1 -2 -6 -8 -3 -1
-8 -4 -2 -8 -8 -6
-3 -1 -2 -5 -7 -4
-3 -5 -3 -6 -6 -6
-3 -6 0 -8 -6 -7
*/

// -19