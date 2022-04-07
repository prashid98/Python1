class sample():
    def __init__(self):
        self.var1=2
        #creating a private variable which can be used only with in the class
        self.__var2= 15
        print(self.__var2)
        pass
s= sample()
print(s.var1)