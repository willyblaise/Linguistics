package main

import (
	"fmt"
)


func main() {

	var pad float32
	var pof float32

	fmt.Println("Please enter the value after the discount applied: ")
	_, err := fmt.Scanf("%f", &pad)

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println("Please enter the percentage off: ")
	_, err2 := fmt.Scanf("%f", &pof)

	if err2 != nil {
		fmt.Println(err2)
	}

	fmt.Printf("The price before discount is: %.2f\n", priceBeforeDiscount(pad, pof))
}


func priceBeforeDiscount( currentPrice float32, percent float32) float32 {
	oneMinus := 1 - percent
	originalPrice := currentPrice/oneMinus
	return originalPrice
}
