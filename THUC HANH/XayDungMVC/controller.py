from model import car
import view

def showAll():
    all_car = car.get_all_car()
    view.showAllView(all_car)

def start():
   choice = view.startView()
   if choice == 'y':
      showAll()
   else:
      view.endView()

#Chương trình chính
if __name__ == "__main__":
   #running controller function
   start()