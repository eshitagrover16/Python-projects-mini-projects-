try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the sev]cond number: "))
    print("Which operation you want to perform ? Press + for addition\n , - for subtraction\n , * for multiplication\n and / for division.\n")
    o=input("Enter the operation you want to perform")
    match o:
        case "+":
            print(f"The result is {a+b}")
        case "-":
            print(f"The result is {a-b}")
        case "*":
            print(f"The result is {a*b}")
        case "/":
            print(f"The result is {a/b}")
        case _:
            print("Invalid operation")
except Exception as e:
    print(e)

