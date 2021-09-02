import java.util.*;

public class BubbleSort {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), i = 0, temp, flag = n - 1, swap, c = 0;
        int container[] = new int[n];
        while(i < n) {
            container[i] = in.nextInt();
            i++;
        }

        while(flag > 0) {
            swap = 0;

            for(i = 0; i < flag; i++) {
                if(container[i] > container[i + 1]) {
                    temp = container[i];
                    container[i] = container[i + 1];
                    container[i + 1] = temp;
                    swap = i;
                    c++;
                    //System.out.println(Arrays.toString(container));
                }
            }
            flag = swap;
        }

        System.out.println("Array is sorted in "+ c +" swaps.");
        System.out.println("First Element: " + container[0]);
        System.out.println("Last Element: " + container[n-1]);
    }
}
