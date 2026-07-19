#functions to do the following addition, subtraction, multiplication , divide

def addition(a, b ):
    return print(a+b)

def subtraction(a,b):
    return print(a - b)

def divide(a,b):
    return print(a/b)

def multiplication(a,b):
    return print(a*b)


def main():
    print('Welcome to our home calculator')
    # a = input("Enter a number: ")
    # b = input("Enter a number: ")
    # c = input("Enter a sign (+, / , *, -) ")

    x = True
    while x == True:
        a = input("Enter a number: ")
        b = input("Enter a number: ")
        c = input("Enter a sign (+, / , *, -) ")
        try:
            a = int(a)
            b = int(b)
            
            x = False
            #check for which sign was inputted
            if c == '-':
                subtraction(a,b)
            elif c == '*':
                multiplication(a,b)
            elif c == '+':
                addition(a,b)
            elif c == '/':
                subtraction(a,b)
            # else:
            #     print("Wrong math")
        except:
            print("Wrong input, Please try again.")
    
    



main()