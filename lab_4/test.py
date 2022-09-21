class Person(object):
 
    def __init__(self,name):
        self.name = name
    def printName(self):
        print(self.name)
    def updateName(self, n):
        self.name += n
p = Person("dupa")
p.updateName('John')
p.printName()
