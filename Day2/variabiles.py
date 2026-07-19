first_name="Urban" 
last_name="Praper"
age=18,
city="Mezica"
personal_info={
    "first_name": "Urban",
    "last_name": "Praper",
    "age": 18,
    "city": "Mezica"
}

print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('City: ', city)
print('Age: ', age)
print('Person information: ', personal_info)

first_name, last_name, country, age, is_married = 'Urban', 'Praper', 'Mezica', 18, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

first_name=input('What is your first name? ')
age=input("How old are you?")
print("My name is", first_name)