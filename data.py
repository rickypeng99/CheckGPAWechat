# from tinydb import TinyDB, Query
# db = TinyDB('gpa.json')
# User = Query()
# print db.search(User.Subject == 'AAS')

import json

class Data():
    dataBase = list()
    def __init__(self):
        with open('data/gpa.json') as json_file:
            data = json.load(json_file)
            for p in data['Courses']:
                Data.dataBase.append(p)
    def printData():
        print dataBase[100]['Subject']
