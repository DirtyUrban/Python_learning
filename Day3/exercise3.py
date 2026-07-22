age=18
height=180.0
complex_number=1+2j

print(type(age))
print(type(height))
print(type(complex_number))

side_a=0.5
side_b=float(input('Enter base:'))
side_h=float(input('Enter height:'))
print('The area of the triangle is:', side_a*side_b*side_h)

side_a=float(input("Enter side a:"))
side_b=float(input("Enter side b:"))
side_c=float(input("Enter side c:"))
print("The perimeter of the triangle is", side_a+side_b+side_c)

#naloga6
side_a=float(input("Enter lenght:"))
side_b=float(input("Enter width:"))
print("Its area is:", side_a*side_b)
print("Its perimeter is:", 2*(side_a+side_b))

#naloga8
slope=2
y_interceptor=-2
x_interceptor=1
print("Slope:",slope)
print("Y-interceptor:",y_interceptor)
print("X-interceptor:", x_interceptor)

#naloga9
x1=2
x2=6
y1=2
y2=10
slope2= y2-y1/x2-x1
euclidean_distance=((x2-x1)*2+(y2-y1)*2)*0.5

print("Slope is:",slope2)
print("Euclidean distane is:",euclidean_distance)


#naloga10
print(slope==slope2)
print(slope>slope2)
print(slope<slope2)

#naloga11
x=input("Select value x:")
y=x**2+6*x*9

if y==0:
    print("The value is 0")
else:
    print("Try another one:")

#naloga12
print(len("python"))
print(len("dragon"))

print(len("python"))==print(len("dragon"))

#nalog13
"on" in "python"
"on" in "dragon"
print("on" in "python" and "on" in "dragon")

#14naloga
print("jargon" in "I hope this course is not full of jargon")

#16naloga
print(len("python"))
print(float(len("python")))
print(str(len("python")))

#17
number=int(input("Enter number:"))
if number%2==0:
    print("Its even.")
else:
    print("Its odd.")


#18
num1=7//3
num2=2.7
num2=int(num2)
print(num1==num2)


#19
num1="10"
num2=10
print(num1==num2)

#20
result = int(float('9.8'))
print(result == 10)


#21
h=input("Enter hours:")
rph=input("Enter rate per hour:")
h=int(h)
rph=int(rph)

print("Your weekly earning is",h*rph)

#22
y=input("Enter number of years you have lived:")
y=int(y)
print("You have lived for",y*365*24*60*60,"seconds")


      





