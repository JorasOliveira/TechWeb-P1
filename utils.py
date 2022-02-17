from os import path
import json

def extract_route(s): #string
    return s.split()[1][1:]
    # split = s.split()
    # route = split[1]
    # return route[1:]

def read_file(p): #path
    with open(p, "rb") as b:
        return b.read()

def load_data(p): #path
    p = path.join("data/", p)
    with open(p) as j:
        return json.loads(j.read())

def load_template(p): #path
    p = path.join("templates/", p)
    print(p)
    with open(p) as f:
        return f.read()

def save_params(d): #dict of params
    return "lol"