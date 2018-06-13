import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class TimeConvert {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String n =  in.next();
        
        String ap = n.substring(8);
        String[] time = n.substring(0, 8).split(":");     
       
       //System.out.println(Arrays.toString(time)); 

       int hour = Integer.parseInt(time[0]);
       //System.out.println("B4: " + hour + ap); 
        if(ap.equals("AM")  && hour == 12) {
             hour = 0; 
        } else if(ap.equals("PM") && hour < 12) {
           hour += 12;
        }

       //System.out.println("Aftr: " + hour + ap); 

       time[0] = String.format("%02d", hour);
       System.out.println(time[0] + ":" + time[1] + ":" + time[2]);
    }
}
