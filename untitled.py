import requests

teams_to_id_mapping = {"Arsenal FC": "57", "AFC Bournemouth": "1044", "Aston Villa FC": "58", "Brentford FC": "402",
                       "Brighton & Hove Albion FC": "397", "Burnley FC": "328", "Chelsea FC": "61", "Crystal Palace FC": "354",
                       "Everton FC": "62", "Fulham FC": "63", "Liverpool FC": "64", "Luton Town FC": "389",
                       "Manchester City FC": "65", "Manchester United FC": "66", "Newcastle United FC": "67",
                       "Nottingham Forest FC": "351", "Sheffield United FC": "356", "Tottenham Hotspur FC": "73", 
                       "West Ham United FC": "563", "Wolverhampton Wanderers FC": "76"}

def get_prediction(team):
    url = 'https://api.football-data.org/v4/teams/389/matches'
    #https://api.football-data.org/v4/competitions/2021/matches
    #/v4/teams/{id}/matches/
    headers = {'X-Auth-Token': 'e5b570312a1546f4a5a9d0675c3ad644'}
    params = {'season': '2023'}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        # Process the data as needed
        for match in data["matches"]:
            if match["competition"]["name"] == "Premier League" and match["status"] == "TIMED":
                print(match)
                break
    else:
        print(f"Error: {response.status_code}, {response.text}")