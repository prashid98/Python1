#Try except error handling

a = 2
b= 0
try: #this will throw the exception error
    c=a/b
    print("the value of c is:",c)
except: #this will be executed after getting an error in try
    print("variable cannot be zero")


#try except and else error handling
try: 
    d= a/b
except:
    print("its an error")
else: 
    print(ArithmeticError)