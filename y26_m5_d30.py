# p = "   hello world   "
# P = "   HELLO WORLD   "

'''strip() method removes any leading (spaces at the beginning) and 
trailing (spaces at the end) characters (space is the default leading 
character to remove)'''
# print(p.strip())
# print(p)
'''lstrip() method removes any leading (spaces at the beginning) characters
 (space is the default leading character to remove)'''
# print(P.lstrip()) 
'''rstrip() method removes any trailing (spaces at the end) characters 
(space is the default trailing character to remove)'''
# print(P.rstrip())
# print(p.split());

#list 
x = ["Aurora", 22, "Python", 3.14];
# Indexing and slicing in the list
'''accessing the 3rd element of the list, 
where the [2] is the index of the element (index starts from 0)⬇️'''
print(x[2])
print("-------------------------")
x.append("Ryukai") #adding a new element to the end of the list
print(x)
print("-------------------------")
x[1] = 23 #modifying the 2nd element of the list
print(x)
print("-------------------------")
x.remove("Python") #removing an element from the list
print(x)
print("-------------------------")
x.insert(1, "Java") #inserting an element at a specific index
print(x)
print("-------------------------")
x.pop() #removing the last element of the list
print(x)