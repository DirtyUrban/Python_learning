#Day 2:30 days of programming
(first_name)='Urban'
last_name="Praper"
full_name=first_name+" "+last_name
country="Slovenia"
city="Mezica"
age=18,
year=2026,
is_married=False
is_true=True
first_name, last_name, country, city, age, year, is_married, is_true = 'Urban', 'Praper', 'Slovenia', 'Mezica', 18, 2026, False, True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))   
print(type(is_married)) 
print(type(is_true))

print(len(first_name))
print(len(last_name))

num_one=5
num_two=4
total=num_one+num_two
diff=num_one-num_two
print(total,diff)
product=num_one*num_two
division=num_one/num_two
print(product, division)
remainder=num_one%num_two
print(remainder)
exp=num_one**num_two
floor_divison=num_one//num_two
print(floor_divison)

import math
radius_input=input("Radius:")
radius_input=float(radius_input)
area_of_the_circle=radius_input*math.pi**2
circum_of_the_circle=radius_input*math.pi*2

print("area is",area_of_the_circle,"m2")



first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

print(first_name, last_name, country, age)

