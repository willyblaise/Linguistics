package main

import (
	"fmt"
	"math"
)


func main(){

	var presentValue float64
	var rate	 float64
	var timeframe    float64

	fmt.Println("Please input Present Value: ")
	_, err := fmt.Scanf("%f", &presentValue)

	if err != nil {
		fmt.Println(err)
	}


	fmt.Println("Please input rate Value: ")
	_, err2 := fmt.Scanf("%f", &rate)

	if err2 != nil {
		fmt.Println(err2)
	}


	fmt.Println("Please input timeframe: ")
	_, err3 := fmt.Scanf("%f", &timeframe)

	if err3 != nil {
		fmt.Println(err3)
	}

	futVal := fValue(presentValue, rate, timeframe)
	fmt.Printf("The Future Value should be: %.2f\n", futVal)
	fmt.Printf("The Present Value should be: %.2f", pValue(futVal, rate, timeframe))

}

func fValue(pValue float64, ir float64, tf float64) float64 {

	fvalue := pValue * math.Pow(1+ir, tf)
	return fvalue
}

func pValue(fValue float64, ir float64, tf float64) float64 {

	denominator := math.Pow(1+ir, tf)
	pvalue := fValue/denominator
	return pvalue
}
