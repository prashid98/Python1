#program to filter the even numbers
from pickle import FALSE, TRUE


num1= [1,2,3,4,5,6]
a= filter(lambda x: x%2, num1)
print(list(a))

#program to filter the ages above 18
age= [10,20,25,17,21,5,31]
def adult(x):
    if x <= 18:
        return False
    else:
        return True
age_group=filter(adult,age)
print(list(age_group))
