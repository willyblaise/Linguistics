package main

import (
	"fmt"
	"net/http"
)

func main() {

	http.HandleFunc("/", handler)
	http.HandleFunc("/champ", handler2)
	http.HandleFunc("/nicole", handler3)

	http.ListenAndServe(":8081", nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Println(w, "Root Point")
}

func handler2(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Two is Here!")
}

func handler3(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Number 3!")
}
