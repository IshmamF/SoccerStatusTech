import pandas as pd
import requests
from tensorflow import keras
from taipy.gui import Markdown

def generate_predictions(team):
    teams_to_id_mapping = {"Arsenal FC": "57", "AFC Bournemouth": "1044", "Aston Villa FC": "58", "Brentford FC": "402",
                       "Brighton & Hove Albion FC": "397", "Burnley FC": "328", "Chelsea FC": "61", "Crystal Palace FC": "354",
                       "Everton FC": "62", "Fulham FC": "63", "Liverpool FC": "64", "Luton Town FC": "389",
                       "Manchester City FC": "65", "Manchester United FC": "66", "Newcastle United FC": "67",
                       "Nottingham Forest FC": "351", "Sheffield United FC": "356", "Tottenham Hotspur FC": "73", 
                       "West Ham United FC": "563", "Wolverhampton Wanderers FC": "76"}
    teams = {}
    teams[22] = {"Arsenal FC", "AFC Bournemouth", "Aston Villa FC", "Brentford FC",
                 "Brighton & Hove Albion FC", "Chelsea FC", "Crystal Palace FC",
                 "Everton FC", "Fulham FC", "Liverpool FC", "Manchester City FC", 
                 "Manchester United FC", "Newcastle United FC", "Nottingham Forest FC", 
                 "Tottenham Hotspur FC", "West Ham United FC", "Wolverhampton Wanderers FC"}
    teams_stats = {}
    teams_stats[22] = {}
    teams_stats[22]["Arsenal FC"] = [84, 88, 43, 38]
    teams_stats[22]["AFC Bournemouth"] = [39, 37, 71, 38]
    teams_stats[22]["Aston Villa FC"] = [61, 51, 46, 38] 
    teams_stats[22]["Brentford FC"] = [59, 58, 46, 38]
    teams_stats[22]["Brighton & Hove Albion FC"] = [62, 73, 53, 38]
    teams_stats[22]["Chelsea FC"] = [44, 38, 47, 38]
    teams_stats[22]["Crystal Palace FC"] = [45, 40, 49, 38]
    teams_stats[22]["Everton FC"] = [36, 34, 57, 38]
    teams_stats[22]["Fulham FC"] = [52, 55, 53, 38]
    teams_stats[22]["Liverpool FC"] = [67, 75, 47, 38]
    teams_stats[22]["Manchester City FC"] = [89, 94, 33, 38]
    teams_stats[22]["Manchester United FC"] = [75, 58, 43, 38]
    teams_stats[22]["Newcastle United FC"] = [71, 68, 33, 38]
    teams_stats[22]["Nottingham Forest FC"] = [38, 38, 60, 38] 
    teams_stats[22]["Tottenham Hotspur FC"] = [60, 70, 63, 38] 
    teams_stats[22]["West Ham United FC"] = [40, 42, 55, 38]
    teams_stats[22]["Wolverhampton Wanderers FC"] = [41, 31, 58, 38]
    teams_stats[23] = {}
    teams_stats[23]["Arsenal FC"] = [49, 47, 22, 23]
    teams_stats[23]["AFC Bournemouth"] = [27, 31, 44, 23]
    teams_stats[23]["Aston Villa FC"] = [46, 49, 30, 23] 
    teams_stats[23]["Brentford FC"] = [25, 34, 39, 23]
    teams_stats[23]["Brighton & Hove Albion FC"] = [35, 43, 40, 24]
    teams_stats[23]["Burnley FC"] = [13, 25, 50, 24]
    teams_stats[23]["Chelsea FC"] = [31, 38, 39, 23]
    teams_stats[23]["Crystal Palace FC"] = [24, 26, 40, 23]
    teams_stats[23]["Everton FC"] = [19, 26, 32, 24]
    teams_stats[23]["Fulham FC"] = [29, 33, 39, 24]
    teams_stats[23]["Liverpool FC"] = [54, 55, 23, 24]
    teams_stats[23]["Luton Town FC"] = [20, 33, 45, 23]
    teams_stats[23]["Manchester City FC"] = [52, 56, 25, 23]
    teams_stats[23]["Manchester United FC"] = [38, 31, 32, 23]
    teams_stats[23]["Newcastle United FC"] = [36, 51, 39, 24]
    teams_stats[23]["Nottingham Forest FC"] = [21, 30, 44, 24]
    teams_stats[23]["Sheffield United FC"] = [13, 22, 60, 24]
    teams_stats[23]["Tottenham Hotspur FC"] = [47, 51, 36, 24] 
    teams_stats[23]["West Ham United FC"] = [36, 36, 36, 23]
    teams_stats[23]["Wolverhampton Wanderers FC"] = [32, 37, 39, 24]
    
    url = "https://api.football-data.org/v4/teams/" + teams_to_id_mapping[team] + "/matches"
    headers = {'X-Auth-Token': 'e5b570312a1546f4a5a9d0675c3ad644'}
    params = {'season': '2023'}

    response = requests.get(url, headers=headers, params=params)

    data = response.json()
    for match in data["matches"]:
        if match["competition"]["name"] == "Premier League" and match["status"] == "TIMED":
            homeTeam = match["homeTeam"]["name"]
            awayTeam = match["awayTeam"]["name"]
            print("home: ", homeTeam)
            print("away: ", awayTeam)
            i = 23
            row1 = [1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
            row2 = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
            if homeTeam in teams[i - 1]:
                row1[2] = teams_stats[i - 1][homeTeam][0] / 38
                row1[4] = teams_stats[i - 1][homeTeam][1] / 38
                row2[3] = teams_stats[i - 1][homeTeam][0] / 38
                row2[5] = teams_stats[i - 1][homeTeam][2] / 38
            if awayTeam in teams[i - 1]:
                row1[3] = teams_stats[i - 1][awayTeam][0] / 38
                row1[5] = teams_stats[i - 1][awayTeam][2] / 38
                row2[2] = teams_stats[i - 1][awayTeam][0] / 38
                row2[4] = teams_stats[i - 1][awayTeam][1] / 38
            row1[6] = teams_stats[i][homeTeam][0] / teams_stats[i][homeTeam][3]
            row1[8] = teams_stats[i][homeTeam][1] / teams_stats[i][homeTeam][3]
            row2[7] = teams_stats[i][homeTeam][0] / teams_stats[i][homeTeam][3]
            row2[9] = teams_stats[i][homeTeam][2] / teams_stats[i][homeTeam][3]
            row1[7] = teams_stats[i][awayTeam][0] / teams_stats[i][awayTeam][3]
            row1[9] = teams_stats[i][awayTeam][2] / teams_stats[i][awayTeam][3]
            row2[6] = teams_stats[i][awayTeam][0] / teams_stats[i][awayTeam][3]
            row2[8] = teams_stats[i][awayTeam][1] / teams_stats[i][awayTeam][3]
            df_to_predict = pd.DataFrame([row1, row2], 
                                         columns=["Home Team", "Away Team",
                                                  "Points Obtained Last Season", "Points Obtained by Opponent Last Season",
                                                  "Goals Scored Last Season", "Goals Conceded by Opponent Last Season",
                                                  "Points Obtained This Season", "Points Obtained by Opponent This Season",
                                                  "Goals Scored This Season", "Goals Conceded by Opponent This Season"])
            model = keras.models.load_model('./prediction_model')
            predictions = model.predict(df_to_predict)
            return homeTeam, str(round(predictions[0][0], 2)), awayTeam, str(round(predictions[1][0], 2))


def button_pressed(state):
    state.showGraphs = True
    state.values[0] = state.value1
    state.values[1] = state.value2

    team_names_mapping = {"Arsenal": "Arsenal FC", "Bournemouth": "AFC Bournemouth", "Aston Villa": "Aston Villa FC", 
                          "Brentford": "Brentford FC", "Brighton": "Brighton & Hove Albion FC", "Burnley": "Burnley FC",
                          "Chelsea": "Chelsea FC", "Crystal Palace": "Crystal Palace FC", "Everton": "Everton FC", 
                          "Fulham": "Fulham FC", "Liverpool": "Liverpool FC", "Luton Town": "Luton Town FC", 
                          "Man City": "Manchester City FC", "Man United": "Manchester United FC", 
                          "Newcastle": "Newcastle United FC", "Nottingham": "Nottingham Forest FC", 
                          "Sheffield United": "Sheffield United FC", "Tottenham": "Tottenham Hotspur FC", 
                          "West Ham": "West Ham United FC", "Wolves": "Wolverhampton Wanderers FC"}
    state['predictions'].home_team_1, state['predictions'].home_goals_1, state['predictions'].away_team_1, state['predictions'].away_goals_1 = generate_predictions(team_names_mapping[state.value1])
    state['predictions'].home_team_2, state['predictions'].home_goals_2, state['predictions'].away_team_2, state['predictions'].away_goals_2 = generate_predictions(team_names_mapping[state.value2])
    state['predictions'].showPred = True

home_md = Markdown("home.md")    

    
    

    
    
    
    