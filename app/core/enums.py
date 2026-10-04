from enum import Enum

class UserRole(str, Enum):
    SUPER_ADMIN = "Super Admin"
    ORG_ADMIN = "Org Admin"
    MANAGER = "Manager"
    AGENT = "Agent"
    USER = "User"