package main

import (
	"fmt"
	"net/http"
	"log"
	"github.com/gorilla/mux"
)

func main() {
	router := mux.NewRouter().StrictSlash(true)
    router.HandleFunc("/{alias}/{secret}", Index)
	log.Fatal(http.ListenAndServe(":8787", router))
}

func Index(w http.ResponseWriter, r *http.Request){
	vars := mux.Vars(r)
	alias := vars["alias"]
	secret := vars["secret"]
	password := combineStrings(alias, secret)
	fmt.Fprintln(w, createB64(createSHA(password))[0:16])
}