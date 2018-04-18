# Pwcalc

PwCalc is an app built with Flask to generate passwords.

## How it works

The app combines 2 strings and generates a SHA512 hash. The hash then gets converted to a BASE64 string of which only the first 16 characters are used.

## Architecture

The application is containerized and runs on Port 3333 to where the user connects via his webbrowser. You need to mount the Docker UNIX-Socket to the container in order for it to work.

See more Info in the chapter **Container versions**.

### Main application

The main application is written in Python and uses Flask for the web interface and the Docker API to make requests to the Docker Engine.

The user sends two values via a form to the back-end. The application then calls the Docker API to create a runner. The values get passed to the runner. When the runner finishes its work the application deletes it.

### Runner

The runner is written in Golang and generates a "password" from the two values it gets from the web interface. It exposes the password in its output where the main application can read it and pass it back to the user. The runner itself is a container too.

## Container versions

- ckevi/pwcalc:1.0 : This version doesn't use a runner. Instead it does all the work in the same application. This is generally faster. Also the container does not run as root. This version can also be run in Kubernetes and OpenShift since it doesn't rely on the Docker API.

- ckevi/pwcalc:2.2-root : This version uses the runner (ckevi/pwcalc-runner) to create the password. It must run as root since the Docker UNIX-Socket can only be accessed by a root user in the container.