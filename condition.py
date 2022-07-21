#condition:-1
#B.M= 25kn/M
#S.F= 50kn/M

#if B.M>S.F:
 #   print("S.F")

#condition:-2
#Age=18.10
#if Age>=18:
 #   print("you are eligible for vote")
#else:
#    print("you are not eligible for vote") 

#condition:-3
from re import A, X
from tkinter import Y


# age= float(input("enter your age :: "))
# age=60
# if age >= 18:
#     print("you are eligible for votting !!")
# else:
#     ("you are not eligioble for votting !!")   


#condition:-4
# X=int(input("enter number :: "))
# Y=int(input("enter number :: "))
# Z=int(input("enter number :: "))

# X=25
# Y=35
# Z=45

# if X>Y:
#     print("x is greater then y")
# elif Y>Z:
#     print("y is greater then z")
# elif Z>X:
#     print("z is greater then x")        
# else:
#     print("entered number is not valid")
    

# x=25
# y=75
# z=45

# if x>y:
#     if x>z:
#         print("x is greater")
#     else:
#         print("z is greater") 
# else:
#     if y>z:
#         print("y is greater")
#     else:
#         print("z is grater")


x=(input("enter the value of x ::"))
y=(input("enter the value of y ::"))
z=(input("enter the value of z ::"))

if x>y:
    if x>z:
        print("x is greater")
    else:
        print("z is greater") 
else:
    if y>z:
        print("y is greater")
    else:
        print("z is grater")




#greater or less then using if else condition
 

x=(input("enter the value of x :: ")) 
y=(input("enter the value of y :: ")) 

if x>y:
    print("y is greater")
if x<y:
    print("x is greater")
        