import java.util.*;

public class Palindrome {

	static int rev(int n, int temp){
		if ( n == 0 ){
			return temp;
		}
		temp = (temp * 10) + (n % 10);

		return rev(n / 10, temp);
	}


	public static void main(String args[]){
		int n;
		Scanner sc = new Scanner(System.in);
		System.out.print("\nEnter number please: ");
		n = sc.nextInt();
		int temp = rev(n, 0);

		if (temp == n)
			System.out.print("Yes\n");
		else
			System.out.print("No\n");

	}
}
