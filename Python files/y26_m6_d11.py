'''
Aggregation it is similar to composition 
whether the difference 
'''

class Battery:
    def __init__(self, capacity, unit):
        self.capacity = capacity 
        self.unit = unit

    def power_usage(self):
        # Note: Added a string identifier just to show it running, 
        # since we can't math-add an int (capacity*1000) and a string (unit)
        return f"{self.capacity * 1000} {self.unit}" 
    
class Device:
    def __init__(self, company, device, chip):
        self.company = company
        self.device = device
        self.chip = chip

    def power_in_kvh(self):
        return self.chip.power_usage()
    
battery = Battery(10, unit="kvh")
dev = Device(company="samsung", device="handset", chip=battery)
print(dev.power_in_kvh())