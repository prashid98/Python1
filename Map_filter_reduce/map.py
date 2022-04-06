#using map inorder to add the multiple numbers

def addition(n):
    return n + n
numbers = (5, 5, 7, 0, 10)
result = map(addition, numbers)
print(list(result))