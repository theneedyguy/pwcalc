#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import render_template
import docker
import hashlib
import base64
import re
import uuid


def generatePassword(alias, secret, length):
    plainPassword = alias + secret
    sha1Password = hashlib.sha512(plainPassword.strip().encode("UTF-8"))
    b64Password = base64.b64encode(bytearray(sha1Password.hexdigest(),"UTF-8"))
    return b64Password[:length].decode("UTF-8")

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
def api(alias = "", secret = "", size = 16):
    alias = request.args.get('alias', alias)
    secret = request.args.get('secret', secret)
    size = request.args.get('size', size)
    pw = generatePassword(alias, secret, int(size))
    return pw

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3333)

