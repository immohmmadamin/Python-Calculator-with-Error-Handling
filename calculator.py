def culculator():
    try:
        num1 = float(input("first number"))
        opreator = input("enter your opreator (+,-,/,*)")
        num2 = float(input("Second number"))
        if opreator == "+":
            print(num1 + num2)
        elif opreator == "-":
            print(num1 - num2)
        elif opreator == "*":
            print(num1 * num2)
        elif opreator == "/":
            if num2 == "0":
                raise ZeroDivisionError
            print(num1 / num2)
        else:
            print("invalid value")
    except ValueError:
        print("invalid input")
    except ZeroDivisionError:
        print(" cannot be divided by zero")
culculator()

        
            
