package main

import (
	"fmt"
	"log"
	"encoding/json"
	"io/ioutil"
	"net/http"
	"github.com/gorilla/mux"
)

type People struct {

	Id        string `json:"id"`
	FirstName string `json: "fname"`
	LastName  string `json: "lname"`
	Age       int    `json: "age"`
}

func homepage(w http.ResponseWriter, r *http.Request){
	fmt.Fprintf(w, "Welcome to this API.")
	fmt.Println("Endpoint was hit")
}

func allPeople(w http.ResponseWriter, r *http.Request){
	fmt.Println("Endpoint was hit")
	json.NewEncoder(w).Encode(people)
}

func instanceOfPeople(w http.ResponseWriter, r *http.Request){
	vars := mux.Vars(r)
	key  := vars["id"]
//	fmt.Fprintf(w, "Key: " + key)
	for _, person := range people{
		if person.Id == key{
			json.NewEncoder(w).Encode(person)
		}
	}
}

func createPeople(w http.ResponseWriter, r *http.Request){
	reqBody, _ := ioutil.ReadAll(r.Body)
	var newPerson People
	json.Unmarshal(reqBody, &newPerson)
	people = append(people, newPerson)
	json.NewEncoder(w).Encode(newPerson)

}

func handleRequests(){

	myRouter := mux.NewRouter().StrictSlash(true)

	myRouter.HandleFunc("/", homepage)
	myRouter.HandleFunc("/people", allPeople)
	myRouter.HandleFunc("/people/{id}", instanceOfPeople)
	myRouter.HandleFunc("/peoples/", createPeople)
	log.Fatal(http.ListenAndServe(":10000", myRouter))
}

var people []People

func main(){

	people = [] People{
		People{"1", "Chance", "Fisk", 31},
		People{"2", "Esther", "Fisk", 29},
		People{"3", "Loga", "Fisk", 2},
		People{"4", "Brill", "Crenshaw", 18},
	}

	handleRequests()

}
