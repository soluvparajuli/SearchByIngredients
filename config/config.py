api_key="3b7173107d9643a5bd00c244ea1817de"

def add_ingredient(ingre):

    with open('.\config\Ingredients.txt', 'r+') as f:
        first = f.read()
    listRes = list(first.split(","))
    if ingre in listRes:
        print("Ingredient is already present  in ingredient_list so  check csv file.")
    else:
        with open('.\config\Ingredients.txt', 'r+') as f:
            first = f.read()
            if not first:
                f.write(ingre)
            else:
                f.write("," + ingre)
            print("Previous Ingredient",first)
            listRes = list(first.split(","))
            print("In list of ingredient previous")
            print(listRes)




