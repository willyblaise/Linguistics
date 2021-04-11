package main

import "fmt"

// We can define our own types using struct
type Rectangle struct{
	leftX float64
	TopY float64
	height float64
	width float64
}	

func main(){
	var name string = "Champ"
	name2 := "Nicole"

	fmt.Println("Hello", name2)
	fmt.Println("Hello", name)
	
	if name2 == "Nicol"{
		fmt.Println("The name is", name2)
	}else{
		fmt.Println("The name may be BG")
	}

	fmt.Println("The sum of all values is:",addUp(5,3,6))

	fam := [] string{"champ", "nicole","loga", "bray"}
	agg := [] float64{40, 38, 2, 17}

	for b, name := range fam {
		fmt.Println(b, name)
	}

	for i, age := range agg {
		fmt.Println(i, age)
	}

	fmt.Println("First person on the fam list is:", fam[0])

	ages := make(map[string] int)
	ages["Champ"] = 40
	ages["Nicole"] = 38
	fmt.Println(ages)
	fmt.Println("Length of ages map:", len(ages))

	for k, v := range ages {
		fmt.Println(k, v)	
       }	
	
       x := 25.67
       y := 32.22

       sum := add(x,y)
       fmt.Println("The sum of x and y is", sum)
       subtotal := 100.00
       total := salesTax(subtotal)
       fmt.Println("The total after taxes is:", total)

       pchange := percentChange(278, 283)
       fmt.Println("The percentage change here is:", pchange)

       mult := func(x int) int{
	     return  x * 4

       }

       fmt.Println("this is the lambda like function", mult(9))

       var fval int = 96
       var sval int = 0

       fmt.Println(fval, "divided by", sval, "=", safeDiv(fval, sval))

       // Define a rectangle
	rect1 := Rectangle{leftX: 0, TopY: 50, height: 10, width: 10}
 
	// Leave off attribute names if we know the order
	// rect1 := Rectangle{0, 50, 10, 10}
 
	// We access values with the dot operator
	fmt.Println("Rectangle is", rect1.width, "wide")
 
	// Call the method area for Rectangle
	fmt.Println("Area of the rectangle =", rect1.area())
 
}

func (rect *Rectangle) area() float64{
	return rect.height * rect.width
}

func addUp(args ...int) int{
	sum := 0

	for _, val := range args{
		sum += val
	}
	return sum
}
