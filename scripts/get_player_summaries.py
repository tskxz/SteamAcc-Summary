import requests
import os

# todo: DRY this with other scripts
def load_env():
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    env = {}
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if '=' in line:
                    k, v = line.strip().split('=', 1)
                    env[k.strip()] = v.strip()
    else:
        api_key = input("Your Steam API KEY: ").strip()
        steamid = input("Your SteamID64: ").strip()
        with open(env_path, 'w', encoding='utf-8') as f:
            f.write(f'STEAM_API_KEY={api_key}\nSTEAMID64={steamid}\n')
        env['STEAM_API_KEY'] = api_key
        env['STEAMID64'] = steamid
    return env

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
    env = load_env()
    api_key = env['STEAM_API_KEY']
    steamid = env['STEAMID64']
    summary = get_player_summaries(api_key, steamid)
    for k, v in summary.items():
        print(f"{k}: {v}")
