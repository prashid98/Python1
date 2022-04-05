#list comprehension
lists= ["car", "bike", "aeroplane", "Helicoptor", "Tractor"]
new_list=[x for x in lists if "tor" in x]
print(new_list)

#above program can also be given as following
new_list2 = []
for x in lists:
    if "tor" in x:
        new_list2.append(x)
print(new_list2)

#There is no comprehension on tuple since comprehension works by iterating over an items and assign them to the container.

#dictionary comprehension for the two times of odd number upto 10
new_list3 = [x for x in range(1,10)]
dictionary_comp= {}

for x in new_list3:
    if x % 2 == 1:
        dictionary_comp[x]= x * 2 
print("this is the output of dictionary comprenhension:",dictionary_comp)