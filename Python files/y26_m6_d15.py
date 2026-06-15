fh = open("Aurora.txt", "w") # This will open the Aurora.txt file and add the line 1.
'''This will open the Aurora2.txt file to write and if it is not there then 
   it will create one inside your vs code same as the Aurora.txt that ic created
   just by using the same method.'''
kt = open("Aurora2.text", "w")
# fh = open("Aurora.txt", "w") # This will print the lines after the line 1.
# fh = open("Aurora.txt", "a") # This will print the lines after the written one on some date.
# fh = open("Aurora.txt", "r") #This will only read the file
# fh = open("Aurora.txt", "r") 
# fh.readline()[12]   # This will read 12 lines.
# print(fh.readlines())

# fh.write("This is the text file just to read and learn the code!")
fh.writelines("This is the god humors and not for the humans.\n"
"This is the another humerous body typo and this will create the things like, \nimaginary for the real men!\n" \
"Well the world only cares about results not about the process it takes.")

kt.writelines("")
fh.close()