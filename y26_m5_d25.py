#concatenation
# a = 4;
# b = 23;
# print("the sum of a and b is ", a+b);

# print("the sum of {0} and {1} is {2}".format(a,b,a+b));

# strinG = "hello world";
# print(strinG[0]);
# print(strinG[0:5]);
# print(strinG[6:11]);

#conditional statements
# num = int(input("enter the number of processes in the system: "));
# num = num*10;
# print("the number of processes in the system is ", num);

# if num > 100:
#     print("the system is overloaded");
# elif num == 100:
#     print("the system is at full capacity");    
# else:
#     print("the system is underloaded");

#Example of simple calculator
num1 = int(input("enter the first nnumber: "));
num2 = int(input("enter the second number: "));
operator = input("enter the operator: ");

if operator == "+":
    print("the sum of ", num1, " and ", num2, " is ", num1+num2);
elif operator == "-":
    print("the difference of ", num1, " and ", num2, " is ", num1-num2);
elif operator == "*":
    print("the product of ", num1, " and ", num2, " is ", num1*num2);
elif operator == "/":
    print("the quotient of ", num1, " and ", num2, " is ", num1/num2);
else:
    print("invalid operator");
