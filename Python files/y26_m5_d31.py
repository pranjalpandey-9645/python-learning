# DICTIONARIES
'''dictionaries are mutable, unordered collections of key-value pairs. 
They are defined using curly braces {} and each key is separated from its 
value by a colon (:).'''

dict = {
           'name': "Aurora", "age": 22, "city": "New York", 
           "hobbies": ["coding", "READING", "traveling"],
           "occupation": "Student", "course": "B.tech in Computer Science"
           } #it is a dictionary with multiple data types

print(dict["name"]) #accessing the value of the key "name"
print("-------------------------")
print(dict["hobbies"]) #accessing the value of the key "hobbies"
print("-------------------------")
print(dict["occupation"]) #accessing the value of the key "occupation"
print("-------------------------")

dict["age"] = 23 #modifying the value of the key "age"
print(dict["age"]) #accessing the modified value of the key "age"
print("-------------------------")

print(dict.keys()) #getting all the keys of the dictionary
print("-------------------------")
print(dict.values()) #getting all the values of the dictionary

print("-------------------------")
print(dict.get("Gaming")) #this will return None because "Gaming" is not a key in the dictionary
# print(dict["Godrej"]) #this will raise an error because "Godrej" is not a key in the dictionary
print("-------------------------")
print(dict.get('name')) #this will return the value of the key 'name'
print("-------------------------")

for key, value in dict.items(): #iterating through the dictionary
    print(key, ":", value)

del dict["course"] #deleting a key-value pair from the dictionary
print(dict) 

'''🧑‍💻where if I want to delete my whole dictionary,
  I can use the del keyword followed by the name of the dictionary → #del dict
  🧑‍💻To update the dictionary, I can use the update() method & append() method
  🧑‍💻To check if a key exists in the dictionary, I can use the in keyword → "name" in dict
  🧑‍💻To get the number of key-value pairs in the dictionary, I can use the len() function → len(dict)
  🧑‍💻To clear all the key-value pairs from the dictionary, I can use the clear() method → dict.clear()
  🧑‍💻To copy a dictionary, I can use the copy() method → dict.copy()
  🧑‍💻To create a new dictionary from a list of keys and a default value, 
  I can use the fromkeys() method → dict.fromkeys(keys, default_value)'''