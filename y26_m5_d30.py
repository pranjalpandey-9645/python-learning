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

#List 
'''Lists are ordered, mutable, and allow duplicate elements. 
They are defined using square brackets [] and can contain elements of 
different data types.'''

# x = ["Aurora", 22, "Python", 3.14];
# # Indexing and slicing in the list
# '''accessing the 3rd element of the list, 
# where the [2] is the index of the element (index starts from 0)⬇️'''
# print(x[2])
# print("-------------------------")
# x.append("Ryukai") #adding a new element to the end of the list
# print(x)
# print("-------------------------")
# x[1] = 23 #modifying the 2nd element of the list
# print(x)
# print("-------------------------")
# x.remove("Python") #removing an element from the list
# print(x)
# print("-------------------------")
# x.insert(1, "Java") #inserting an element at a specific index
# print(x)
# print("-------------------------")
# x.pop() #removing the last element of the list
# print(x)
# print("-------------------------")
# x.pop(1) #removing an element at a specific index
# print(x)
# print("-------------------------")
# x.clear() #removing all elements from the list
# print(x)
# print("-------------------------")
# x.count("Aurora") #counting the number of occurrences of an element in the list
# print(x.count("Aurora"))
# print("-------------------------")
# x.__len__() #getting the length of the list
# print(x.__len__())
# print("-------------------------")
# del x #deleting the list
# #print(x) #this will raise an error because the list has been deleted

#Tuples
'''Tuples are similar to lists but they are immutable, meaning that once a tuple is created,
it cannot be modified. Tuples are defined using parentheses () instead of square brackets [].'''

A = ("Aurora", 22, "Python", 3.14); #it is a tuple with multiple data types
B = (1, 2, 3, 4, 5); #it is a tuple with only integers 
print(A[2]) #accessing the 3rd element of the tuple
print(B[0]) #accessing the 1st element of the tuple
print("-------------------------")
# A[1] = 23 #this will raise an error because tuples are immutable
# B[0] = 0 #this will also raise an error because tuples are immutable
print(A)
print(B)
print("-------------------------")
C = A + B #concatenating two tuples
print(C)
found = False;
for element in C:
    if element == "Python":
        print("Python is found in the tuple C")
        found = True;
        break;

if not found:
    print("Python is not found in the tuple C")

# if A + B == C: #checking if the concatenation of A and B is equal to C
#     print("A + B is equal to C")
# elif A == C: #checking if A is equal to C
#     print("A is equal to C")
# else:
#     print("A + B is not equal to C and A is not equal to C")