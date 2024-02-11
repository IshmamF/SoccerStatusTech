from taipy.gui import Markdown
import requests

API_URL = "http://api.football-data.org/v4/competitions/PL/teams"
headers = { 'X-Auth-Token': 'bafc651292bf4fda9539e3a88814cb9e' }
response = requests.get(API_URL, headers=headers)

def nationalityChart(club):
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


team = 'Arsenal'

logo, countries = nationalityChart(team) 

data = {
    "Country": list(countries.keys()),
    "Count": list(countries.values())
}

showTeam = True


charts_md = Markdown("charts.md")