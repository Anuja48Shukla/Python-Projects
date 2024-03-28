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
        #super().__init__(eid, ename, ebasic)
        Employee.__init__(self,eid,ename,ebasic)
        self.foodAll = foodAll
        self.petAll = petAll

    def display(self):
        #super().display()
        Employee.display(self)
        print("", self.foodAll, self.petAll)

    def TotalSalary(self):
        return Employee.TotalSalary() + self.foodAll + self.petAll

class SalesPerson(Employee):
    def __init__(self, eid, ename, ebasic, Sales, Commission):
        Employee.__init__(self, eid, ename, ebasic)
        self.Sales = Sales
        self.Commission = Commission

    def display(self):
        Employee.display(self)
        print('', self.Sales, self.Commission)

    def TotalSalary(self):
        return Employee.TotalSalary() + (self.Sales*self.Commission)

class SalesManager(SalesPerson, Manager):
    def __init__(self, eid, ename, ebasic, foodAll, petAll, Sales, Commission, HRA):
        SalesPerson.__init__(self, eid, ename, ebasic, Sales, Commission)
        Manager.__init__(self, eid, ename, ebasic, foodAll, petAll)
        self.HRA = HRA

    def display(self):
        SalesPerson.display(self)
        Manager.display(self)

    def TotalSalary(self):
        return SalesPerson.TotalSalary(self) + self.HRA


mgr = Manager(300, 'Sam' , 45000 , 4000, 3000)
mgr.display()
print('Manager Total Salary : ', mgr.TotalSalary())

sales = SalesPerson(400, 'Ram', 10000, 20, 1000)
sales.display()
print('Sales Person Total Salary:', sales.TotalSalary())

Sales_Manager = SalesManager(111, 'Joy', 12000, 2000, 3000, 20, 200, 1500)
Sales_Manager.display()
print('Sales Manager Total Salary:', Sales_Manager.TotalSalary())



