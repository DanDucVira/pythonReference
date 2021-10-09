

#--------------------------------------#
# Conditional Statements ##---------------


"""
if (boolean expression) :
    execute the statements
"""


# --------------Example ->>> check for a single condition

temperature = 35

if temperature > 30:
    print("It is a good day for walking")


# ------------------Example ->>> check for 2 conditions

if temperature > 25:
    print("Awesome")
else:
    print("Cold")


# ------------Example ->>>> check for multiple conditions


if temperature > 35:
    print("Hot")
elif temperature > 25:
    print("Awesome")
else:
    print("cold")
