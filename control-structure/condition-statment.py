age = int(input("enter your age:"))
print("your age is:",age)

#condition operator 
# >,<,<=,>=,==,!=
print(age>18)
print(age>=18)
print(age<=18)
print(age!=18)
print(age==18)
print(age==18)
if(age>18):
    # : means start the block
    print("i am  adult")
    # space (indentation after remove space it will be show the error)
    #indentation means start the block


#nested 
elif(age==18):
    print("now you adult")
else:
    print("i am not adult")