from app import app
from flask import render_template, request, jsonify
from app import translate
import requests
import sys
import json
import ast
from socket import error as SocketError
import errno

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/", methods=["POST"])
def scrambleConf():
    times = int(request.form['times'])
    text = request.form['toScramble']
    error = False
    try: 
        output_str, langs = translate.scraggle(times, text)
        raise SocketError
    except SocketError as e:
        error = True # Handle error here.
    # Combine the results into a string or any other format you prefer
    print(output_str)
    print(langs)
    # Return the result as JSON
    return jsonify({
        "original_text": text,
        "scrambled_output": output_str,
        "langs": langs, 
        "status": error
    })

