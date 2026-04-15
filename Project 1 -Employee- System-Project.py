# Employees System Project
# The Employees System Project is a simple Python-based project that showcases the use of object-oriented programming (OOP) principles. It includes three main classes: Employee, EmployeesManager, and FrontendManager. This project provides a basic example of managing employee data and interactions using OOP concepts.
# Table of Contents
# •	Introduction
# •	Classes
# o	Employee
# o	EmployeesManager
# o	FrontendManager
# Introduction
# The Employees System Project demonstrates the implementation of object-oriented programming concepts in Python. It encompasses three primary classes, each serving a distinct purpose:
# Employee
# The Employee class represents an individual employee with the following attributes:
# •	name: The name of the employee.
# •	age: The age of the employee.
# •	salary: The salary of the employee.
# This class provides methods for string representation and formatted output of employee information.
# EmployeesManager
# The EmployeesManager class is responsible for managing a list of employees. It offers functionalities to:
# •	Add a new employee to the list.
# •	List all existing employees.
# •	Delete employees within a specified age range.
# •	Find an employee by their name.
# •	Update an employee's salary by name.
# FrontendManager
# The FrontendManager class provides a user interface for interacting with the EmployeesManager. Users can perform actions such as:
# •	Adding new employees.
# •	Listing existing employees.
# •	Deleting employees based on age range.
# •	Updating employee salaries by name.




class Employee:
  def __init__(self):
    self.emp_details=[]

  def display(self):
    self.name = input("Enter your name: ")
    self.age = int(input('Enter your age: '))
    self.salary = float(input ('Enter your salary: '))
    print(f"Employee Name:  {self.name} \nEmployee age:  {self.age} \nEmployee salary:  {self.salary}")
    self.emp_details.append({'name':self.name,'age':self.age,'salary':self.salary})
    print(self.emp_details)
    self.panel()

class EmployeeManager(Employee):
  def __init__(self):
    super().__init__()

  def addEmp(self):
    self.display()

  def displayEmp(self):
    print(self.emp_details)
    self.panel()

  def deleteEmp(self):
    b= int(input('enter start age range of employee'))
    c= int(input('enter end age range of employee'))
    for i in self.emp_details:
      if i['age']> b and i['age'] <c:
        self.emp_details.remove(i)
    print(self.emp_details)
    self.panel()

  def find_emp(self):
    b= input('enter name of employee')
    for i in self.emp_details:
      if i['name']== b:
        print(i)
    self.panel()

  def update_sal(self):
    print(self.emp_details)
    b= input('enter name of employee')
    c= float(input('enter updated salary'))
    for i in self.emp_details:
      if i['name']== b:
        i['salary']=c
    print(self.emp_details)
    self.panel()



class FrontedManager(EmployeeManager):
  def __init__(self):
    super().__init__()
    self.panel()

  def panel(self):
      a = input('''
      1. Adding new employees
      2. Listing existing employees
      3. Delete employees within a specified age range.
      4. Find an employee by their name.
      5. Update an employee's salary by name.
      6. exit
      ''')
      if a == '1':
        self.addEmp()
      elif a == '2':
        self.displayEmp()
      elif a=='3':
        self.deleteEmp()
      elif a == '4':
        self.find_emp()
      elif a=='5':
        self.update_sal()
      else:
        print('Thank You!')
        exit()


# a= Employee()
# a.display()
# b= EmployeeManager()
c=FrontedManager()
