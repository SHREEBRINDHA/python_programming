a=int(input("enter a number"))
if a>1:
    for i in range (2,a):
        if(a%i)==0:
            print(a,"not a prime number")
            print(i,"times",a//i,"is",a)
            break
        else:
            print(a,"prime number")

