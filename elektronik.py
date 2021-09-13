import pandas as pd
import requests
from bs4 import BeautifulSoup
from ftfy import fix_encoding


def init():
    global hours, d1, d2, d3, d4, d5, lista, lista_href

    # Lesson hours
    hours = []

    # Days
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d5 = []

    # CTR
    lista = []
    lista_href = []


# Scrapping - Scrap lesson table
def fetch_table(question):
    return pd.read_html("https://plan.elektronik.edu.pl/" + lista_href[lista.index(question)])


def scrap_table(plan):
    plan = plan[2].values.tolist()
    for i in plan:
        iter = 0
        for x in i:
            if iter == 0:
                pass
            if iter == 1:
                hours.append(x)
            if iter == 2:
                d1.append(x)
            if iter == 3:
                d2.append(x)
            if iter == 4:
                d3.append(x)
            if iter == 5:
                d4.append(x)
            if iter == 6:
                d5.append(x)
            iter = iter + 1


# Scrapping - Scrap CTR List
def fetch_list():
    return requests.get("https://plan.elektronik.edu.pl/lista.html")


def scrap_list(plan2):
    init()
    plan2 = BeautifulSoup(plan2.text, 'html.parser')
    plan2 = plan2.findAll('a')
    for i in plan2:
        lista_href.append(i.get('href'))
        lista.append(fix_encoding(i.get_text()))


# Outputs - List of Classes, Teachers and Rooms (links)
def href_list():
    scrap_list(fetch_list())
    return lista_href


# Outputs - List of Classes, Teachers and Rooms (pure text)
def text_list():
    scrap_list(fetch_list())
    return lista


def text2href(question):
    scrap_list(fetch_list())
    return lista_href[lista.index(question)]


# Outputs - Main query, returns data from lesson table
def query(question, data, out):
    init()
    output = []
    # Scrap CTR List
    try:
        scrap_list(fetch_list())
    except:
        print("Error connecting to the site !")
    # Scrap Class Table
    try:
        if out == "HTML":
            table = BeautifulSoup(requests.get("https://plan.elektronik.edu.pl/" + lista_href[lista.index(question)]).text, 'html.parser').findAll('table')[2]
            xd = table.findAll('a')
            num = 0
            for i in xd:
                del xd[num]['href']
                num = num + 1
            return str(table)
        else:
            scrap_table(fetch_table(question))
    except:
        print("Error connecting to the site !")
    if data == "all":
        return [hours, d1, d2, d3, d4, d5]
    if type(data) == list:
        for i in data:
            output.append(eval(i))
        return output
    else:
        return eval(data)
