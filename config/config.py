api_key="3b7173107d9643a5bd00c244ea1817de"

def add_ingredient(ingre):
    with open('.\config\Ingredients.txt', 'r+') as f:
        first = f.read()
        if not first:
            f.write(ingre)
        else:
            f.write("," + ingre)
        print(first)
        listRes = list(first.split(","))
        print(listRes)




