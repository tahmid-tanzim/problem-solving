public class Test {
    public static void main(String[] args) {
        System.out.println("Hello World");
        int[] array = new int[10];
        Random rand = new Random();

        for (int i = 0; i < array.length; i++)
            array[i] = rand.nextInt(100) + 1;

        Arrays.sort(array);
        System.out.println(Arrays.toString(array));s
    }
}