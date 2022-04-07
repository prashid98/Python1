#inheritance
class sam1:
    def b(self):
        print("In sample1")
class sam2(sam1):
    def b(self):
        print("In sample2")
c= sam2()
c.b()


#multiple inheritance
class Class1:
	def a(self):
		print("In Class1")
	
class Class2(Class1):
	def a(self):
		print("In Class2")

class Class3(Class1):
	def a(self):
		print("In Class3")
		
class Class4(Class2, Class3):
	pass
	
obj = Class4()
obj.a()


