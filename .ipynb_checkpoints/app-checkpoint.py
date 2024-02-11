from taipy.gui import Gui

app = Gui()
#gui.run(dark_mode=False, port=5001)
if __name__=='__main__':
    app.run(use_reloader=True, port = 5001)