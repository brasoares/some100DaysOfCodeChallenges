import java.util.Scanner;

public class FibonacciSeq {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.print("Enter the number of Fibonacci terms: ");
        int n = scan.nextInt();
        
        // Closing the scanner to avoid resource leak
        scan.close();
        
        // Call a method to perform the needed actions
        genAndDisplaySeq(n);
    }
}
