A = [1, 2, 3, 4, 5]; #List

# for i in A:
#     if i >= 3:
#         print(i);
# else: 
#     print("Permission not granted!");

found = False;

for number in A:
    if number < 1:
        print(number);
        found = True;

if not found:
    print("Permission not granted!");