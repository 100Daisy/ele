from flask import Flask
from flask_cors import CORS

import pandas as pd
from ftfy import fix_encoding
import elektronik

app = Flask(__name__)
CORS(app)

@app.route("/html/<question>")
def hello_world(question):
    return fix_encoding(elektronik.query(str(question).upper(), "all", "HTML"))

@app.route("/html/<question>/<theme>")
def hello_world2(question, theme):
    theme = '<style>' + open("themes/" + theme + ".css", "r").read() + '</style>'
    plan = fix_encoding(elektronik.query(str(question).upper(), "all", "HTML"))
    return theme + plan

@app.route("/html/ctr/href")
def ctr():
    n = -1
    f = ""
    x = elektronik.href_list()
    y = elektronik.text_list()
    for i in x:
        n = n + 1
        f += '<a href="https://plan.elektronik.edu.pl/' + i + '">' + y[n] + '</a><br>'
    return f

@app.route("/html/ctr/<onclick>")
def ctr2(onclick):
    n = -1
    f = ""
    x = elektronik.href_list()
    y = elektronik.text_list()
    for i in x:
        n = n + 1
        f += '<li><a onclick="' + onclick + '(' + "'" + y[n].lower() + "'" + ')">' + y[n] + '</a><br></li>'
    return f

@app.route("/list")
def list():
    return str(elektronik.text_list())

@app.route("/list_href")
def href_list():
    return str(elektronik.href_list())

@app.route("/")
def debug():

    return '<a href="/list_href">Lista linków do planów (HREF)</a><br>' \
           '<a href="/list">Lista linków do planów (Nazwy)</a><br>' \
           '<a href="/html/ctr/href">Lista linków do planów (Linki)</a><br>' \
           '' \
           ''
