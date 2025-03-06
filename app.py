import math
print("Hello World")
print("*😒" * 10)

X = 1

y = 2

unit_price = 3

course = "Software \"Devolepment"
# len function gives the length
print(len(course))
# [:] can give the string from inedx to index
print(course[0])
print(course[-1])
print(course[5:])
print(course[:5])
print(course[:])
# -------------------------------------


first = "Thor"
last = "Odin"
# concatination
full = f"{first} {last} {len(last)}"
print(full)
# ----------------------------------------


course2 = "  python progammin  "
Upper_course2 = course2.upper()
Lower_course2 = course2.lower()
print(Upper_course2)
print(Lower_course2)
print(course2.title())
# .strip can be used to remove white spaces
print(course2.strip())
print(course2.find("rog"))
print(course2.replace("p", "y"))
# find if a srting is avilable with true or false
print("proi" in course2)
print("proi" not in course2)
# ------------------------------------------

# Numbers
x = 1  # int
y = 1.5  # float
z = 5+6j  # complex

print(3+5)
print(9-5)
print(10*2)
print(10/3)
print(10//3)  # the reult in int
print(10 % 3)  # modular
print(10**3)  # exponent

x += 3
print(x)


# Function for numbers


print(round(6.5))
print(abs(-452))

print(math.ceil(5.4))
# ---------------------

k = input("k: ")
t = int(k)+1
print(f"k: {k}, t: {t}")

# int(x)
# float(x)
# bool(x)
# str(x)
