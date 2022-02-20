package main


import (
	"fmt"
)


func main(){

	var k int

	cost := [] int{10,20,30,40,50,70,90}

	fmt.Println("Please enter the amount you have to spend: ")
	_, err := fmt.Scanf("%d", &k)

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(maxToys(cost, k))
}


func maxToys(cost []int, K int) int {
	
	sum := 0
	count := 0

	for _, v := range(cost){
		if sum + v <= K {
			sum  = sum + v
			count++
		}
	}
	return count
}
