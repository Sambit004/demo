class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
            print(self.first,self.lastname)
 class student (person):
     pass
x=student("sambit","tom")
x.printname()
