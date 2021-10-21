package main

import (
	"fmt"
	"math/rand"
	"time"
)

func init() {

	rand.Seed(time.Now().UnixNano())
}

func main() {

	//nums := make([]int, 6)
	nums := []int{}
	fmt.Println("Numbers for this run: ")
	for i := 0; i < 6; i++ {
		nums = append(nums, rand.Intn(100))
	}
	fmt.Println(nums)

	for i, v := range nums {

		fmt.Println(i+1, v)
	}
}
