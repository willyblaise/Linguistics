package main

import(
	"fmt"
	"encoding/json"
)


type Keyboards struct {

	Brand  string `json:"brand"`
	Model  string `json:"model"`
	Color  string `json:"color"`
	Weight string `json:"weight"`
}

func main(){

	var kbOne Keyboards

	jsonString := `{"brand":"Glorious", "model":"GMMK Pro", "color":"whiite ice", "weight":"3lb"}`

	err := json.Unmarshal([]byte(jsonString), &kbOne)

	if err != nil {
		fmt.Println(err)
	}

	fmt.Printf("%+v", kbOne)

}
