#normal function in python
def new_functions():
    print("hello, its 1st function in python")
new_functions() #calling the new_functions.

#passing the information from the function
def single_argument(a):
    print("this is a single argument function value:", a + 5)
single_argument(15) #pass the single value 15 into the single_argument

#passing a multiple information from the function
def multi_argument(b,c):
    print("this is a value of multiple argument function:", b + " "+ c)
multi_argument("Prashid", "Kafle") #pass the multiple string value at once.

#return value from the functions
def return_value(d):
    return d*3
print("This return the value by calling the function:",return_value(5)) #return the value of 5*3 after calling the function return_value 

#default value initialization in function
def default_value(e, message="Good Morning"):
    print(e+", "+message)
default_value("ram", "good morning")
default_value("shyam") #this will take the default value of message as an augument

#Function with a tuple of arguments
def tuple_function(*f):
    print(f," is the employee of cotiviti")
tuple_function("Prashid","Jenish","arun")

#function with individual tuple arguments
def tuple_indvfunction(*g):
    for indv in g:
            print(indv," is the employee of cotiviti")
tuple_indvfunction("Prashid","Jenish","arun")