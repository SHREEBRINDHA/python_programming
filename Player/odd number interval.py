a=int(input())
b=int(input())
if(a and b<=1000):
 for n in range(a,b):
  if((n%2)!=0):
   if(n>a):
    print(n)
else:
    print("no")
