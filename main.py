from model import Model
from view import View
from controller import Controller
from GUI import GUIv
import sys

def main():
    model = Model()
    GUI = GUIv(model)
    controller = Controller(model, GUI)
    try:
        controller.run()
    except Exception:
        print("Internal error exists!")
        sys.exit()
    finally:
        model.write_file()
        
main()