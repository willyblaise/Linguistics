package main


import (
	"fmt"
	"encoding/json"
)

type Person struct {

	FirstName string `json:"firstName"`
	LastName  string `json:"lastName"`
	Age       int    `json:"age"`

}


func main(){

	pone := Person{ "Sherlock", "Holmes", 31}

	poneString, err := json.Marshal(pone)

	if err != nil {

		fmt.Println(err)
	}

	fmt.Printf("%s", string(poneString))

}
