package main

import (
	"fmt"
	"os"
)

func main() {
	alias    := os.Getenv("PWCALC_ALIAS")
	secret   := os.Getenv("PWCALC_SECRET")
	password := combineStrings(alias, secret)
	fmt.Print(createB64(createSHA(password))[0:16])
}

