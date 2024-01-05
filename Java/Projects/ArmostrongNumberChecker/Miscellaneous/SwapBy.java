// Basic numbers swap.
import java.util.*;

public SwapBy {
  public static void main(String[] args){
    // Scanner object to read from the user
    Scanner scanner = new Scanner(System.in);

    // Prompt for the user to provide the first integer
    System.out.print("Enter the first number: ")
    int firstInte = scanner.nextInt();
    // Prompt for the user to provide the second integer
    System.out.print("Enter the second number (different from the previous one): ")
    int secondInte = scanner.nextInt();

    scanner.close();

    // Swap
    int swapVar = firstInte;
    firstInt = secondInte;
    secondInte = swapVar;

    System.out.print("The swapped numbers are: first: %d and second: %d.", firstInte, secondInte);    
  }
}
