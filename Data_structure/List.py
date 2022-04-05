#simple list example in python
sim_list= ["Prashid","Jenish","Arun"]
print(sim_list) #This will print items of the list

#determinig the length of list
print(len(sim_list))

#indexing the content of list
print(sim_list[1])

#adding the content on list
sim_list.append("Test")
print(sim_list)

#accessing the last element of the list
print(sim_list[-1])

#using slice operation on list
print(sim_list[2:4])

#keeping the odd value less than 10 on list
new_list=[]
for x in range(0,11):
    if x % 2 == 1:
        new_list.append(x)
print("This are the list of odd number less than 10",new_list)

#joining different list as one
sim_list.extend(new_list)
print(sim_list)