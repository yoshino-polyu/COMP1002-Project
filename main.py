from model import Model
from view import View
from controller import Controller
import sys

def main():
    model = Model()
    model.init() # read all info from txt, and store it into storage.
    view = View(model)
    controller = Controller(model, view)
    try:
        controller.run()
    except Exception:
        print("Internal error exists!")
        sys.exit()
    # gui = new GUI(args)
    # gui.display(true)
    
main()