class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress \
                and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average_grade(self):
        #Student.grades=self.grades

        A = len(self.grades.values())
        B = list(self.grades.values())
        C = []
        for i in range(0, A):
            C += B[i]
        average = sum(C) / len(C)
        return average
    def __str__(self):
        to_return = ', '.join(self.courses_in_progress)
        to_return2 = ', '.join(self.finished_courses)
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname+\
               '\nСредняя оценка за домашние задания: ' + \
               str(self.average_grade())+'\nКурсы в процессе изучения ' + str(to_return)+\
               '\nЗавершенные курсы ' + str(to_return2)


    def __lt__(self, other):
        print(self.surname+" имеет меньшие оценки за домашние задания?")
        print(self.average_grade() < other.average_grade())
        return self.average_grade() < other.average_grade()
    def __gt__(self, other):
        print(self.surname+" имеет большие оценки за домашние задания?")
        print(self.average_grade() > other.average_grade())
        return self.average_grade() > other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def average_grade(self):
        #Lecturer.grades=self.grades
        A = len(self.grades.values())
        B = list(self.grades.values())
        C = []
        for i in range(0, A):
            C += B[i]
        average = sum(C) / len(C)
        return average
    def __str__(self):
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname+\
               '\nСредняя оценка за лекции: ' + \
               str(self.average_grade())
    def __lt__(self, other):
        print(self.surname+" имеет меньше оценки за лекции?")
        print(self.average_grade() < other.average_grade())
        return self.average_grade() < other.average_grade()
    def __gt__(self, other):
        print(self.surname+" имеет большие оценки за лекции?")
        print(self.average_grade() > other.average_grade())
        return self.average_grade() > other.average_grade()
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return 'Имя:' + self.name + '\nФамилия:' + str(self.surname)




#Данные для класса Студенты
perviy_student = Student ('Paul', 'Molt')
perviy_student.courses_in_progress += ['Python', "Blender"]
perviy_student.finished_courses += ['C']

vtoroy_student = Student ("Ivan", "Ryaboy")
vtoroy_student.courses_in_progress += ['C++']
vtoroy_student.finished_courses += ['C#']


# Данные для класса Лекторы
# Даём имена и фамилии лекторам
perviy_lecturer = Lecturer('Vasya','Siniy')
perviy_lecturer.courses_attached += ['Python']

vtoroy_lecturer = Lecturer("Syzan", "Shtosh")
vtoroy_lecturer.courses_attached += ['C++', 'Blender']

# Данные для класса Эксперты
# Даём имена и фамилии для экспертов
perviy_expert = Reviewer('Revy','Expertov')
perviy_expert.courses_attached += ['Python', 'Blender', 'C++']

vtoroy_expert = Reviewer ('Bazz', "Lighter")
vtoroy_expert.courses_attached += ['C++', 'Blender', 'Python']

# Выставление оценок
perviy_student.rate_lector(perviy_lecturer, 'Python', 5)
perviy_student.rate_lector(perviy_lecturer, 'C++', 7)
perviy_student.rate_lector(vtoroy_lecturer, 'Blender', 3)

vtoroy_student.rate_lector(perviy_lecturer, 'Python', 3)
vtoroy_student.rate_lector(perviy_lecturer, 'Blender', 6)
vtoroy_student.rate_lector(vtoroy_lecturer, "C++", 9)
vtoroy_student.rate_lector(vtoroy_lecturer, "Blender", 2)


perviy_expert.rate_hw(perviy_student, 'Python', 10)
vtoroy_expert.rate_hw(perviy_student, "Blender", 1)
vtoroy_expert.rate_hw(perviy_student, 'Python', 6)
vtoroy_expert.rate_hw(vtoroy_student, "C++", 7)
vtoroy_expert.rate_hw(vtoroy_student, "Blender", 5)


print("\nСтуденты: ")
print(perviy_student)
print(vtoroy_student)
print("\nЛекторы: ")
print(perviy_lecturer)
print(vtoroy_lecturer)
print("\nЭксперты: ")
print(perviy_expert)
print(vtoroy_expert)

student_list = [vars(perviy_student),vars(vtoroy_student)]
lecture_list = [vars(perviy_lecturer),vars(vtoroy_lecturer)]
leng_student = len(student_list)
leng_lecture = len(lecture_list)
# for i in range(0,leng_student):
#     print(student_list[i]['grades']['Python'])
# for j in range (0,leng_lecture):
#      print(lecture_list[i]['grades'])

#print(student_list)
#print(lecture_list[0]['grades']['Python'])


def ocenka_lectorov(lecture_list,kurs):
    average_grade=[]
    for lector in lecture_list:
        average_grade.extend(lector.grades.get(kurs, []))
    if average_grade:
        print(f"Средняя оценка студентов по курсу {kurs}: {sum(average_grade) / len(average_grade):.1f}")
    else:
        print(f"Нет оценок студентов по курсу {kurs}")

def ocenka_studentov(student_list,kurs):
    average_grade=[]
    for student in student_list:
        average_grade.extend(student.grades.get(kurs, []))
    if average_grade:
        print(f"Средняя оценка студентов по курсу {kurs}: {sum(average_grade) / len(average_grade):.1f}")
    else:
        print(f"Нет оценок студентов по курсу {kurs}")

ocenka_lectorov(lecture_list,'Blender')
ocenka_studentov(student_list,'Python')

# print(perviy_student.grades)
# print(vtoroy_student.grades)
#


print("\nСравнение оценок студентов за дз: ")

is_lt1 = (perviy_student < vtoroy_student)
is_gt1 = (perviy_student > vtoroy_student)

is_lt2 = (vtoroy_student < perviy_student)
is_gt2 = (vtoroy_student > perviy_student)

print("\nСравнение оценок лекторов за лекции : ")

is_lt3 = (perviy_lecturer < vtoroy_lecturer)
is_gt3 = (perviy_lecturer > vtoroy_lecturer)

is_lt4 = (vtoroy_lecturer < perviy_lecturer)
is_gt4 = (vtoroy_lecturer > perviy_lecturer)

