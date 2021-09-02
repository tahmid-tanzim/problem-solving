import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Grading {
    
    static void solve(int[] grades){
        int multiple;
        for(int i = 0; i < grades.length; i++) {
            if(grades[i] >= 38) {
                 multiple = 5 + (grades[i] / 5) * 5;
                if(multiple - grades[i] < 3) {
                 grades[i] = multiple;   
                }
            }
            System.out.println(grades[i]);
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] grades = new int[n];
        for(int grades_i=0; grades_i < n; grades_i++){
            grades[grades_i] = in.nextInt();
        }
        solve(grades);
    }
}
