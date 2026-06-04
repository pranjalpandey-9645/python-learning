A = [1, 2, 3, 4, 5]; #List

# for i in A:
#     if i >= 3:
#         print(i);
# else: 
#     print("Permission not granted!");

# found = False;

# for number in A:
#     if number < 10:
#         print(number);
#         found = True;

# if not found:
#     print("Permission not granted!");

found = True;
for number in A:
    if number < 20:
        print(number);
        found = False;
if found:
    print("Permission not granted!");