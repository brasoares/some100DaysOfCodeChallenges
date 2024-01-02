// Program to check an Armstrong Number

import java.util.Scanner;

public class ArmstrongNumber{ 
	public static void main(String[] args) {
		Scanner	scanner = new Scanner(System.in);
		System.out.print("Enter a number to check: ");
		int number = scanner.nextInt();
		scanner.close();	

				// Call method/class
		boolean isArmstrong = ArmstrongCalculator.isArmstrong(number);

		// Print the conclusion
		System.out.println("Is " + number + " an Armstrong number: " + isArmstrong + ".");
		}	
}
