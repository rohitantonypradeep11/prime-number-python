from math import sqrt
a = int(input("enter a number"))
if a>1:
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            print("its not a prime number")
            break
    else:
        print("its a prime number")
else:
    print("its not a prime number")