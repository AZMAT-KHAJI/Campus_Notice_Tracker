# Base Class
class UserRole:
    def can_create_notice(self):
        return False


# Derived Class 1
class AdminRole(UserRole):
    def can_create_notice(self):
        return True


# Derived Class 2
class StudentRole(UserRole):
    def can_create_notice(self):
        return False


# Factory Function
def get_user_role(user):
    """
    Returns role object based on Django user
    """

    if user.is_staff:
        return AdminRole()
    else:
        return StudentRole()
