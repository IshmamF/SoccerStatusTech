from taipy.gui import Markdown

def button_pressed(state):
    state.showGraphs = True

home_md = Markdown("home.md")
