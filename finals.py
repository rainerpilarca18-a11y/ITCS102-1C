import os

def print_statements():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("\t\t---> PRINT STATEMENTS <---")
    print("The print() function prints the specified message to the screen, or other standard output device. <---")
    print("The message can be a string, or any other object, the object will be converted into a string before written to the screen.. <---")
    print("---------------------------------------------------------------------------------------------------------------")
    
    def printing():
        os.system("cls")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> PRINTING <---")
        print("print() is commonly used to show the result of a program, debug code, or interact with the user <---")
        print("---------------------------------------------------------------------------------------------------------------")

    def string_formatting():
        os.system("cls")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> STRING FORMATTING <---")
        print("String Formatting is the easiest and most readable method.")
        print('String Formatting is the use of "f" before the string and put variables in curly braces "{}" ')
        print("Here is an Example:")
        print("age = 20")
        print('print(f"Hello user! you are {age} yrs old")')
        print("Output: Hello user!, you are 20 yrs old")
        print("---------------------------------------------------------------------------------------------------------------")

    while True:

        print('1. PRINTING')
        print('2. STRING FORMATTING')
        print('3. EXIT TO MAIN MENU')

        choice1 = int(input('Enter the number you want to open:'))

        if choice1 == 1:
            printing()
            input("Press Enter to show menu...")

        elif choice1 == 2:
            string_formatting()
            input("Press Enter to show menu...")
            
        elif choice1 == 3:
            print("Exiting to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to show menu...")
            continue


def variables():
        os.system("cls")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> VARIABLE TYPES <---")
        print("In Python, there are several built-in data types that can be used to store different kinds of values.")
        print("Here are some of the most common variable types in Python:")
        print("1. Integer (int): Represents whole numbers.")
        print("2. Float (float): Represents decimal numbers.")
        print("3. String (str): Represents sequences of characters.")
        print("4. Boolean (bool): Represents truth values, either True or False")
        print("5. List: Represents an ordered collection of items.")
        print("6. Dictionary (dict): Represents a collection of key-value pairs.")
        print("---------------------------------------------------------------------------------------------------------------")

        def integer():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> INTEGER <---")
            print("An integer is a whole number, positive or negative, without decimals.")
            print("Example: 1, -5, 42")
            print("You can perform arithmetic operations with integers.")
            print("Example:")
            print("x = 10")
            print("y = 5")
            print("print(x + y)")
            print("Output: 15")
            print("---------------------------------------------------------------------------------------------------------------")

        def float():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> FLOAT <---")
            print("A float is a number that has a decimal point.")
            print("Example: 3.14, -0.001, 2.0")
            print("You can perform arithmetic operations with floats.")
            print("Example:")
            print("x = 5.5")
            print("y = 2.0")
            print("print(x * y)")
            print("Output: 11.0")
            print("---------------------------------------------------------------------------------------------------------------")

        def string():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> STRING <---")
            print("A string is a sequence of characters enclosed in single or double quotes.")
            print("Example: 'Hello', 'Python123'")
            print("You can concatenate strings using the + operator.")
            print("Example:")
            print("greeting = 'Hello'")
            print("name = 'Rainer'")
            print("print(greeting + ' ' + name")
            print("Output: Hello Rainer")
            print("---------------------------------------------------------------------------------------------------------------")

        def boolean():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> BOOLEAN <---")
            print("A boolean represents one of two values: True or False.")
            print("Booleans are often used in conditional statements and comparisons.")
            print("Example:")
            print("is_raining = True")
            print("if is_raining:")
            print('    print("Take an umbrella!")')
            print("Output: Take an umbrella!")
            print("---------------------------------------------------------------------------------------------------------------")
        
        def list():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> LIST <---")
            print("A list is an ordered collection of items, which can be of different types.")
            print("Example: [1, 2, 3], ['apple', 'banana']")
            print("You can access list items using their index.")
            print("Example:")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("print(fruits[0])")
            print("Output: apple")
            print("---------------------------------------------------------------------------------------------------------------")

        def dictionary():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> DICTIONARY <---")
            print("A dictionary is a collection of key-value pairs.")
            print("Example: {'name': 'Rainer', 'age': 19}")
            print("You can access values using their keys.")
            print("Example:")
            print("person = {'name': 'Rainer', 'age': 19}")
            print("print(person['name'])")
            print("Output: Rainer")
            print("---------------------------------------------------------------------------------------------------------------")

        while True:

            print('1. INTEGER')
            print('2. FLOAT')
            print('3. STRING')
            print('4. BOOLEAN')
            print('5. LIST')
            print('6. DICTIONARY')
            print('7. EXIT TO MAIN MENU')

            choice2 = int(input('Enter the number you want to open:'))

            if choice2 == 1:
                integer()
                input("Press Enter to show menu...")

            elif choice2 == 2:
                float()
                input("Press Enter to show menu...")

            elif choice2 == 3:
                string()
                input("Press Enter to show menu...")

            elif choice2 == 4:
                boolean()
                input("Press Enter to show menu...")

            elif choice2 == 5:
                list()
                input("Press Enter to show menu...")

            elif choice2 == 6:
                dictionary()
                input("Press Enter to show menu...")
                
            elif choice2 == 7:
                print("Exiting to main menu...")
                break

            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to show menu...")
                continue

