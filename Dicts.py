player = {
    'name' : 'nico',
    'age' : 12,
    'alive' : True,
    'fav_food' : ["🥪","🥨"]
}
#dictionery 는 수정 가능함
print(player.get('age'))
player.pop('age')
print(player)
player['xp'] = 1500
print(player)
player['fav_food'].append("🥔")
print(player.get('fav_food'))