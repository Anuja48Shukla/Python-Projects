class Employee:
    def __init__(self, eid, ename, ebasic):
        self.eid = eid
        self.ename = ename
        self.ebasic = ebasic

    def display(self):
        print(self.eid, self.ename, self.ebasic)

emp1 = Employee(100,'Raj',5000.00)
emp2= Employee(200,'Giri',6000.00)

emp1.display()
emp2.display()