def operators():
        os.system("cls")
        def arithmetic_operators():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> ARITHMETIC OPERATORS <---")
            print("Arithmetic operators are used to perform mathematical operations on numeric values.")
            print("Here are the common arithmetic operators in Python:")
            print("1. Addition (+): Adds two numbers together.")
            print("2. Subtraction (-): Subtracts one number from another.")
            print("3. Multiplication (*): Multiplies two numbers.")
            print("4. Division (/): Divides one number by another.")
            print("5. Modulus (%): Returns the remainder of a division operation.")
            print("6. Exponentiation (**): Raises a number to the power of another number.")
            print("7. Floor Division (//): Divides one number by another and rounds down to the nearest whole number.")
            print("---------------------------------------------------------------------------------------------------------------")
            
        def comparison_operators():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> COMPARISON OPERATORS <---")
            print("Comparison operators are used to compare two values and return a Boolean result (True or False).")
            print("Here are the common comparison operators in Python:")
            print("1. Equal to (==): Checks if two values are equal.")
            print("2. Not equal to (!=): Checks if two values are not equal.")
            print("3. Greater than (>): Checks if the left value is greater than the right value.")
            print("4. Less than (<): Checks if the left value is less than the right value.")
            print("5. Greater than or equal to (>=): Checks if the left value is greater than or equal to the right value.")
            print("6. Less than or equal to (<=): Checks if the left value is less than or equal to the right value.")
            print("---------------------------------------------------------------------------------------------------------------")

        def logical_operators():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> LOGICAL OPERATORS <---")
            print("Logical operators are used to combine multiple Boolean expressions and return a Boolean result.")
            print("Here are the common logical operators in Python:")
            print("1. AND (and): Returns True if both expressions are True.")
            print("2. OR (or): Returns True if at least one expression is True.")
            print("3. NOT (not): Returns the opposite of the Boolean value.")
            print("---------------------------------------------------------------------------------------------------------------")

        def assignment_operators():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> ASSIGNMENT OPERATORS <---")
            print("Assignment operators are used to assign values to variables.")
            print("Here are the common assignment operators in Python:")
            print("1. = : Assigns a value to a variable.")
            print("2. += : Adds a value to a variable and assigns the result.")
            print("3. -= : Subtracts a value from a variable and assigns the result.")
            print("4. *= : Multiplies a variable by a value and assigns the result.")
            print("5. /= : Divides a variable by a value and assigns the result.")
            print("6. %= : Assigns the remainder of a variable divided by a value.")
            print("---------------------------------------------------------------------------------------------------------------")
        
        
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> OPERATORS <---")
        print("Operators are special symbols that perform specific operations on one or more operands (values or variables).")
        print("Here are some common types of operators in Python:")
        print("1. Arithmetic Operators: +, -, *, /, %, **, //")
        print("2. Comparison Operators: ==, !=, >, <, >=, <=")
        print("3. Logical Operators: and, or, not")
        print("4. Assignment Operators: =, +=, -=, *=, /=, %=")
        print("---------------------------------------------------------------------------------------------------------------")

        while True:
            print('1. ARITHMETIC OPERATORS')
            print('2. COMPARISON OPERATORS')
            print('3. LOGICAL OPERATORS')
            print('4. ASSIGNMENT OPERATORS')
            print('5. EXIT TO MAIN MENU')

            choice3 = int(input('Enter the number you want to open:'))

            if choice3 == 1:
                arithmetic_operators()
                input("Press Enter to show menu...")

            elif choice3 == 2:
                comparison_operators()
                input("Press Enter to show menu...")
                
            elif choice3 == 3:
                logical_operators()
                input("Press Enter to show menu...")

            elif choice3 == 4:
                assignment_operators()
                input("Press Enter to show menu...")

            elif choice3 == 5:
                print("Exiting to main menu...")
                break

            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to show menu...")
                continue

