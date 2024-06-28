# Arithmetic calculator

print("Welcome!")
print("Simple Calculator")

while (True):
    operator = input("Enter the Operator from (+,-,*,/) :")

    if operator in ['+','-','*','/']:
        try:
            num1=float(input("Enter the first number :"))
            num2=float(input("Enter the first number :"))
        except ValueError:
            print("Not a number!. Enter a valid number")
            continue

        if(operator == "+"):
            print("calculation is -:")
            print(num1, "+" , num2 ,"=" ,num1+num2)
        elif(operator == "-"):
            print("calculation is -:")
            print(num1, "-" , num2 ,"=" ,num1-num2)
        elif(operator == "*"):
            print("calculation is -:")
            print(num1, "*" , num2 ,"=" ,num1*num2)
        elif(operator == "/"):
            if(num2!=0):
                print("calculation is -:")
                print(num1, "/" , num2 ,"=" ,num1/num2)
            else:
                print("Denoinator is zero !. Invalid operation")
        
        choice = input("Did you wanna to do next calculation? yes/no :")
        if(choice.lower() != "yes"):
            print("Thank you !")
            break
    else:
        print("Not a valid operator. enter a valid operator from given set of choice.")