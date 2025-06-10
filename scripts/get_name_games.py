import json

with open('owned_games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)

seen = set()
for game in games:
    name = game['name']
    if name not in seen:
        print(name)
        seen.add(name)
