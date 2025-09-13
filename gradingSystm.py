#Student Class
class Student:
  def __init__(self, name, iD):
    self.name = name #Student name
    self.id = iD #Student Id
    self.subs = [] #Stores subject

  def add_subs(self, sub, grade): #Function to add subs to array of objects (subjects)
    subj = Sub(sub, grade)  #calls subject object
    self.subs.append(subj)

  def update_grade(self): #Function to update specific subject from an array
    self.show_subs()
    subj = int(input("Select subject to update: "))
    grd = int(input("Enter new grade: "))
    self.subs[subj-1].changeGrade(grd)  #Update specific subject from the array
    print(f"Subject {self.subs[subj-1].name} updated successfully")

  def getAve(self): #Function to get student's average
    if len(self.subs) <= 0:
      print("\nNo Subjects\n")
      return
    
    sum = 0
    for i in range (len(self.subs)):
      sum += self.subs[i].grade

    return sum/(len(self.subs))

  def show_subs(self): #Function to show list of subjects from an array
    if len(self.subs) <= 0:
      print("\nNo Subjects\n")
      return

    print(f"\n\n<------------------------->")
    print(f"Name: {self.name}")
    for i in range(len(self.subs)):
      print(f"{i+1}.) {self.subs[i].name}: {self.subs[i].grade}")
    print(f"--------------------------")
    print(f"Ave: {self.getAve():.2f}")
    print(f"<------------------------->\n\n")


class Sub: #Subject class
  def __init__ (self, name, grade):
    self.name = name
    self.grade = grade

  def changeGrade(self, newgrade): #function to change grade
    self.grade = newgrade


class Klass: #Klass ckass (class to grouped students)
  def __init__ (self):
    self.students = [] #array to grouped students
    self.studId = 1  #initial id, (helps to manage ids)

  def add_studs(self): #Function to add student
    name = input("Enter student name: ")
    student = Student(name, self.studId) #calls student object
    self.studId += 1 #Increment id adter adding student into the array

    num_subs = int(input(f"Enter how many subs?")) 
    for _ in range(num_subs): #repeatedly asks subject info
      sub = input("Enter Subject: ")
      grade = float(input(f"Enter initial grade: "))
      student.add_subs(sub, grade)

    self.students.append(student)

  def display_studs(self): #display student objects from the array
    if len(self.students) <= 0:
      print("\nNo students\n")
      return
    
    print("\n\n<---------STUDENTS---------->")
    for i in range (len(self.students)):
      print(f"{i+1}.) -ID:{self.students[i].id}   {self.students[i].name}  -ave:{self.students[i].getAve():.2f}") #Gets student info from every object
    print("<--------------------------->\n\n")

klass = Klass()
while True: 
  print(f"[1] Add Student")
  print(f"[2] Update Student")
  print(f"[3] Display Students")
  print(f"[0] Exit")
  opt = int(input("Enter option: "))
  
  if opt == 1:
    klass.add_studs()
  elif opt == 3: 
    klass.display_studs()
  elif opt == 2:
    klass.display_studs()
    std = int(input("Select student no.: "))
    klass.students[std-1].update_grade()
  elif opt == 0:
    break
  else:
    print("\n\nInvalid choice\n\n")


