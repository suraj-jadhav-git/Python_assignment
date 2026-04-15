# Hospital Patient Queue Management System
# The Hospital Patient Queue Management System is a Python-based command-line application designed to manage patient queues in a hospital. It utilizes object-oriented programming (OOP) principles and includes three main classes: Patient, Specialization, and OperationsManager. This project provides a simple yet effective way to handle patient data and queue management within a hospital setting.
# The Hospital Patient Queue Management System is an illustration of OOP concepts in Python. It consists of three primary classes, each serving a specific purpose:
# Patient
# The Patient class represents an individual patient and includes the following attributes:
# •	name: The name of the patient.
# •	status: The patient's status, which can be 0 (normal), 1 (urgent), or 2 (super-urgent).
# This class provides methods for string representation and status formatting for patients.
# Specialization
# The Specialization class manages patient queues within different specializations. It offers functionalities such as:
# •	Adding patients with various urgency levels.
# •	Retrieving the next patient from the queue.
# •	Removing patients by name.
# •	Checking queue capacity.
# OperationsManager
# The OperationsManager class serves as the user interface for interacting with the Specialization instances. Users can perform actions like:
# •	Adding new patients to specializations.
# •	Listing patients in specializations.
# •	Retrieving the next patient.
# •	Removing patients.
# •	Ending the program gracefully.


class Patient:
  def __init__(self):
    self.cardiac_q=[]
    self.dentist_q=[]
    self.neuro_q=[]
    self.dermat_q=[]

  def status(self):
    a=input(""" enter specialization-
    1. Cardic
    2. Dentist
    3. Neuro
    4. Dermat
    5. Exit
    """)
    if a== '1':
      x=self.cardiac_q
    elif a== '2':
      x=self.dentist_q
    elif a== '3':
      x=self.neuro_q
    elif a== '4':
      x=self.dermat_q
    else:
      print('enter valid input number')


    for i in x:
      print(f"Patient Name: {i[1][0]} Patient Status: {i[1][1]}")

    self.panel()


class Specialization(Patient):
  def __init__(self):
    super().__init__()


  def add_patient(self):
    self.name= input('enter patients name')
    l= input("enter your status \n0: normal \n1: urgent \2: super urgent")
    if l== '0':
      x='normal'
    elif l== '1':
      x='urgent'
    elif l== '2':
      x='super-urgent'
    else:
      print('enter valid status number')
      self.panel()
    self.p=(int(l),(self.name,x))

    a=input(""" enter specialization-
    1. Cardic
    2. Dentist
    3. Neuro
    4. Dermat
    5. Exit
    """)
    if a== '1':
      self.cardiac_q.append(self.p)
      print('Cardiac queue')
      self.cardiac_q.sort(reverse=True)
      print(self.cardiac_q)

    elif a== '2':
      self.dentist_q.append(self.p)
      print('Dentist queue')
      self.dentist_q.sort(reverse=True)
      print(self.dentist_q)

    elif a== '3':
      self.neuro_q.append(self.p)
      print('Neuro queue')
      self.neuro_q.sort(reverse=True)
      print(self.neuro_q)

    elif a== '4':
      self.dermat_q.append(self.p)
      print('Dermat queue')
      self.dermat_q.sort(reverse=True)
      print(self.dermat_q)

    else:
      print('enter valid input number')
    self.panel()

  def show_queues(self):
    print('Cardiac queue')
    print(self.cardiac_q)
    print('Dentist queue')
    print(self.dentist_q)
    print('Neuro queue')
    print(self.neuro_q)
    print('Dermat queue')
    print(self.dermat_q)
    self.panel()


  def next_patient(self):
    a=input(""" enter specialization-
    1. Cardic
    2. Dentist
    3. Neuro
    4. Dermat
    5. Exit
    """)
    if a== '1':
      l=self.cardiac_q
      l.remove(l[0])
      print('Cardiac queue')
      print(l[0])

    elif a== '2':
      l=self.dentist_q
      l.remove(l[0])
      print('Dentist queue')
      print(l[0])

    elif a== '3':
      l=self.neuro_q
      l.remove(l[0])
      print('Neuro queue')
      print(l[0])

    elif a== '4':
      l=self.dermat_q
      l.remove(l[0])
      print('Dermat queue')
      print(l[0])

    else:
      print('enter valid input number')
    self.panel()

  def remove_patient(self):
    p_name = input('enter patients name')
    a=input(""" enter specialization-
    1. Cardic
    2. Dentist
    3. Neuro
    4. Dermat
    5. Exit
    """)
    if a== '1':
      x=self.cardiac_q
    elif a== '2':
      x=self.dentist_q
    elif a== '3':
      x=self.neuro_q
    elif a== '4':
      x=self.dentist_q
    else:
      print('enter valid input number')
      self.panel()

    for i in x:
      if i[1][0]== p_name:
        x.remove(i)
        print('removed->',i)
        print(x)
        self.panel()


  def check_q(self):
    print('Patients in Cardiac Queue : ',len(self.cardiac_q))
    print('Patients in Dentist Queue : ',len(self.dentist_q))
    print('Patients in Neuro Queue : ',len(self.neuro_q))
    print('Patients in Dermat Queue : ',len(self.dermat_q))
    self.panel()


class OperationsManager(Specialization):
  def __init__(self):
    super().__init__()
    self.panel()

  def panel(self):
    a=input("""
    1. Add a new patient to specialization
    2. listing patients in specilization
    3. Call the next patient
    4. Remove a patient by name
    5. Check q capacity
    6. display Petient details
    7. Exit
    """)
    if a== '1':
      self.add_patient()
    elif a== '2':
      self.show_queues()
    elif a== '3':
      self.next_patient()
    elif a== '4':
      self.remove_patient()
    elif a== '5':
      self.check_q()
    elif a== '6':
      self.status()
    elif a== '7':
      print('thank you!')
      exit()
    else:
      print('enter valid input number')

# obj=Patient()
obj=OperationsManager()