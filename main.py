from taipy.gui import Gui
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


app = Gui(pages=pages)

if __name__ == '__main__':
    tp.Core().run()
    
    app.run(title="SoccerStatusTech", use_reloader=True, port=3000)