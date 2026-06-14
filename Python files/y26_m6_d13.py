from abc import ABC, abstractmethod

# 1. Abstract Base Class (Blueprint)
class Car(ABC):
    def __init__(self, parts_obj):
        # AGGREGATION: We store the passed Parts object into a class variable
        self.parts = parts_obj  

    @abstractmethod
    def car_mechanism(self):
        pass
    
# 2. Independent Parts Class (Used for Aggregation)
class Parts:
    def __init__(self, part1, part2):
        self.upper = part1
        self.lower = part2

    def display_parts(self):
        return f"Upper body: {self.upper}, Lower body: {self.lower}"

# 3. Child Class (Concrete Class)
class Sportscar(Car):
    def __init__(self, *args):
        # *args receives arguments as a Tuple: (p, m1, m2)
        # args[0] is the Parts object 'p'
        # args[1] is the string 'm1'
        # args[2] is the string 'm2'
        
        # Pass the Parts object (args[0]) up to the parent class (Car) constructor
        super().__init__(args[0]) 
        
        # Unpack and assign the mechanism strings to separate instance variables
        self.mech1 = args[1]
        self.mech2 = args[2]

    def car_mechanism(self):
        # AGGREGATION IN ACTION: 
        # Using 'self.parts' (which holds the Parts object) to call its 'display_parts' method
        parts_info = self.parts.display_parts()

        return (f"--- CAR DETAILS ---\n"
                f"Mechanisms: 1. {self.mech1} | 2. {self.mech2}\n"
                f"Structure: {parts_info}")
    
# --- EXECUTION ---

# Step 1: Create an independent object of the Parts class
p = Parts("Carbon Fiber Spoiler", "Low-profile Alloy Wheels")

# Step 2: Take user inputs for the mechanisms
m1 = str(input("Enter your 1st mechanism (e.g., Turbocharge): "))
m2 = str(input("Enter your 2nd mechanism (e.g., AWD): "))

# Step 3: Instantiate Sportscar by passing the Parts object and the strings
# This is where Aggregation happens (passing one object into another)
sports_c = Sportscar(p, m1, m2)

print("\n-----------------\n")
# Step 4: Call the method to see the combined output of inheritance and aggregation
print(sports_c.car_mechanism())