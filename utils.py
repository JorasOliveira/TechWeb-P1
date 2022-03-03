from email import header
from encodings import utf_8
from os import path
import json
from urllib import response

from numpy import identity

def extract_route(s): #string
    return s.split()[1][1:]
    # split = s.split()
    # route = split[1]
    # return route[1:]

def read_file(p): #path
    with open(p, "rb") as b:
        return b.read()

def load_data(fN): #path
    p = path.join("data/", fN)
    with open(p) as j:
        return json.loads(j.read())

def load_template(fN): #fileName
    p = path.join("templates/", fN)
    with open(p) as f:
        return f.read()

def save_params(d): #dict of params
    with open ("data/note.json", "r", encoding=utf_8) as file:
        data = json.load(file)
    data.append(d)

    with open ("data/note.json", "w", encoding=utf_8) as file:
        json.dump(data, file, ensure_ascii=False, ident = 4)

def build_response(body = '', code = 200, reason = 'ok', headers = ''): 
    #se chama a funcao vazia, os valores usados sao os expecificados aqui, porem pode chamar declarando os valores
    #entao a funcao usa os valores declarados como override dos padroes
    response = f'HTTP/1.1 {code} {reason}' #fstring
    if headers:
        response +=  f'\n{header}'

    response += f'\n\n{body}'

    return(response.encode())
 