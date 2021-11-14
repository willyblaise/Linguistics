package main

import "fmt"


func sales_tax(subtotal float64) float64 {
	return subtotal * 1.0825

}


func main(){

	var subtotal float64

	fmt.Println("Please provide the subtotal:")
	_, err := fmt.Scanf("%f", &subtotal)

	if err != nil {
		fmt.Println(err)
	}

	after_tax := sales_tax(subtotal)
	fmt.Printf("Your total after tax is: %f\n", after_tax)

}
