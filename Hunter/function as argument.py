list = ['guvi'] 
def copy(x):
     print (x * 5)

 
def simple(fun, list):
     for item in list:
         fun(item)

 
simple(copy, list)
