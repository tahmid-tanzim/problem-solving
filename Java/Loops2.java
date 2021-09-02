import java.util.*;
import java.io.*;

public class Loops2 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt(), sum, i, j;
        int[][] output = new int[t][];
        for (i = 0; i < t; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            /* Process */
            output[i] = new int[n];
            sum = a + b * 1;
            output[i][0] = sum;
            for(j = 1; j < n; j++) {
                sum += b * Math.pow(2, j);
                output[i][j] = sum;
            }
        }
        in.close();

        /* Output */
        for (i = 0; i < t; i++) {
            for (j = 0; j < output[i].length; j++) {
                System.out.print(output[i][j] + " ");
            }
            System.out.print("\n");
        }
    }
}
