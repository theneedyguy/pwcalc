#!/bin/bash
docker build . -t ckevi/pwcalc:latest
docker tag ckevi/pwcalc:latest ckevi/pwcalc:3.0.1-2-root
docker push ckevi/pwcalc:latest
docker push ckevi/pwcalc:3.0.1-2-root
