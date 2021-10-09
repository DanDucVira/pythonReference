

# --------------------## Ternary Operator ## --------------------

score = 74


#  First Version--------------------- Amateur

# if score >= 75:
#     print("Passed")
# else:
#     print("Failed")


# Second Version -------------------- More Professional

if score >= 75:
    result = "Passed"
else:
    result = "Failed"


print(result)


# Third Version ->> Ternary Operator

result = "Passed" if score >= 75 else "Failed"
print(result)