def conditionals():
        os.system("cls")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> CONDITIONAL STATEMENTS <---")
        print("Conditional statements are used to perform different actions based on whether a certain condition is true or false.")
        print("Here are the common conditional statements in Python:")
        print("1. if statement: Used to execute a block of code if a specified condition is true.")
        print("2. elif statement: Used to specify a new condition to test if the previous if statement was false.")
        print("3. else statement: Used to execute a block of code if all previous conditions were false.")
        print("---------------------------------------------------------------------------------------------------------------")

        def if_statement():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> IF STATEMENT <---")
            print("The if statement is used to test a specific condition. If the condition is true, the block of code inside the if statement is executed.")
            print("Here is an Example:")
            print("age = 18")
            print("if age >= 18:")
            print('    print("You are eligible to vote.")')
            print("elif age == 17:")
            print('    print("You will be eligible to vote next year.")')
            print("else:")
            print('    print("You are not eligible to vote yet.")')
            print("The output will be: You are eligible to vote.")
            print("---------------------------------------------------------------------------------------------------------------")
       
        def elif_statement():
                os.system("cls")
                print("---------------------------------------------------------------------------------------------------------------")
                print("\t\t---> ELIF STATEMENT <---")
                print("The elif statement is used to test multiple conditions. If the previous if statement was false, the elif condition is checked.")
                print("Here is an Example:")
                print("age = 17")
                print("if age >= 18:")
                print('    print("You are eligible to vote.")')
                print("elif age == 17:")
                print('    print("You will be eligible to vote next year.")')
                print("else:")
                print('    print("You are not eligible to vote yet.")')
                print("The output will be: You will be eligible to vote next year.")
                print("---------------------------------------------------------------------------------------------------------------")

        def else_statement():
                os.system("cls")
                print("---------------------------------------------------------------------------------------------------------------")
                print("\t\t---> ELSE STATEMENT <---")
                print("The else statement is used to execute a block of code if the condition in the if statement is false.")
                print("Here is an Example:")
                print("age = 16")
                print("if age >= 18:")
                print('    print("You are eligible to vote.")')
                print("elif age == 17:")
                print('    print("You will be eligible to vote next year.")')
                print("else:")
                print('    print("You are not eligible to vote yet.")')
                print("The output will be: You are not eligible to vote yet.")
                print("---------------------------------------------------------------------------------------------------------------")

        while True:

            print('1. IF STATEMENT')
            print('2. ELIF STATEMENT')
            print('3. ELSE STATEMENT')
            print('4. EXIT TO MAIN MENU')

            choice_02 = int(input('Enter the number you want to open:'))

            if choice_02 == 1:
                if_statement()
                input("Press Enter to show menu...")

            elif choice_02 == 2:
                elif_statement()
                input("Press Enter to show menu...")

            elif choice_02 == 3:
                else_statement()
                input("Press Enter to show menu...")

            elif choice_02 == 4:
                print("Exiting to main menu...")
                break

            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to show menu...")
                continue

