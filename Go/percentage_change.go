package main

import (
	"fmt"
	"time"
)


func main(){
	
	var currentValue float32
	var initialValue float32

	fmt.Printf("Please enter the current value: ")
	_, err := fmt.Scanf("%f", &currentValue)

	if err != nil {
		fmt.Println(err)
	}

	fmt.Printf("Please enter the initial value: ")
	_, err2 := fmt.Scanf("%f", &initialValue)

	if err2 != nil {
		fmt.Println(err2)
	}

	fmt.Printf("The percent change is: %.2f%%\n", percent_change(currentValue, initialValue))

	fmt.Println(time.Now())
}

func percent_change( cv float32, iv float32) float32 {
	return (cv - iv) / iv * 100

}

