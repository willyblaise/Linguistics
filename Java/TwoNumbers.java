import java.util.*;

public class TwoNumbers {

	static int add(int a, int b){
		return a + b;
	}

	public static void main(String args[]){

		int a;
		int b;

		Scanner sc = new Scanner(System.in);

		System.out.print("Please enter first number: ");
		a = sc.nextInt();

		System.out.print("Please enter second number: ");
		b = sc.nextInt();

		int sum = add(a, b);

		System.out.print("The sum is: " + sum + "\n");
	}
}
