from taipy.gui import Gui
from taipy import config
import taipy as tp

from pages.home.home import home_md
from pages.prediction.predictions import predictions_md
from pages.charts.charts import charts_md
from pages.root import root

pages = {
    '/':root,
    'home':home_md,
    "statistics":charts_md,
    "predictions":predictions_md,
}

light_theme = {
    "palette": {
        "background": {
            "default": "#d580ff"  
        },
        "primary": {"main": "#ffffff"}
    }
}

dark_theme = {
    "palette": {
        "background": {
            "default": "#471061"  
        },
        "primary": {"main": "#000000"}
    }
}

card = {
    "palette": {
        "background": {
            "default": "#471061"  
        },
        "primary": {"main": "#000000"}
    }
}

value1="team1"
value2="team2"
showGraphs = False

app = Gui(pages=pages)

Gui.add_shared_variables(value1, value2, showGraphs)

if __name__ == '__main__':
    tp.Core().run()
    
    app.run(title="SoccerStatusTech", use_reloader=True, port=3636, light_theme=light_theme, dark_theme=dark_theme)