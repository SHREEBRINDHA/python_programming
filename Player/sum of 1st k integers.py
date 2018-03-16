x=[]
n=int(input(""))
k=int(input(""))
sum1=0
for i in range(n):
    x.append(int(input()))
for i in range(k):
    sum1=sum1+x[i]
print(sum1)
