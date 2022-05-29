num1 = 42   #variable declartion
num2 = 2.3  #variable declartion
boolean = True  #Data Type Primitive Boolean
string = 'Hello World'  #Data Type Primitive String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #Data Type Compsit List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #Data Types Composit Tuples
fruit = ('blueberry', 'strawberry', 'banana')   #Data Type Compsit Dictionary
print(type(fruit))  #initialize
print(pizza_toppings[1])    #access value
pizza_toppings.append('Mushrooms')  #add value
print(person['name'])   #initialize
person['name'] = 'George'   #change value
person['eye_color'] = 'blue'    #adding value
print(fruit[2]) #access value

if num1 > 45:                   #conditional 01 if
    print("It's greater")
else:                           #conditional 01 else
    print("It's lower")

if len(string) < 5:             #conditional 02 if
    print("It's a short word!")
elif len(string) > 15:          #conditional 02 else if
    print("It's a long word!")
else:                           #conditional 02 else
    print("Just right!")

for x in range(5):              #for loop start
    print(x)                    
for x in range(2,5):            
    print(x)
for x in range(2,10,3):
    print(x)                    #for loop end
x = 0
while(x < 5):                   #while loop start
    print(x)
    x += 1                      #while loop increment

pizza_toppings.pop()            #calls pop function
pizza_toppings.pop(1)           #removes the 2nd item in pizza toppings

print(person)                   
person.pop('eye_color')            #prints person attributes, removes eye_color attribute, prints peron attributes
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue                    #for each topping in pizza toppings > if pepperoni continue, when olives stop listing toppings
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):       #function stores "hello" x10
        print('Hello')

print_hello_ten_times()         #calls function, outputs "hello" x10

def print_hello_x_times(x):
    for num in range(x):        # function that will run "hello" how ever many times it is passed
        print('Hello')

print_hello_x_times(4)          # calls prior function with a argument of 4, outputs "hello" x4

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):        # fuction that will output "hello" either or a value or 10x   
        print('Hello')

print_hello_x_or_ten_times()    #calls function, outputs "hello" x10
print_hello_x_or_ten_times(4)   #calls function, outputs "hello" x4


"""
Bonus section
"""

# print(num3)   --- outputs value of num3 (72)
# num3 = 72 
# fruit[0] = 'cranberry'    sets array 0 to be cranberry instead
# print(person['favorite_team'])    
# print(pizza_toppings[7])  error
#   print(boolean)  true or false depending on boolean 
# fruit.append('raspberry') adds respberry to fruit array
# fruit.pop(1) removes fruit[1]