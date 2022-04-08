import re

#regular expression to find out the number of vi simultaneously used in string
txt = "Hello and welcome to cotiviti Nepal."
x = re.findall("vi", txt)
print(x)

#find the location of a character
y = re.search("i", txt)

print("The first i character is located in position:", y.start())

