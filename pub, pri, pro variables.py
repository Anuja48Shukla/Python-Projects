class Employee:
    def __init__(self,eid,ename,ebasic):
        self.__eid = eid
        self.__ename = ename
        self.__ebasic = ebasic
    def display(self):
        print(self.__eid,self.__ename,self.__ebasic)
    def getebasic(self):
        return self.__ebasic

    def setebasic(self,ebasic):
        self.__ebasic = ebasic

    def delebasic(self):
        del(self.__ebasic)

    ebasic = property(getebasic,setebasic,delebasic)


#__main__
emp1 = Employee(100,'Raj',5000.00)
emp1.display()

emp2 = Employee(200,'Giri',6000.00)
emp2.display()
#print(emp2.__ename)
#print(emp1.getebasic())

#emp1.setebasic(55555)

emp1.ebasic = 2000000
print(emp1.ebasic)
del(emp1.ebasic)

emp1.display()


#print('outside class:',emp1._Employee__ebasic) #happens internally
#emp1.display()


#name mangling method
#Encapsulation

##
##def someMeth(emp):
##    print(emp.ebasic)
##
##
##someMeth(emp1)
