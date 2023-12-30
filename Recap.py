print("nico".upper())
print("nico".endswith("a"))
#list
numbers = [5,3,1,5,7,3,"True",True]
print(numbers)
numbers.append(["🥨🥨","🥪"])
print(numbers)
#Tupple
numbers = (1,2,3,4,5,True,"false")
#dictionery
player = {
    "name":"nico",
    "age": 12,
    "alive": True,
    "fav_food": ("🥨","🥔"),
    "friend":{
        "name":"lynn",
        "fav_food": ["🥔"]
    }
}

print(player["friend"]["fav_food"])
player['fav_food'] = "🍹"
player.pop("alive")
player['friend']
['fav_food'].append("🍬")

print(player)