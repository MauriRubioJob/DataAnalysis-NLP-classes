#  This is another program with some issues. Try to fix all of them.
#  

name1 = "Juan"
name2 = "Paco"
age1 = 20
age2 = int(input("Enter Paco's age"))

if ( age2 > age1 ):
    print(name2 + " is older than " + name1)
elif (age2 < age1):
    print(name1 + " is older than " +  name2)
else:
    print("They are the same age.")
