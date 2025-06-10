import json

with open('owned_games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)

for game in games:
    print(game['name'])
