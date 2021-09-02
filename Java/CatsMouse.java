import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class CatsMouse {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int q = in.nextInt(), x, y, z, a, b, i;
        String[] output = new String[q];

        for(i = 0; i < q; i++) {
            x = in.nextInt();
            y = in.nextInt();
            z = in.nextInt();

            a = Math.abs(z - x);
            b = Math.abs(z - y);

            if(a < b) {
                output[i] = "Cat A";
            } else if(a > b) {
                output[i] = "Cat B";
            } else {
                output[i] = "Mouse C";
            }
        }

        for(i = 0; i < q; i++) {
            System.out.println(output[i]);
        }
    }
}
