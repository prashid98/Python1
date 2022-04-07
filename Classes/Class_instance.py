#creating a class
class mydetail:
    name = "prashid"
    #creating a constructor
    def __init__(self, age, company):
        self.age= age
        self.company = company
m=mydetail(23, "cotiviti")
print("My detail", m.name, "age", m.age, "company",m.company)
