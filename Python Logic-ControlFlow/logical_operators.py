

#-------------------------Logical Operators--------------------------#


"""
1- and
2- or
3- not
"""


# Example 1:   ->>>> Processing Loans ->>> and Logical Operator

high_income = True
good_credit = False

if high_income and good_credit:
    print("Eligible For loan")
else:
    print("Not Eligible For loan")


# Example 2:   ->>>> Processing Loans ->>> or Logical Operator

high_income = True
good_credit = False

if high_income or good_credit:
    print("Eligible For loan")
else:
    print("Not Eligible For loan")


# Example 3:   ->>>> Processing Loans ->>> not Logical Operator

# high_income = True
# good_credit = True
student = False

if not student:
    print("Eligible For loan")
else:
    print("Not Eligible For loan")
