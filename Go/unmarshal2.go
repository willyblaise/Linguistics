package main

import (
	"encoding/json"
	"fmt"
)



type People struct {
	Name     string `json:"name"`
	Age      int    `json:"age"`
	Race     string `json:"race"`
}

func main(){

	jsonString := `{"name": "Bill Kapri", "age": 30, "race": "Black"}`

	var person People

	err2 := json.Unmarshal([]byte(jsonString), &person)
	if err2 != nil{
		fmt.Println(err2)
	}
	fmt.Printf("%+v", person)

}
