addition = None
x = int(input("Enter your number: "))
y = int(input("Enter your 2nd number: "))

try:
   print(x/y)
except Exception as e:
#    print("Code error!!!", e)
     print(type(e))
print("-----Exception handling------")
print(addition)