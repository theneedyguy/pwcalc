FROM python:3.6
RUN mkdir -p /opt/pwcalc

COPY ./app.py /opt/pwcalc/
COPY ./requirements.txt /opt/pwcalc/
COPY ./templates /opt/pwcalc/templates

RUN pip install -r /opt/pwcalc/requirements.txt

#USER nobody
WORKDIR /opt/pwcalc

EXPOSE 3333

ENTRYPOINT ["python3", "app.py"]
