# Python variables - Data types - Basic Grammar


# 1 - Variables names must make sense
# 2 - Python covention is to use lowercase letters
# 3 - Python is snake case _
# 4 - Variables names must start with a letter or _
# 5 - Following the pep8 standards

# --- Strings ---
my_favorite_game = "Skyrim"
my_first_name = "Daniel"


# --- Numbers ---

my_age = 31
my_score = 92

# --- Boolean ---
im_canadian = True
im_female = False


"""
--Data Types              --Class--    --Value--
integers                  -> int         -> 45
floating point numbers    -> float       -> 4.5
booleans                  -> bool        -> True/False
strings                   -> str         -> "Daniel Ducas-Viramontes"
list                      -> list        -> [1,2,3]
dictionary                -> dict        -> {"user_name": "awesome50", "user_id":56}
tuple                     -> tuple       -> (10,20,30)
set                       -> set         -> {"cat", 99}

"""


# integer-------------------------------------------------------
age = 31
print(age)
print(type(age))


# floats--------------------------------------------------------
grade = 9.1
print(grade)
print(type(grade))

# boolans------------------------------------------------------
alarm = True
offline = False
print(alarm, offline)
print(type(alarm))
print(type(offline))


# strings ----------------------------------------------------

movie_name = "The matrix"
print(movie_name)
print(type(movie_name))


# List ----------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 6.4, 9.3, "People"]
# Ordered
print(numbers)
print(type(numbers))


# Dictionary ----------------------------------------------------
# unordered
user_info = {"user_name": "awesome50", "user_id": 56}
print(user_info)
print(type(user_info))


# Tuple ----------------------------------------------------
# ordered
mixed_tuple = (1, 2, 3, 4, 5.6, True, "Daniel", [1, 2, 3])
print(mixed_tuple)
print(type(mixed_tuple))

# Set ----------------------------------------------------
# unordered
mixed_set = {1, 2, 3, 4, 5.6, True, "Daniel", "python"}
print(mixed_set)
print(type(mixed_set))
