#The reduce() function computation is similar to a for-loop in Python, but being an in-built function, it’s much better and faster.
from functools import reduce
num1= [2,3,4,5,6,7,8,9]

#finding the multiply of numbers using reduce
def multy(n,m):
    return n*m
result1= reduce(multy,num1)
print(result1)

#finding the sum of number using lambda and reduce
result2= reduce(lambda x,y: x+y, num1)
print(result2)