from .settings import add_subject, add_teacher, add_class, add_student, add_schedule, add_grade
def main():
    while True:
        print("Меню:")
        print("0. Вийти")
        print("1. Додати предмет")
        print("2. Додати вчителя")
        print("3. Додати клас")
        print("4. Додати учня")
        print("5. Додати заняття в розклад")
        print("6. Додати оцінку")
        print("7. Вийти")
        choice = input("Введіть свій вибір: ")
        if choice == "0":
            break
        elif choice == "1":
            add_subject()
        elif choice == "2":
            add_teacher()
        elif choice == "3":
            add_class()
        elif choice == "4":
            add_student()
        elif choice == "5":
            add_schedule()
        elif choice == "6":
            add_grade()
        elif choice == "7":
            break
        else:
            print("Неправильний вибір. Будь ласка, спробуйте знову.")

if __name__ == "__main__":
    main()