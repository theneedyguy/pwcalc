# Pwcalc Runner

The Pwcalc Runner is written in Golang and generates a password from 2 values.
It combines the 2 and creates a SHA512 hash. The hash then gets converted to Base64 of which the first 16 characters get returned as the password.

## How it works

The runner listens on port 1099 and expects 2 parameters via post request. It then calculates a password out of the 2 values and exposes it as a json value. The main app then reads the result back to the user.


