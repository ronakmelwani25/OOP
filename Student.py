class student():
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def showDetails(self):
        print("Name :" + self.name)
        print("Age :" + str(self.year))

s1 = student("Ronnie",9)
s1.showDetails()