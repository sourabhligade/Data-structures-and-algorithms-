Write a Python class, Flower, that has three instance variables of 
type str, int, and float, that respectively represent the name of the 
flower, its num- ber of petals, and its price. Your class must include
a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type.



class Flower:
    def __init__(self,name,numofpetals,price):
        self.name=name
        self.numofpetals=numofpetals
        self.price__=price
    def set_name(self,name):
        self.name=name
    def set_numofpetals(self,numofpetals):
        self.numofpetals=numofpetals
    def set_price(self,price):
        self.price__=price
    def get_name(self):
        return self.name
    def get_numofpetals(self):
        return self.numofpetals
    def get_price(self):
        return self.price__

rose = Flower("Rose", 12, 2.5)
print(rose.get_name())    
print(rose.get_numofpetals())  
print(rose.get_price())   

rose.set_name('red rose')

print(rose.get_name())    
print(rose.get_numofpetals())  
print(rose.get_price()) 
