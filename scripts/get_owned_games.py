import requests

def get_owned_games(api_key, steamid):
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        'key': api_key,
        'steamid': steamid,
        'include_appinfo': 1,
        'include_played_free_games': 1
    }
    resp = requests.get(url, params=params)
    try:
        data = resp.json()
    except Exception as e:
        print("Error decoding JSON response!")
        print("Status code:", resp.status_code)
        print("Response received:")
        print(resp.text)
        raise e
    games = data.get('response', {}).get('games', [])
    return games

if __name__ == "__main__":
    api_key = input("Your Steam API KEY: ").strip()
    steamid = input("Your SteamID64: ").strip()
    games = get_owned_games(api_key, steamid)
    print(f"Total games: {len(games)}")
    for game in games:
        print(game['name'])
