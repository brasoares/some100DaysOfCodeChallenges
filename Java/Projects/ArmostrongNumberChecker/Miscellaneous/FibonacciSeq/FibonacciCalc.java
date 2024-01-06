public class FibonacciCalc {
    // Method to generate and display the sequence
    public void genAndDisplaySeq(int n) {
        for (int i = 0; i < n; i++) {
            int fiboNum = calcFibo(i);
            System.out.printf("Fibonacci number at index %d: %d%n", i, fiboNum);
        }
    }

    // This method actually calculates the Fibonacci sequence
    private int calcFibo(int index) {
        if (index <= 1) {
            return index;
        } else {
            int a = 0;
            int b = 1;
            int result = 0;
            for (int i = 2; i <= index; i++) {
                result = a + b;
                a = b;
                b = result;
            }
            return result;
        }
    }
}
