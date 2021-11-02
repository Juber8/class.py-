
'''class collage:

    def __init__(self,name,collage,country):
        self.name=name
        self.collage=collage
        self.country=country
s=collage()

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method access instance variable
    #def show(self):
        #print('Name:', stud.name, 'Age:', stud.age)

# create object
stud = Student('jessa',20)
stud.name

# call instance method
#stud.show()

#class variable / static varible
class student:
    #class variable
    school_name='abc school'

    def __init(self,name):
        self.name = name
        #acces the static varaible inside the constructor using self
        print(self.school_name)
        #acces the class varible inside the constructor using class name
        print(student.school_name)
s1=student()

#outside the class by using object refrance
print(s1.school_name)
#outside the class by using class name
print(student.school_name)

class juber:
    school_name= 'sgi kolhapur'

    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no
        print(self.school_name)
        print(juber.school_name)
s1=juber('juber',22,146)
print(s1.name,s1.age,s1.roll_no)

class juber:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print('name:',self.name,'age:',self.age)

    def upadate(self,country):
        self.country=country

    def display(self):
        print('country:',self.country)

s=juber('juber',15)
s.show()
s.display()
class juber:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def update(self,place):
        self.place=place
s=juber('juber',14)
s.update('patan')
print(s.name,s.age,s.place)
#s.__init__('tushar',15)
print(s.__init__('tushar',15))

class juber:
    def __init__(self,name):
        self.name=name
    def update(self,pin):
        self.pin=pin
s=juber('juber')
s.update('1254')
print(s.name)
print(s.pin)
delattr(s,'update')
s.update(12)

class sample:
    pin=123234
    @classmethod
    def jm(cls):
        print('pin no is',cls.pin)
s=sample()
s.jm()

class sample:
    pin=1324
    def m1(self):
        print(self.pin)
    @classmethod
    def m2(cls):
        print(cls.pin)
s=sample()
s.m1()
s.m2()

class school:
    pin=1245
    def m1(cls):
        print(cls.pin)
school.m1=classmethod(school.m1)
school.m1()
'''
























