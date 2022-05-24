package main

import(
	"fmt"
)        



func main(){

	var amt float32
	var percentage float32

	fmt.Println("Please enter the amount you would like invested: ")
	_, err := fmt.Scanf("%f", &amt)
	
	if err != nil {
		fmt.Println(err)

	}

	fmt.Println("Please enter the percentage of the company in return for the investment: ")
	_, err2 := fmt.Scanf("%f", &percentage)
	
	if err2 != nil {
		fmt.Println(err2)
	}

	percentOwnership := percentOf(amt, percentage)
	
	fmt.Printf("The valuation of the company at this amount is: $%.2f\n", percentOwnership)

}

func percentOf( amount float32, percent float32) float32 {

	return amount / percent
}
