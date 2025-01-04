from enum import Enum

class Category(Enum):
    PERSONAL = "personal"
    BUSSINESS = "bussiness"
    FAMILY = "family"
    MISCELLANEOUS="miscellaneous"
    
class Status(Enum):
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"

class Priorities(Enum):
    HIGH = "high"
    LOW = "low"
    MIDDLE = "middle"
