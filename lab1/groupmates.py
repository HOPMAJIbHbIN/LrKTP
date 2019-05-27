#coding:utf-8
groupmates = [
    {
        "name": u"Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": u"Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": u"Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 5, 5]
    },
        {
        "name": u"Олег",
        "group": "912-2",
        "age": 20,
        "marks": [5, 3, 3, 4, 5]
    },
        {
        "name": u"Анастасия",
        "group": "912-1",
        "age": 18,
        "marks": [5, 3, 4, 4, 4]
    },
        {
        "name": u"Даша",
        "group": "912-1",
        "age": 18,
        "marks": [3, 3, 3, 4, 3]
    }
    
]
def print_students(students):
    print u"Имя студента".ljust(15),\
          u"Группа".ljust(8),\
          u"Возраст".ljust(8),\
          u"Оценка".ljust(20)
    for student in students:
        print \
              student["name"].ljust(15),\
              student["group"].ljust(8),\
              str(student["age"]).ljust(8),\
              str(student["marks"]).ljust(20)
        print "\n"

print_students(groupmates)

def filter_students(students):
    print u"Введите среднюю оценку:"
    a_sr=int(raw_input())
    TrueStudents=[]
    print u"Список студентов, удовлетворяющих условию средней оценки"
    for student in students:
        l=len(student["marks"])
        k=sum(student["marks"])
        if (k/l)>=a_sr:
            TrueStudents.append(student)
    print_students(TrueStudents)
            
filter_students(groupmates)
