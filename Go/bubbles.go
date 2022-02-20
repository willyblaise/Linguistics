package main

import (
	"fmt"
)



func BubbleSort(nums []int32 ) []int32 {

	n := len(nums)
	swapped := true


	for swapped {

		swapped = false
		for i := 0; i < n - 1 ; i++ {
			if nums[i] > nums[i + 1]{
				nums[i], nums[i + 1] = nums[i+1], nums[i]
				swapped = true
			}
		}
	}
	return nums
}

func main(){

	lst := []int32{ 221, 200, 190, 10, 1, 199, 17, 22 }

	fmt.Println("The list sorted is: ", BubbleSort(lst))
}
