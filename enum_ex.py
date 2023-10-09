from enum import Enum

class level(Enum):
    Beginner        = 1
    Intermediate    = 2
    Professional    = 3
print(level.Beginner.name)
print(level.Beginner.value)