def loops():
        os.system("cls")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> LOOPS <---")
        print("Loops are used to execute a block of code repeatedly as long as a certain condition is met.")
        print("Here are the common types of loops in Python:")
        print("1. for loop: Used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.")
        print("2. while loop: Repeats a block of code as long as a specified condition is true.")
        print("3. nested loop: A loop inside another loop.")
        print("---------------------------------------------------------------------------------------------------------------")

        def for_loop():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> FOR LOOP <---")
            print("The for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.")
            print("Here is an Example:")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("for fruit in fruits:")
            print('    print(fruit)')
            print("The output will be:")
            print("apple")
            print("banana")
            print("cherry")
            print("---------------------------------------------------------------------------------------------------------------")

        def while_loop():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> WHILE LOOP <---")
            print("The while loop repeats a block of code as long as a specified condition is true.")
            print("Here is an Example:")
            print("count = 1")
            print("while count <= 5:")
            print('    print(count)')
            print('    count += 1')
            print("The output will be:")
            print("1")
            print("2")
            print("3")
            print("4")
            print("5")
            print("---------------------------------------------------------------------------------------------------------------")

        def nested_loop():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> NESTED LOOP <---")
            print("A nested loop is a loop inside another loop.")
            print("Here is an Example:")
            print("for i in range(1, 4):")
            print("    for x in range(1, 4):")
            print('        print(f"i: {i}, x: {x}")')
            print("The output will be:")
            print("i: 1, x: 1")
            print("i: 1, x: 2")
            print("i: 1, x: 3")
            print("i: 2, x: 1")
            print("i: 2, x: 2")
            print("i: 2, x: 3")
            print("i: 3, x: 1")
            print("i: 3, x: 2")
            print("i: 3, x: 3")
            print("---------------------------------------------------------------------------------------------------------------")

        while True:
            print('1. FOR LOOP')
            print('2. WHILE LOOP')
            print('3. NESTED LOOP')
            print('4. EXIT TO MAIN MENU')

            choice4 = int(input('Enter the number you want to open:'))

            if choice4 == 1:
                for_loop()
                input("Press Enter to show menu...")

            elif choice4 == 2:
                while_loop()
                input("Press Enter to show menu...")

            elif choice4 == 3:
                nested_loop()
                input("Press Enter to show menu...")

            elif choice4 == 4:
                print("Exiting to main menu...")
                break

            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to show menu...")
                continue

def lists():
        os.system("cls")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> LISTS <---")
        print("A list is an ordered collection of items, which can be of different types.")
        print("Here are some common operations you can perform on lists in Python:")
        print("---------------------------------------------------------------------------------------------------------------")

        def creating_list():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> CREATING A LIST <---")
            print("You can create a list by placing comma-separated values inside square brackets [].")
            print("Here is an Example:")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("print(fruits)")
            print("Output: ['apple', 'banana', 'cherry']")
            print("---------------------------------------------------------------------------------------------------------------")

        def accessing_list_items():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> ACCESSING LIST ITEMS <---")
            print("You can access list items using their index. The index starts at 0.")
            print("Here is an Example:")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("print(fruits[0])")
            print("Output: apple")
            print("print(fruits[1])")
            print("Output: banana")
            print("print(fruits[2])")
            print("Output: cherry")
            print("---------------------------------------------------------------------------------------------------------------")

        def modifying_list_items():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> MODIFYING LIST ITEMS <---")
            print("You can modify list items by accessing them using their index and assigning a new value.")
            print("Here is an Example:")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("fruits[1] = 'orange'")
            print("print(fruits)")
            print("Output: ['apple', 'orange', 'cherry']")
            print("---------------------------------------------------------------------------------------------------------------")

        def adding_items():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> ADDING ITEMS TO A LIST <---")
            print("You can add items to a list using the append() method or the insert() method.")
            print("Here is an Example:")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("fruits.append('orange')")
            print("print(fruits)")
            print("Output: ['apple', 'banana', 'cherry', 'orange']")
            print("fruits.insert(1, 'kiwi')")
            print("print(fruits)")
            print("Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']")
            print("---------------------------------------------------------------------------------------------------------------")

        def removing_items():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> REMOVING ITEMS FROM A LIST <---")
            print("You can remove items from a list using the remove() method or the pop() method.")
            print("Here is an Example:")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("fruits.remove('banana')")
            print("print(fruits)")
            print("Output: ['apple', 'cherry']")
            print("fruits.pop(0)")
            print("print(fruits)")
            print("Output: ['cherry']")
            print("---------------------------------------------------------------------------------------------------------------")

        def looping_through_list():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> LOOPING THROUGH A LIST <---")
            print("You can loop through a list using a for loop.")
            print("Here is an Example:")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("for fruit in fruits:")
            print('    print(fruit)')
            print("The output will be:")
            print("apple")
            print("banana")
            print("cherry")
            print("---------------------------------------------------------------------------------------------------------------")

        while True:
            print('1. CREATING A LIST')
            print('2. ACCESSING LIST ITEMS')
            print('3. MODIFYING LIST ITEMS')
            print('4. ADDING ITEMS TO A LIST')
            print('5. REMOVING ITEMS FROM A LIST')
            print('6. LOOPING THROUGH A LIST')
            print('7. EXIT TO MAIN MENU')

            choice5 = int(input('Enter the number you want to open:'))

            if choice5 == 1:
                creating_list()
                input("Press Enter to show menu...")

            elif choice5 == 2:
                accessing_list_items()
                input("Press Enter to show menu...")

            elif choice5 == 3:
                modifying_list_items()
                input("Press Enter to show menu...")

            elif choice5 == 4:
                adding_items()
                input("Press Enter to show menu...")

            elif choice5 == 5:
                removing_items()
                input("Press Enter to show menu...")

            elif choice5 == 6:
                looping_through_list()
                input("Press Enter to show menu...")

            elif choice5 == 7:
                print("Exiting to main menu...")
                break

            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to show menu...")
                continue

