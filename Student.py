class student():
    def __init__(self,name,year,hobby,grade):
        self.name=name
        self.year=year
        self.hobby=hobby
        self.grade=grade
    def showDetails(self):
        print("Name: " + self.name)
        print("Age: " + str(self.year))
        print("Hobby: " + self.hobby)
        print("Grade: " + str(self.grade))

s1 = student("Ronnie",9,"Gaming",9)
s2 = student("Neev",9,"Cricket",1)
s1.showDetails()
s2.showDetails()