#generator dont hold all the result in the memory. It hold one result at a time
def square(a):
    #no need to initialize the list like list = []
    for i in a:
        #no need to return the value
        yield(i *i)

num= square([2,3,4,5,6,7,8])
#this will give the individual results
print (next(num))
print (next(num))#this will give the value next to above printed value and goes on continue
print (next(num))
print (next(num))   
print (next(num))


