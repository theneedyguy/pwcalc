#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import render_template
import docker
import hashlib
import base64
import re
import uuid

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    if request.form['alias'] != "" and request.form['secret'] != "":
        client = docker.from_env()
        container_uuid = "runner"+uuid.uuid4().hex

        alias = request.form['alias']
        secret = request.form['secret']
        response = client.containers.run("ckevi/pwcalc-runner",
            name=container_uuid,
            labels=[container_uuid],
            environment={"PWCALC_ALIAS": alias, "PWCALC_SECRET": secret})
        response_text = response.decode("UTF-8")
        client.containers.prune(filters={"label": container_uuid})
        return render_template("index.html", password = response_text)
    else:
        return render_template("index.html", password = "Not able to calculate with empty values.")
@app.route('/api')
def api(alias = "", secret = ""):
	alias = request.args.get('alias', alias)
    secret = request.args.get('secret', secret)
    client = docker.from_env()
    container_uuid = "runner"+uuid.uuid4().hex
    response = client.containers.run("ckevi/pwcalc-runner",
        name=container_uuid,
        labels=[container_uuid],
        environment={"PWCALC_ALIAS": alias, "PWCALC_SECRET": secret})
    response_text = response.decode("UTF-8")
    client.containers.prune(filters={"label": container_uuid})
    return response_text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3333)

