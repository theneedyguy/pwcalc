#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import render_template
import docker
from conf import *
import hashlib
import base64
import re
import uuid
import requests
import json

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    if request.form['alias'] != "" and request.form['secret'] != "":
        alias = request.form['alias']
        secret = request.form['secret']
        pwcalc_runner = getConfigValue("runner-container")
        print(pwcalc_runner)
        URL = "http://"+pwcalc_runner+"/calc"
        PARAMS = {'alias': alias, 'secret': secret}
        r = requests.post(url = URL, params = PARAMS)
        return render_template("index.html", password = json.loads(r.text)["Password"])
    else:
        return render_template("index.html", password = "Not able to calculate with empty values.")

@app.route('/api')
def api(alias = "", secret = ""):
    alias = request.args.get('alias', alias)
    secret = request.args.get('secret', secret)
    pwcalc_runner = getConfigValue("runner-container")
    URL = "http://"+pwcalc_runner+"/calc"
    PARAMS = {'alias': alias, 'secret': secret}
    r = requests.post(url = URL, params = PARAMS)
    return json.loads(r.text)["Password"]

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3333)

