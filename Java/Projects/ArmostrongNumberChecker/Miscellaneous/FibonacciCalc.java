public class FibonacciCalc {
    // Method to create and display the seq
    public void genAndDisplaySeq(int n) {
        for (int i = 0; i < n; i++){
            int fiboNum = calcFibo(i);
            System.out.printf("Fibonacci number at index %d: %d%n", i, fiboNum);
        }

        System.out.println("The sequence of requested %d numbers: %d", n, genAndDisplaySeq)
    }
}
