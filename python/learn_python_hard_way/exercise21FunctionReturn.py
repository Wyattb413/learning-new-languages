def add(a,b):
    print "Adding %d + %d" % (a,b)
    return (a+b)

def subtract(a,b):
    print "Subtracting %d - %d" % (a,b)
    return (a-b)

def multiply(a, b):
    print "Multiplying %d * %d" % (a,b)
    return (a*b)

def divide(a, b):
    print "Dividing %d / %d" % (a,b)
    return (a/b)


print "Let's do some math with just functions!"

# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)
#
# print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
#
# print "Here is a puzzle..."
#
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#
# print "That becomes: ", what, "Can you do it by hand?"

def invalid_input():
    print "Please Select From the Available Opperations: \nWould you like to Add (a), Subtract (s), Multiply (m), or Divide (d)?"
    users_operation = raw_input("> ")
    choose_operation()

def choose_operation():
    print "Would you like to Add (a), Subtract (s), Multiply (m), or Divide (d)?"
    users_operation = raw_input("> ")

    if users_operation == 'a' or users_operation == 'add' or users_operation == 'Add':
        first_opperand = float(raw_input("Enter your first opperand: "))
        second_opperand = float(raw_input("Enter your Second opperand: "))
        print add(first_opperand, second_opperand)
        choose_operation()
    elif users_operation == 's' or users_operation == 'subtract' or users_operation == 'Subtract':
        first_opperand = float(raw_input("Enter your first opperand: "))
        second_opperand = float(raw_input("Enter your Second opperand: "))
        print subtract(first_opperand, second_opperand)
        choose_operation()
    elif users_operation == 'm' or users_operation == 'multiply' or users_operation == 'Multiply':
        first_opperand = float(raw_input("Enter your first opperand: "))
        second_opperand = float(raw_input("Enter your Second opperand: "))
        print multiply(first_opperand, second_opperand)
        choose_operation()
    elif users_operation == 'd' or users_operation == 'divide' or users_operation == 'Divide':
        first_opperand = float(raw_input("Enter your first opperand: "))
        second_opperand = float(raw_input("Enter your Second opperand: "))
        print divide(first_opperand, second_opperand)
        choose_operation()
    else:
        invalid_input()

choose_operation()
