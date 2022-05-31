def fac(n):
    f = 1
    for x in range(1,n+1):
        f = f*x
    return f

a = int(input("Please enter the desired Number: "))
if a < 0:
    print("Sorry wrong number inserted") 
elif a == 0:
    print("The Factorial of 0 is 1")
else:
   b = fac(a)
   print("The desired Factorial is :",b)
#    print(result)