from model import Model
from view import View
from controller import Controller
import sys

def main():
    model = Model()
    view = View(model)
    controller = Controller(model, view)
    # try:
    controller.run()
    # except Exception:
        # print("Internal error exists!")
    # finally:
    model.write_file()
    sys.exit()
        
main()