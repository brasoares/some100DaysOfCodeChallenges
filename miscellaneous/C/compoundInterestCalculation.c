#include <stdio.h>
#include <math.h>

// Compound Interest = Principal * (1 + (Rate / 100))^Time

int main() {
	double principal, time, rate;

	printf("Enter Principal (amount): ");
	scanf("%lf", &principal);

	printf("Enter the time span: ");
	scanf("%lf", &time);

	printf("Enter the rate: ");
	scanf("%lf", &rate);

	double rightHalf = pow(1 + (rate / 100), time);

	double compoundInterest = principal * rightHalf;

	printf("Compound Interest: %.2lf\n", compoundInterest);

	return 0;
}
