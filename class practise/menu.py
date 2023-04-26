# Create a class to represent a 
# restaurant menu. This class should have methods 
# for adding and removing menu items, 
# as well as displaying the menu.

class Menu:
    def __init__(self):
        self.menu=[]
    
    def add_item(self,menu_item):
        #self.menu+=menu_item #String
        self.menu.append(menu_item)
    
    def rem(self,menu_item):
        self.menu.remove(menu_item)

    def display(self):
        for item in self.menu:
            print(item)
       
    
menu=Menu()
menu.add_item("Burger")
menu.add_item("Pizza")
menu.add_item("Cola")

menu.display()
