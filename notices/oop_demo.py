# notices/oop_demo.py

# Base Class
class User:
    def __init__(self, name):
        self.name = name

    def can_create_notice(self):
        return False

    def show_role(self):
        return "General User"


# Derived Class 1 - Admin
class Admin(User):

    # Method Overriding
    def can_create_notice(self):
        return True

    def show_role(self):
        return "Admin: Can manage notices"


# Derived Class 2 - Student
class Student(User):

    # Method Overriding
    def can_create_notice(self):
        return False

    def show_role(self):
        return "Student: Can view notices"


# Main Program (Polymorphism)
def main():

    # Creating objects
    u1 = Admin("Ravi")
    u2 = Student("Amit")
    u3 = Student("Neha")

    # Store in single list
    users = [u1, u2, u3]

    print("\nUser Details:\n")

    # Polymorphism
    for user in users:

        print("Name:", user.name)
        print("Role:", user.show_role())

        if user.can_create_notice():
            print("Permission: Can create notice")
        else:
            print("Permission: Cannot create notice")

        print("-" * 40)


# Run Program
if __name__ == "__main__":
    main()
