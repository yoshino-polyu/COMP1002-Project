from view import View
from model import Model
b = Model()
a = View(b)
print(type(a).__name__)
FL = open("storage.txt","w")
print(type(FL).__name__)
FL.close()