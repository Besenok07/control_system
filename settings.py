from school.models import Subject, Teacher, Class, Student

def add_subject():
    name = input("Введіть назву предмету: ")
    description = input("Введіть опис предмету: ")
    subject = Subject(name=name, description=description)
    subject.save()
    print("Предмет доданий успішно!")

def add_teacher():
    first_name = input("Введіть ім'я вчителя: ")
    last_name = input("Введіть прізвище вчителя: ")
    subject_name = input("Введіть назву предмету вчителя: ")
    subject = Subject.objects.get(name=subject_name)
    teacher = Teacher(first_name=first_name, last_name=last_name, subject=subject)
    teacher.save()
    print("Вчитель доданий успішно!")

def add_class():
    name = input("Введіть назву класу: ")
    year = int(input("Введіть рік навчання класу: "))
    class_obj = Class(name=name, year=year)
    class_obj.save()
    print("Клас доданий успішно!")

def add_student():
    first_name = input("Введіть ім'я учня: ")
    last_name = input("Введіть прізвище учня: ")
    class_name = input("Введіть назву класу учня: ")
    class_obj = Class.objects.get(name=class_name)
    student = Student(first_name=first_name, last_name=last_name, class_name=class_obj)
    student.save()
    print("Учень доданий успішно!")

def add_schedule():
    day_of_week = input("Введіть день тижня: ")
    start_time = input("Введіть час початку заняття: ")
    subject_name = input("Введіть назву предмету: ")
    class_name = input("Введіть назву класу: ")
    teacher_name = input("Введіть ім'я вчителя: ")
    subject = Subject.objects.get(name=subject_name)
    class_obj = Class.objects.get(name=class_name)
    teacher = Teacher.objects.get(first_name=teacher_name)
    schedule = Schedule(day_of_week=day_of_week, start_time=start_time, subject=subject, class_name=class_obj, teacher=teacher)
    schedule.save()
    print("Заняття додане успішно!")

def add_grade():
    student_name = input("Введіть ім'я учня: ")
    subject_name = input("Введіть назву предмету: ")
    grade = int(input("Введіть оцінку: "))
    date = input("Введіть дату: ")
    student = Student.objects.get(first_name=student_name)
    subject = Subject.objects.get(name=subject_name)
    grade_obj = Grade(student=student, subject=subject, grade=grade, date=date)
    grade_obj.save()
    print("Оцінка додана успішно!")