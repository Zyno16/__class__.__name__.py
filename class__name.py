 
class person:
    def printtype(self):
        print(self.__class__.__name__)

class customer(person):
   pass
    

class employee(person):
    pass
   
    
class doctor(person):
   pass


p = person()
c = customer()
e = employee()
d = doctor()

p.printtype()
c.printtype()
e.printtype()
d.printtype()

