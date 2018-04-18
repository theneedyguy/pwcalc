#!/bin/bash
CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o pwcalc .
sudo docker build . -t ckevi/pwcalc-runner:latest
sudo docker tag ckevi/pwcalc-runner:latest ckevi/pwcalc-runner:1.0
sudo docker push ckevi/pwcalc-runner:latest
sudo docker push ckevi/pwcalc-runner:1.0

