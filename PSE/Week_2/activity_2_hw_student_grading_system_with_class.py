# Activity 2: Deadline 2 May - Simple Student Grading System Using classes
# Task: Create students, record their grades, and show results.

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.courses = []
    
    def add_course(self, course):
        self.courses.append(course)
    
    def show_course_results(self):
        print(f"Student: {self.name} - ID: {self.id}")
        for course in self.courses:
            print(f"Course: {course.name} - Grade: {course.get_grade()}\n")

class Course:
    def __init__(self, name):
        self.name = name
        self.scores = []
        
    def add_score(self, score):
        self.scores.append(score)
        
    def add_scores(self, scores):
        self.scores.extend(scores)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)
    
    def get_grade(self):
        average_score = self.get_average_score()
        if average_score >= 90:
            return "A"
        elif average_score >= 80:
            return "B"  
        elif average_score >= 70:
            return "C"
        elif average_score >= 60:
            return "D"
        elif average_score >= 50:
            return "E"
        else:
            return "F"

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
        
    def add_student(self):
        student_info = input("Enter student name and id (e.g. John Doe, 123456): ")
        name, student_id = student_info.split(",")
        student = Student(name.strip(), student_id.strip())
        
        course_name = input("Enter course name: ")
        course = Course(course_name)
        scores = input("Enter scores for 3 assignments in the format 'score1, score2, score3': ")
        converted_scores = list(map(float, scores.split(",")))
        course.add_scores(converted_scores)
        
        student.add_course(course)
        self.students.append(student)
        
    def show_student_results(self):
        for student in self.students:
            student.show_course_results()
            
    def start_grading_system(self):
        while True:
            print("1. Add student")
            print("2. Show student results")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.show_student_results()
            elif choice == "3":
                break
            else:
                print("Invalid choice")


classroom = Classroom("Classroom 1")
classroom.start_grading_system()

