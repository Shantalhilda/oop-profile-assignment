class Student:
    def __init__(self,name):
        self.name = name          #public
        self._gpa = 3.5           #protected
        self.__password = "1234"  #private



student1 = Student("shantal");

print(student1.name)
print(student1._gpa)

#change name to albert
student1.name = "hillary"



