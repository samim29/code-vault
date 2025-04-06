'''1. Design and implement a lython program for managing student information using obgect-oriented
principles. Create a class called `Student` with encapsulated attributes for name, age, and roll number.
Implement getter and setter methods for these attributes. Additionally, provide methods to display student
information and update student details.'''

class Student:
    def __init__(self,name,age,roll):
        self.__name=name
        self.__age=age
        self.__roll_number=roll

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_roll_number(self):
        return self.__roll_number
    
    def set_name(self,new_name):
        self.__name=new_name
    def set_age(self,new_age):
        self.__age=new_age
    def set_roll_number(self,new_roll):
        self.__roll_number=new_roll

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Roll Number: {self.__roll_number}")
    
    def update_student_details(self,new_name,new_age,new_roll):
        self.set_name(new_name)
        self.set_age(new_age)
        self.set_roll_number(new_roll)
        print("Stdent's details updated successfully")
    

std1=Student("Mohon",20,15)
std1.display()
std1.update_student_details("Mehek",21,25)
std1.display()
