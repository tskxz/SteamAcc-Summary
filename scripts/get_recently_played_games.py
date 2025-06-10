import requests

def get_recently_played_games(api_key, steamid):
    url = "https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/"
    params = {
        'key': api_key,
        'steamid': steamid
    }
    resp = requests.get(url, params=params)
    try:
        data = resp.json()
    except Exception as e:
        print("Error decoding JSON response (recently played games)!")
        print("Status code:", resp.status_code)
        print("Response received:")
        print(resp.text)
        raise e
    games = data.get('response', {}).get('games', [])
    return games

if __name__ == "__main__":
    api_key = input("Your Steam API KEY: ").strip()
    steamid = input("Your SteamID64: ").strip()
    recent_games = get_recently_played_games(api_key, steamid)
    for game in recent_games:
        print(game)
