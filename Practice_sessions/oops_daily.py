# class Practice1():
#     def __init__(self):
#        self.name = "Prakhar"
#        self.age = "20"
#        self.subject = "Commerce"
#        self.occupation = "Banking"

#     def display(self):
#         print("hey there! ", self.name)
#         print("your age is ", self.age)
#         print("and it's pretty good that you like ", self.subject)
#         print("we are hiring you for your good skills in ", self.occupation)

# p = Practice1()
# p.age = 30
# p.display()

# print("\n----------------------------------------\n")

class Maths():
    __velocity = None
    __displacement = None

    def set_velocity(self, vel):
        self.__velocity = vel 

    def get_velocity(self):
        return self.__velocity
    
    def set_displacement(self, disp):
        self.__displacement = disp

    def get_displacement(self):
        return self.__displacement
    
class Physics(Maths):
    def time(self):
        print(self.get_displacement() / self.get_velocity() * 2**3)

t = Physics()
t.set_velocity(30)
t.set_displacement(15)
t.time()