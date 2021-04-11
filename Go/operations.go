package main

import "fmt"

func add(x float64, y float64) float64 {
	return x + y
}

func salesTax(x float64) float64 {
	return x * 1.0825
}

func percentChange(currentValue float64, initialValue float64) float64 {
	pc := ((currentValue - initialValue)/initialValue) * 100
	
	return pc
}

func safeDiv(num1, num2 int) int {
    defer func() {
        fmt.Println(recover())
    }()
    solution := num1 / num2
    return solution
}


