'''
Attributes prefixed with double underscores (__) are name-mangled
to discourage direct access from outside the class.

get_new_speed() is a getter method used to access the private attribute.

set_new_speed() is a setter method used to modify the private attribute.
'''

class Speed:
    def __init__(self):
        self.speed = 50
        self.__new_speed = 80

    def get_new_speed(self):
        return self.__new_speed

    def set_new_speed(self, new_speed):
        self.__new_speed = new_speed

s = Speed()

print(s.speed)

print("-------------------------------")

print(s.get_new_speed())
print("-------------------------------")
s.set_new_speed(70)
print(s.get_new_speed())

#--------------------------------------------------------------------------------------------------------------------#