def fahrenheit_to_celsuis(c):
    result = c * (9/5) + 32
    print(result)
    return result
    

def celsuis_to_fahrenheit(f):
    result = (f -32) * (5/9)
    print(result)
    return result

def celsuis_to_kelvin(c):
    result = c + 273.15
    print(result)
    return result
    


def main():
    print("Enter which temperature you will like to convert from and to")
    current_temp = input("Enter temp:")
    print("what is the current temperature in")
    print("Enter 1 for fahreheit to celsuis")
    print("Enter 2 for Celsuis to fahreheit")
    print("Enter 3 for celsuis to kelvin" )
    current_scale = input()

    if current_scale == '1':
        fahrenheit_to_celsuis(int(current_temp))
    elif current_scale == '2':
        celsuis_to_fahrenheit(int(current_temp))
    elif current_scale == '3':
        celsuis_to_kelvin(int(current_temp))
    else:
        print( "Error we don't have we missed something")


main()

