a = 120
for x in range(1,a+1):
    c = 0
    rev = 0
    temp = x
    for i in range(1,temp+1):
        if temp%i==0:
            c = c+1
    if c==2:
        while temp>0:
            rev = rev*10+(temp%10)
            temp = temp//10
        if rev==x:
            print(x)