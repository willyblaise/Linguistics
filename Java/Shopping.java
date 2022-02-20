import java.util.*;
import java.io.*;

public class Shopping {

	static int maxToys(List<Integer> cost, int k){

		int sum = 0;
		int count = 0;

		for (int c : cost) {
			if (sum + c <= k){
				sum += c;
				count++;
			}

		}
		cost.forEach( name ->
			System.out.println("$" + name));


		return count;
	}

	public static void main(String args[]){
		List<Integer> cost = Arrays.asList(10, 12, 15, 20, 25, 30, 40, 50, 21, 17);
		cost.sort(null);
		System.out.print(cost + "\n");
		int k = 100;

		System.out.print("You can buy " + maxToys(cost, k) + " Toys with $" + k +"\n");
	}

}
