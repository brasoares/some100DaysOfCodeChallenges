class ArmstrongCalculator{ // PascalCase
	public static boolean isArmstrong(int number){
		// variable declaration
		int temp = number;
			int digits = 0;

		while(temp>0){
		temp = temp/10;
		digits++;
		}
		temp = number;

		// calculation
		int sum = 0;
		while(temp>0){
			// gather the last digit
			int last = temp % 10;
			// calculates the power of a number up to max (n) times and add it to the sum variable
			sum += (Math.pow(last, digits));
			// removes the last one
			temp = temp/10;
		}	
		if(number==sum)
			return true;
		else return false;
	}
}
