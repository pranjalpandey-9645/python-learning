# class Predators():
#     def __init__(self):
#         self.sting = "Scorpion"
#         self.__medi_kit = 80

#     def get_new_medikit(self):
#         return self.__medi_kit

# c = Predators()
# # c.get_new_medikit()

# print(c.sting)
# print(c.get_new_medikit())

class Dec():
    def __init__(self):
        self.x = 10
        self._y = 30
        self.__z = 50
    
    def public_method(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        self.__private_method()

    def __private_method(self):
        print("this is the private method in this class")
    
d = Dec()
d.public_method()
# d.__private_method()