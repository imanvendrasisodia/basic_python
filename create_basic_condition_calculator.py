operation = input("enter your operation: ")

first_digit = int(input("enter your first digit: "))

second_digit = int(input("enter second digit: "))

if(operation == "+"):
    print("additon of two digit:" ,first_digit + second_digit)

elif(operation == "-"):
    print("the substraction of two digit is: ", first_digit - second_digit)    

elif(operation == "*"):
    print("multiplication of two digit is: ", first_digit * second_digit)

elif(operation == "/"):
    print("division of two number is: ", first_digit/second_digit)

elif(operation == "%"):
    print("the modules of : ", first_digit%second_digit)
    
else:
    print("invalid operator: ")

