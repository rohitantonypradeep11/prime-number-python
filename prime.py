a = int(input("enter a number"))
if a>1:
    for i in range(2,(a//2)+1):
        if a%i==0:
            print("its not a prime number")
            break
    else:
        print("its a prime number")
else:
    print("its not a prime number")