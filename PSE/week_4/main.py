from database import create_table, create_table_course, create_table_junction
from user_manager import add_user, view_users, search_user, delete_user
from course_manager import add_course, view_courses, search_course

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Search User by ID and Name")
    print("5. Delete User by ID")
    print("\n==== Course Manager ====")
    print("6. Add Course")
    print("7. View All Courses")
    print("8. Search Course by ID and Name")
    print("9. Exit")

def main():
    create_table()
    create_table_course()
    create_table_junction()
    while True:
        menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            id = input("Enter id to search: ")
            name = input("Enter name to search: ")
            users = search_user(id, name)
            for user in users:
                print(user)
        elif choice == '5':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '6':
            name = input("Enter course name: ")
            unit = input("Enter course unit: ")
            user_id = input("Enter user ID: ")
            if unit.isdigit() and user_id.isdigit():
                add_course(name, int(unit), int(user_id))
            else:
                print("Please enter a valid number for unit and user ID.")
        elif choice == '7':
            courses = view_courses()
            for course in courses:
                print(course)
        elif choice == '8':
            course_id = input("Enter course ID: ")
            user_name = input("Enter user name: ")
            course = search_course(course_id, user_name)
            print(course)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
