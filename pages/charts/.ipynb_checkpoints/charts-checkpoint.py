from taipy.gui import Markdown
import requests

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

data = {"Country":[], "Count":[]}
logo = ''
selected_team = ''
def toggle_choice(state):

    state.logo, countries = nationalityChart(state.selected_team, state.response) 

    state.data = {
        "Country": list(countries.keys()),
        "Count": list(countries.values())
    }


charts_md = Markdown("charts.md")