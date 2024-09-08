import django_setup
from school.models import Subject, Class, Teacher, Student

math = Subject.objects.create(
    name="Математика"
)
physics = Subject.objects.create(
    name="Фізика"
)

teacher_1 = Teacher.objects.create(
    name="Олег",
    middle_name="Петрович",
    subject=math
)
teacher_2 = Teacher.objects.create(
    name="Наталія",
    middle_name="Івановна",
    subject=physics
)

class_8a = Class.objects.create(
    grade=8,
    letter='a'
)
class_11b = Class.objects.create(
    grade=11,
    letter='b'
)

student_1 = Student.objects.create(
    name="Дмитро",
    surname="Шевченко",
    in_class=class_8a
)
student_2 = Student.objects.create(
    name="Олена",
    surname="Коваленко",
    in_class=class_11b
)

print(Teacher.objects.all())
print(Student.objects.all())
