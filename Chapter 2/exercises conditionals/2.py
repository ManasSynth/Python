# program to find Greatest of three numbers entered by user

a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))

if( a > b and a > c ):
    print("the largest number is ", a)
elif( b > c ):
    print("The Largest number is ", b)
else:
    print("The largest number is ", c)