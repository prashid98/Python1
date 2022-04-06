#using map inorder to add the multiple numbers

def addition(n):
    return n + n
numbers = (5, 5, 7, 0, 10)
result = map(addition, numbers)
print(list(result))

#lambda using map function
numbers2= (2,3,4,5,8)
lambda_results= map(lambda a,b:a*b,numbers, numbers2 )
print(list(lambda_results))