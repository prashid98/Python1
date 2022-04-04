#normal Lambda function
simple= lambda a: a + 2
print("This is the simple sum using lambda:",simple(2))

multiply = lambda b: b*5
print("this is the simple multiplication using lambda:",multiply(5))

#passing the multiple value on the lambda functions
multi_value_operation= lambda c,d,e: c+d-e
print("This is the multiple value operation result on lambda function:", multi_value_operation(4,5,6))

#using lambda function inside of another function
def lambda_function(n):
    return lambda f: f*n
g= lambda_function(5)#this pass the value to the function lambda_function
print("This final value of lambda function:",g(5))#this pass the value to the lambda function

#python lambda with list comprehension
lambda_list= [lambda h=h: h+2 for h in range (1,5)]
for i in lambda_list:
    print(i())

#python lambda function with if-else
minimum= lambda j,k: j if (j<k)else k
print("the minimum number from if else lambda is", minimum(3,4))    
