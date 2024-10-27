class Student:
    def __init__(self, name, city, student_id, grade):
        self.name = name
        self.city = city
        self.student_id = student_id
        self.grade = grade
        self.marks = []

    def getdata(self):
        num_subjects = int(input("How many subjects? "))
        for i in range(num_subjects):
            mark = float(input(f"Enter marks for subject {i + 1}: "))
            self.marks.append(mark)

    def showdata(self):
        print(f"\nName: {self.name}, ID: {self.student_id}, City: {self.city}, Grade: {self.grade}")
        print(f"Marks: {self.marks}")


students = []
for i in range(4):
    print(f"\nStudent {i + 1}:")
    name = input("Name: ")
    city = input("City: ")
    student_id = input("ID: ")
    grade = input("Grade: ")