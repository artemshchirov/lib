import csv


def add_student(first_name, last_name, age):
    with open('students.csv', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first_name, last_name, age])


add_student('test first name', 'test last name', 88)


def print_students(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for student in csv_reader:
            print(student[0], student[1], student[2])


print_students('students.csv')
