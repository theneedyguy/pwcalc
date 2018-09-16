package main

import (
	"encoding/json"
	"io"
	"net/http"
)

type response struct {
	Password string
}

func paramHandler(res http.ResponseWriter, req *http.Request) {
	if req.Method != "POST" {
		a := &response{"ERROR"}
		out, err := json.Marshal(a)
		if err != nil {
			panic(err)
		}
		io.WriteString(res, string(out))

	} else {
		alias := req.FormValue("alias")
		secret := req.FormValue("secret")
		password := combineStrings(alias, secret)

		a := &response{createB64(createSHA(password))[0:16]}
		out, err := json.Marshal(a)
		if err != nil {
			panic(err)
		}

		io.WriteString(res, string(out))
	}

}

func main() {
	http.HandleFunc("/calc", func(res http.ResponseWriter, req *http.Request) {
		res.Header().Set("Content-Type", "application/json")
		paramHandler(res, req)
	})
	http.ListenAndServe(":1099", nil)
}
