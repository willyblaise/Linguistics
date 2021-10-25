package main


import (
	"fmt"
	"math"
)


type Shape interface {
	area() float64
}

type Rectangle struct {
	length float64
	height float64
	shape  string
}

type Circle struct {
	radius float64
	shape  string
}



func (rect Rectangle) area() float64 {
	return rect.length * rect.height
}

func (circ Circle) area() float64 {
	return math.Pi * math.Pow(circ.radius, 2)
}

func measure(shape Shape) {
	fmt.Println(shape)
	fmt.Println(shape.area())
}

func main(){
	r := Rectangle{10,10, "rectangle"}
	c := Circle{100, "circle"}

	measure(r)
	measure(c)
}
