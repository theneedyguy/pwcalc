# Pwcalc Runner

The Pwcalc Runner is written in Golang and generates a password from 2 values.
It combines the 2 and creates a SHA512 hash. The hash then gets converted to Base64 of which the first 16 characters get returned as the password.

## How it works

The runner expects 2 environment variables PWCALC_ALIAS and PWCALC_SECRET to create the password. You need to set the 2 values when you start the container. The password then gets written to the stdout. The container then exits and can be removed.

```shell
docker run -it ckevi/pwcalc-runner -e PWCALC_ALIAS='test' -e PWCALC_SECRET='test'
```


## Future plans

- Use a web listener instead of environment variables. (This might need some more testing. Also the runner would need to run in the same docker network as the main application to ensure communication)