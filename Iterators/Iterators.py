#looping of an iterator
sets= ("Nepal", "USA", "Canada")
for x in sets:
    print(x)

# A simple Python program that iterates from 5 to given value
class Test:
	# Constructor __init__
	def __init__(self, a):
		self.a = a

	# Creates iterator object and calls when iteration is initialized
	def __iter__(self):
		self.b = 5
		return self

	# To move to next element we should replace next with __next__
	def __next__(self):

		# Store current value of b
		b = self.b

		# Stop iteration if limit is reached
		if b > self.a:
			raise StopIteration

		# Else increment and return old value
		self.b = b + 2;
		return b

# Prints numbers from 5 to 20
for i in Test(20):
	print(i)


