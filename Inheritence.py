class Employee:
    def __init__(self, eid, ename, ebasic):
        self.eid = eid
        self.ename = ename
        self.ebasic = ebasic

    def display(self):
        print(self.eid, self.ename, self.ebasic, end='')

    def TotalSalary(self):
        return self.ebasic

class Manager(Employee):
    def __init__(self, eid, ename, ebasic, foodAll, petAll):
        super().__init__(eid, ename, ebasic)
        #Employee.__init__(self,eid,ename,ebasic)
        self.foodAll = foodAll
        self.petAll = petAll

    def display(self):
        super().display()
        #Employee.display(self)
        print("", self.foodAll, self.petAll)

    def TotalSalary(self):
        return super().TotalSalary() + self.foodAll + self.petAll

class SalesPerson(Employee):
    def __init__(self, eid, ename, ebasic, Sales, Commission):
        super().__init__(eid, ename, ebasic)
        self.Sales = Sales
        self.Commission = Commission

    def display(self):
        super().display()
        print('', self.Sales, self.Commission)

    def TotalSalary(self):
        return super().TotalSalary() + (self.Sales*self.Commission)

mgr = Manager(300, 'Sam' , 45000 , 4000, 3000)
mgr.display()
print('Manager Total Salary : ', mgr.TotalSalary())

sales = SalesPerson(400, 'Ram', 10000, 20, 1000)
sales.display()
print('Sales Person Total Salary:', sales.TotalSalary())



