# --------String Methods------------


# 1 - len()
address = "Canada"
print(len(address))


# 2 - [] Notation
print(address[0])
print(address[5])
print(address[0:4])
print(address[-5: 5])
print(address[:])
print(address[:5])

# 3 - Concatenation
country = "Canada"
city = "Ottawa"
full_address = city + " " + country
print(full_address)


# 4 - upper()
print(address.upper())


# 5 - lower()
print(address.lower())


# 6 - title()
print(full_address.title())

# 7 - strip
job = "                      Programmer"
print(job.strip())
print(job.lstrip())
print(job.rstrip())


#8- find()
print(address.find("d"))
print(address.find("C"))


# 9 replace()
print(address.replace("C", "Z"))

# 10 - in operator
print("a" in country)
print("f" in country)


# 12 - not operator
print("a"not in country)
print("f" not in country)