def functions():
        os.system("cls")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> FUNCTIONS <---")
        print("A function is a block of organized, reusable code that is used to perform a single, related action.")
        print("Here are some common aspects of functions in Python:")
        print("---------------------------------------------------------------------------------------------------------------")

        def defining_function():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> DEFINING A FUNCTION <---")
            print("You can define a function using the def keyword followed by the function name and parentheses ().")
            print("Here is an Example:")
            print("def greet():")
            print('    print("Hello, World!")')
            print("---------------------------------------------------------------------------------------------------------------")

        def calling_function():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> CALLING A FUNCTION <---")
            print("You can call a function by using its name followed by parentheses ().")
            print("Here is an Example:")
            print("def greet():")
            print('    print("Hello, World!")')
            print("greet()")
            print("The output will be: Hello, World!")
            print("---------------------------------------------------------------------------------------------------------------")

        def function_parameters():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> FUNCTION PARAMETERS AND ARGUMENTS <---")
            print("You can define parameters in the function definition and pass arguments when calling the function.")
            print("Here is an Example:")
            print("def greet(name):")
            print('    print(f"Hello, {name}!")')
            print("greet('Rainer')")
            print("The output will be: Hello, Rainer!")
            print("---------------------------------------------------------------------------------------------------------------")

        def return_values():
            os.system("cls")
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> RETURN VALUES <---")
            print("You can use the return statement to return a value from a function.")
            print("Here is an Example:")
            print("def add(a, b):")
            print("    return a + b")
            print("result = add(5, 3)")
            print("print(result)")
            print("Output: 8")
            print("---------------------------------------------------------------------------------------------------------------")

        while True:
            print('1. DEFINING A FUNCTION')
            print('2. CALLING A FUNCTION')
            print('3. FUNCTION PARAMETERS AND ARGUMENTS')
            print('4. RETURN VALUES')
            print('5. EXIT TO MAIN MENU')

            choice6 = int(input('Enter the number you want to open:'))

            if choice6 == 1:
                defining_function()
                input("Press Enter to show menu...")
                
            elif choice6 == 2:
                calling_function()
                input("Press Enter to show menu...")

            elif choice6 == 3:
                function_parameters()
                input("Press Enter to show menu...")

            elif choice6 == 4:
                return_values()
                input("Press Enter to show menu...")

            elif choice6 == 5:
                print("Exiting to main menu...")
                break

            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to show menu...")
                continue

        

while True:
    os.system('cls')
    print("\t\t***********************************************************************************************")
    print("\t\t\t\t---> WELCOME TO RAINER PILARCA'S FINAL PROJECT <---")
    print("\t\t---> THIS IS A PROGRAM THAT CONTAINS A BRIEF SUMMARY OF THE BASICS TOPICS OF PYTHON <---")
    print("\t\t\t---> THIS IS ALSO A SHORT RECALL ON WHAT TOPICS I'VE MASTERED A LITTLE <---")
    print("\t\t***********************************************************************************************")
    print('1. PRINT STATEMENTS')
    print('2. VARIABLES')
    print('3. OPERATORS')
    print('4. CONDITIONALS')
    print('5. LOOPS')
    print('6. LISTS')
    print('7. FUNCTIONS')
    print('8. EXIT')
    
    choice = int(input('Enter the number you want to open:'))

    if choice == 1:
        print_statements()
        input("Press Enter to go back...")

    elif choice == 2:
        variables()
        input("Press Enter to go back...")
    
    elif choice == 3:
        operators()
        input("Press Enter to go back...")

    elif choice == 4:
        conditionals()
        input("Press Enter to go back...")

    elif choice == 5:
        loops()
        input("Press Enter to go back...")

    elif choice == 6:
        lists()
        input("Press Enter to go back...")

    elif choice == 7:
        functions()
        input("Press Enter to go back...")

    elif choice == 8:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to go back...")
        continue