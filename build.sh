#!/bin/bash
docker build . -t ckevi/pwcalc:latest
docker tag ckevi/pwcalc:latest ckevi/pwcalc:1.0
docker push ckevi/pwcalc:latest
docker push ckevi/pwcalc:1.0
