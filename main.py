import requests
import json
import csv
import os
from config import config
import pandas as pd
apikey=config.api_key
# try:
def getRecipeByIngredients(Ingredients):
    payload = {
        'fillIngredients': False,
        'ingredients': Ingredients,
        'limitLicense': False,
        'number': 2,# can be changed according to required number of receipe we are getting only receipe for now
        'ranking': 1 # ranking is done by system , I am unknown about the ranking
    }
    endpoint="https://api.spoonacular.com/recipes/findByIngredients"
    headers = {
        'x-api-key': apikey
                }
    try:

        observation= requests.get(endpoint, params=payload, headers=headers)
        observation = observation.json()
        if len(observation) > 0:
            config.add_ingredient(Ingredients)
            return observation
        else:
            pass
    except:
        print("Provide ingredient is not in our any receipe")

input1=input("search the receipe by single ingredient:")

with open('.\config\Ingredients.txt', 'r+') as f:
    first = f.read()
    list123=list(first.split(","))

list456=list(input1.split(","))

for i in list456:
    if i in list123:
        print("The ingredient is already in the csv file please look for csv file that is",i)
        pass
    else:
        inputforjson=getRecipeByIngredients(i)
                # # aheley testing ko lagi matra function nabhanako
        # # def json_creator():
        data = inputforjson
        s=json.dumps(data)
        with open(".\jsonfiles\data1.json",'w') as f:
            f.write(s)
            #
        # # converting json to csv
        df = pd.read_json (r'.\jsonfiles\data1.json')
        # df.to_csv (r'Path where the new CSV file will be stored\New File Name.csv', index = None)
        df.to_csv (r'.\csvfiles\data1.csv', index = None)


        # yo comment gareko method ley header lai skip chai garyo tara sabai row lekhna safal bhayena
        # file = open('.\csvfiles\data1.csv')
        # csv_reader = csv.reader(file)
        # next(csv_reader)
        # dc=pd.read_csv(file)
        # print(dc)
        # with open(".\csvfiles\data2.csv",'a',newline="") as f:
        #     writer = csv.writer(f)
        #     writer.writerow(dc)

        with open(".\csvfiles\data1.csv", "r") as f1, open(".\csvfiles\Final.csv", "a") as f2 :
            line = f1.readline() #remove header
            line = f1.readline()
            while line != "" :
                f2.write(line)
                line = f1.readline()
                print(line)

        os.remove('.\csvfiles\data1.csv')# deleting the read file as we need to make only one csv as required