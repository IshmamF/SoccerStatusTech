from taipy.gui import Markdown

def button_pressed(state):
    state.showGraphs = True
    state.values[0] = state.value1
    state.values[1] = state.value2

home_md = Markdown("home.md")
