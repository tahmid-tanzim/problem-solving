import java.util.*;
import java.math.*;

public class ExtraLongFactorials {

    public static BigInteger factorial(BigInteger n) {
        BigInteger one = new BigInteger("1");
        if(n.equals(one)) {
            return one;
        } else {
            return n.multiply(factorial(n.subtract(one)));
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BigInteger n = in.nextBigInteger();
        in.close();
        System.out.println(factorial(n));
    }
}
