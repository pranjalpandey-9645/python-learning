class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
    def show(self):
        print(f"Student Name: {self.name}, Age: {self.age}")
        
s1 = Student("Pranjal", 101)
s1.show()  # This will print the name and age of s1
s1.display()  # This will also print the name and age of s1
s2 = Student("Rohit", 102)
s2.show()  # This will print the name and age of s2
s2.display()  # This will also print the name and age of s2
s3 = Student("Rohan", 103)
s3.show()  # This will print the name and age of s3
s3.display()  # This will also print the name and age of s3


questions = {
    "Capital of India? ": "Delhi",
    "2 + 2 = ? ": "4",
    "Color of sky? ": "blue"
}

score = 0
for q, a in questions.items():
    ans = input(q)
    if ans.strip().lower() == a.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"\nYour Score: {score}/{len(questions)}")
