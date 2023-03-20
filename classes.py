#classes / class method / static method
class Person:
    def __init__(self,name,age,email): #constructor #initiator
        self.n=name
        self.e=email
        self.a=age
    def info(self): #instance method 
        print(f'the name of person is {self.n} and the age of person is {self.a}. and email is {self.e} ')   
    def info2(self):
        print(f'email of amir is {self.e} ')  
        print(f'the age of amir is {self.a} ')
    def info3(self):
        print(f'the name of person is {self.n} and age is {self.a} ')
jim=Person('jim',14,'jim123@gmail.com ') #instance
ali=Person('ali',19,'ali34@gmail.com ')
amir=Person('amir',23,'amir56@gmail.com ')
ali.info()
amir.info()
jim.info()
amir.info2()
jim.info3()
#print
print(jim.a)
print(ali.e)
#classes variables 
#if salary of ali ,jim and amir is same
class Person:
    salary=30000
    def __init__(self,name,age,email): 
        self.n=name #instance variables 
        self.e=email
        self.a=age
    def info(self): 
        print(f'the name of person is {self.n} and the age of person is {self.a}. and email is {self.e} ')   
 # change salary 
    @classmethod
    def change_salary(cls,new_salary):
        cls.salary=new_salary
    @staticmethod
    def isofficeopen(day):
        if day=='sunday':
            print('no today is holiday ')
        else:
            print('yes today is working day ')

jim=Person('jim',14,'jim123@gmail.com ') #instance
ali=Person('ali',19,'ali34@gmail.com ')
amir=Person('amir',23,'amir56@gmail.com ') 
Person.change_salary(40000)
print(ali.salary)
print(amir.salary)
print(jim.salary)

jim.isofficeopen('sunday')
ali.isofficeopen('monday')



