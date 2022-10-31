class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectories(self, mentor, course, grade_l):
        if course in self.courses_in_progress and course in mentor.courses_attached and isinstance(mentor, Lecturer):
            if course in mentor.grades_lectur:
                mentor.grades_lectur[course] += [grade_l]
            else:
                mentor.grades_lectur[course] = [grade_l]
        else:
            return 'Ошибка'


    def midle_grades_student(self):
        midle_g = 0
        for key in self.grades:
            midle = sum(self.grades[key]) / len(self.grades[key])
            midle_g += midle
        self.all_midle = midle_g / len(self.grades)

    def __gt__(self, other):
        self.midle_grades_student()
        other.midle_grades_student()
        sc = float(other.all_midle)
        if self.all_midle > sc :
            return f"Средний балл {self.surname} больше среднего балла {other.surname}"
        else:
            return f"Средний балл {self.surname} меньше среднего балла {other.surname}"


    def __str__(self):
        self.midle_grades_student()
        l = " ".join(self.courses_in_progress)
        m = " ".join(self.finished_courses)
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания:{self.all_midle}\nКурсы в процессе обучения:{l}\nЗавершенные курсы:{m}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and isinstance(self, Reviewer) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lectur = {}

    def midle_grades_lector(self):
        midle_g = 0
        for key in self.grades_lectur:
            midle = sum(self.grades_lectur[key]) / len(self.grades_lectur[key])
            midle_g += midle
        self.all_midle = midle_g / len(self.grades_lectur)

    def __gt__(self, other):
        self.midle_grades_lector()
        other.midle_grades_lector()
        sc = float(other.all_midle)
        if self.all_midle > sc :
            return f"Средний балл {self.surname} больше среднего балла {other.surname}"
        else:
            return f"Средний балл {self.surname} меньше среднего балла {other.surname}"


    def __str__(self):
        self.midle_grades_lector()
        return f"Имя: {self.name} \nФамилия: {self.surname}\n \nСредняя оценка за лекции{self.all_midle}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

student_1 = Student('Mike', 'Baum', 'your_gender')
student_1.courses_in_progress += ['Python', "Git"]
student_1.finished_courses += ["Introduction in IT"]


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
print(cool_mentor)

lecturer_1 = Lecturer("Sam", "Smith")
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer("Ivan", "Wolf")
lecturer_2.courses_attached += ['Python']

lecturer_3 = Lecturer("Jon", "Duglas")
lecturer_3.courses_attached += ['Git']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(student_1, 'Python', 8)
cool_mentor.rate_hw(student_1, 'Python', 9)
cool_mentor.rate_hw(student_1, 'Python', 7)
cool_mentor.rate_hw(student_1, 'Git', 9)
cool_mentor.rate_hw(student_1, 'Git',10)




best_student.rate_lectories(lecturer_1, 'Python', 9)
best_student.rate_lectories(lecturer_2, 'Python', 7)
student_1.rate_lectories(lecturer_1, 'Python', 10)
student_1.rate_lectories(lecturer_2, 'Python', 9)
student_1.rate_lectories(lecturer_3, 'Git', 10)

lecturer_1.midle_grades_lector()
best_student.midle_grades_student()
student_1.midle_grades_student()
print(Student.__gt__(best_student, student_1))
print(Lecturer.__gt__(lecturer_1, lecturer_3))
print(lecturer_1)
print(student_1)
print(best_student.grades)
print(lecturer_1.grades_lectur)


students = [best_student, student_1]

def average_score_course_student(course):
    midle_b = 0
    amount = 0
    for item in students:
        if course in item.courses_in_progress:
            midle = sum(item.grades[course]) / len(item.grades[course])
            midle_b += midle
            amount += 1
    average_score = m / s
    print(f"Средний балл студентов по курсу {course} - {average_score}")

average_score_course_student("Python")

lecturers = [lecturer_1, lecturer_2, lecturer_3 ]

def average_score_course_lecture(course):
    midle_b = 0
    amount = 0
    for item in lecturers:
        if course in item.courses_attached:
            midle = sum(item.grades_lectur[course]) / len(item.grades_lectur[course])
            midle_b += midle
            amount += 1
    average_score = m / s
    print(f"Средний балл лекторов по курсу {course} - {average_score}")


