from taipy.gui import Markdown

team1 = ''
team2 = ''

def button_pressed(state):
    state.showGraphs = True
    #state.value1 = "".join(state.team1)
    #state.value2 = "".join(state.team2)

home_md = Markdown("home.md")
