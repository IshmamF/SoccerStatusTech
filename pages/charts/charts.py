from taipy.gui import Markdown
import pandas as pd
import numpy as np

df = pd.read_csv('pages/charts/EPL-Standings-2000-2022.csv')

df = df.rename(columns={'GF': 'Goals Scored', 'GA': 'Goals Conceded', 'Pts': 'Points'})

showGraphs = False

team_name_mapping = {
    'Manchester United': 'Man United',
    'Newcastle United': 'Newcastle',
    'Tottenham Hotspur': 'Tottenham',
    'West Ham United': 'West Ham',
    'Wolverhampton Wanderers': 'Wolverhampton',
    'Brighton & Hove Albion': 'Brighton Hove',
    'Sheffield United': 'Sheffield Utd',
    'Manchester City' : 'Man City'
}

df['Team'] = df['Team'].replace(team_name_mapping)

def nationalityChart(club, response):
    nationalities = {}
    logo = ''
    for team in response.json()['teams']:
        if team['shortName'].lower() == club.lower():
            logo = team['crest']
            for player in team['squad']:
                if player['nationality'] not in nationalities:
                    nationalities[player['nationality']] = 1
                else:
                    nationalities[player['nationality']] += 1
    return logo,nationalities 

layout = {
    "yaxis": {
      # Place the y axis on the left
      "side": "left",
      # and give it a title
      "title": "Games"
    },
    "title": {
        "text" : "Win vs Losses Throughout the Season(s)"
    }
}

dataframe = {"Season":[], "W":[], "L":[]}
allFrame = {"Season":[], "Goals Scored":[], "Goals Conceded":[], "Points":[]}

data = {"Country":[], "Count":[]}
logo = ''
selected_team = ''
def toggle_choice(state):

    state.logo, countries = nationalityChart(state.selected_team, state.response) 

    state.data = {
        "Country": list(countries.keys()),
        "Count": list(countries.values())
    }
    

    state.dataframe = df[df['Team']==state.selected_team].copy()
    state.allFrame = df[df['Team']==state.selected_team].copy()
    state.showGraphs = True

charts_md = Markdown("charts.md")