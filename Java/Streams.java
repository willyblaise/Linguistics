import java.util.*;


public class Streams {

	public static void main(String[] args) {

		List<Integer> nums = Arrays.asList(1,2,3,4,5);
		List<String> words = Arrays.asList("Pearl", "is", "a", "Neat", "Baby");

		nums.stream().map(num -> num * 2).forEach(System.out::println);
		words.stream().forEach(System.out::println);
	}

}
