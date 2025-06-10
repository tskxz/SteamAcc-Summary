import requests

def get_player_summaries(api_key, steamid):
    url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/"
    params = {
        'key': api_key,
        'steamids': steamid
    }
    resp = requests.get(url, params=params)
    try:
        data = resp.json()
    except Exception as e:
        print("Error decoding JSON response (player summaries)!")
        print("Status code:", resp.status_code)
        print("Response received:")
        print(resp.text)
        raise e
    players = data.get('response', {}).get('players', [])
    return players[0] if players else {}

if __name__ == "__main__":
    api_key = input("Your Steam API KEY: ").strip()
    steamid = input("Your SteamID64: ").strip()
    summary = get_player_summaries(api_key, steamid)
    for k, v in summary.items():
        print(f"{k}: {v}")
