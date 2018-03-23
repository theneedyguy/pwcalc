#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import render_template
import hashlib
import base64
import re


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
		alias = request.form['alias']
		secret = request.form['secret']
		pw = generatePassword(alias, secret, 16)
		return render_template("index.html", password = pw)
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

