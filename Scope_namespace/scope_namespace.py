#creating a global nammespace
a=5
def sample():
    print("The global variable value is:",a)
sample()

#creating  a local namespace
def sum():
    b=3
    c= b+a
    print("the sum of global and local variable is:",c)
    #print the locals used in this class
    print(locals())
sum()