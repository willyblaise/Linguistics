import java.util.*;

import javax.lang.model.util.ElementScanner6;

public class Medium {

    public static void main(String[] args) {
        //int[] nums = {100,2,38,10,20,30,40,50};
        int[] nums = {51,38,10,20,30,40,50};

        Arrays.sort(nums);

        for ( int i : nums) {
            System.out.println(i);
        }
        double median;

        if(nums.length % 2 == 0) {
           median = (double) (nums[nums.length/2] + nums[nums.length/2-1])/2;
        } else {
            median = (double) nums[nums.length/2];
        }

        System.out.println("Current array: " + Arrays.toString(nums));
        System.out.println("Median is: " + median);
    }

}
