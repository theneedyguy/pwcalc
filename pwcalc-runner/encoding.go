package main

import (
	"crypto/sha512"
	"bytes"
	"encoding/hex"
	"encoding/base64"
)

func createSHA(text string) string {
	hash := sha512.New()
	hash.Write([]byte(text))
	return hex.EncodeToString(hash.Sum(nil))
}

func createB64(hash string) string {
	encoded := base64.StdEncoding.EncodeToString([]byte(hash))
	return encoded
}

func combineStrings(alias string, secret string) string {
	valueArray := []string{alias, secret}
	var buffer bytes.Buffer
	for i := 1; i < len(valueArray); i++ {		
		buffer.WriteString(alias)
		buffer.WriteString(secret)
	}
	return buffer.String()
}
