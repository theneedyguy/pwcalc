#!/bin/bash
docker build . -t ckevi/pwcalc:latest
docker tag ckevi/pwcalc:latest ckevi/pwcalc:2.1-root
docker push ckevi/pwcalc:latest
docker push ckevi/pwcalc:2.1-root
