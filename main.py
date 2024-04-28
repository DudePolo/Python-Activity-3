# Function Definition Practice:
# Define functions according to the following prompts. Run the Replit to verify correct output.


# 1. Function that accepts no arguments. It's called say_hello and returns nothing, just prints 'hello'.
def say_hello():
    print('hello')

say_hello()
# 2. a 'sum' function that accepts two integers and returns the sum.
def two_sum(a , b):
    print(a + b)

two_sum(12, 13)
# 3. an 'average' function that accepts two numbers and returns the average.
def number_mean(a , b):
    print((a + b) / 2)

number_mean(34, 26)
# 4. A function that accepts a first name and a last name and formats it to "{last_name}, {first_name}" (returns a string).
def full_name(firstname, lastname):
    print(firstname + ' ' + lastname)

full_name('Andres', 'Polo-Wood')
# 5. A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.
def student(firstname, lastname, grad_year, student_id):
    student_dict = [
        firstname,
        lastname,
        grad_year,
        student_id,
    ]
    print(student_dict)

student('Andres', 'Polo-Wood', '2024', '1999')
# 6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).
# ^ what a weird question
def barely_legal(x):
    if x > 18:
        print('Yes she\'s legal')
    else:
        print('Hello, my name is Chris Hansen')

barely_legal(16)
barely_legal(21)
#7. A function that accepts a string and prints the string in reverse (no return value).
my_string = 'hello world'[::-1]
print(my_string)