import requests
import json
import csv
from config import config
import pandas as pd
apikey=config.api_key
try:
    def getRecipeByIngredients(Ingredients):
        payload = {
            'fillIngredients': False,
            'ingredients': Ingredients,
            'limitLicense': False,
            'number': 2,
            'ranking': 1
        }
        endpoint="https://api.spoonacular.com/recipes/findByIngredients"
        headers = {
            'x-api-key': apikey
                    }
        observation= requests.get(endpoint, params=payload, headers=headers)
        observation = observation.json()
        print(observation)
        config.add_ingredient(Ingredients)
        return observation
except:
    print("Provide ingredient is not in our any receipe")
input1=input("search the receipe by single ingredient:")
inputforjson=getRecipeByIngredients(input1)

# # aheley testing ko lagi matra function nabhanako
# # def json_creator():
data = inputforjson
s=json.dumps(data)
with open(".\jsonfiles\data1.json",'w') as f:
    f.write(s)
    #
# # converting json to csv
df = pd.read_json (r'.\jsonfiles\data1.json')
df.to_csv (r'.\csvfiles\data1.csv', index = None)
#
# # df.to_csv (r'Path where the new CSV file will be stored\New File Name.csv', index = None)
dc = pd.read_csv (r'.\csvfiles\data1.csv')

#
with open(".\csvfiles\data2.csv",'a',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(dc)



