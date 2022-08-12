import requests
import json
import csv
from config import config
import pandas as pd
apikey=config.api_key

# searching the receipe by ingredient
Ingredient=input("Enter the ingredient to search the receipe")
config.add_ingredient(Ingredient)
print(config.Ingredients)

url="https://api.spoonacular.com/recipes/findByIngredients?ingredients="+Ingredient+ "&number=1&apiKey=" + apikey
observation= requests.get(url)
print(observation.json())

# aheley testing ko lagi matra function nabhanako
# def json_creator():
data = observation.json()
s=json.dumps(data)
with open(".\jsonfiles\data1.json",'w') as f:
    f.write(s)

# converting json to csv
df = pd.read_json (r'.\jsonfiles\data1.json')
df.to_csv (r'.\csvfiles\data1.csv', index = None)

# df.to_csv (r'Path where the new CSV file will be stored\New File Name.csv', index = None)

dc = pd.read_csv (r'.\csvfiles\data1.csv')
with open(".\csvfiles\data2.csv",'a',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(dc)


