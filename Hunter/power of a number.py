def pow1(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*pow1(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",pow1(base,exp))
