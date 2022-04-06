#For unpacking we need to have same number of item as in the list
a,b,c= [4,5,6]
print("value of a:",a)
print("value of b:",b)
print("value of c:",c)

#we can pack the remaining value in the single variable using *
d,e,*f = [1,2,3,4,5,6]
print("value of f:", f)

#unpacking string
g,h,*i = "python intern"
print(g)
print(h)
print(i)

#creating a range object
j = [1,20,4]
range= list(range(*j))
print(range)

#unpacking 2 different objects
k = [1,2,3,4,5,6,7]
l= "prashid"
m= [*k, *l]
print(m)

#Unpacking a Sequence into Separate Variables
seq= ['Prashid', 'Kafle',23, 'Student', 'Nccs', (1,2,3,4,5,6,7,8)]
Fname, Lname, Years, Profession, College, Semesters = seq
print("First name:", Fname)
print("Last name:", Lname)
print("Age:", Years)
print("Profession:", Profession)
print("College name:", College)
print("Semesters Passed:", Semesters)