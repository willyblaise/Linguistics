package main

import "fmt"

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

}


func addUp(args ...int) int{
	sum := 0

	for _, val := range args{
		sum += val
	}
	return sum
}
