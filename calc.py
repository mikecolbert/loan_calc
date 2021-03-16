#calc.py


def addTwoNumbers(numberOne, numberTwo):
    return (numberOne + numberTwo)
    

def main():
    numberOne = int(input("What is your first number?"))
    numberTwo = int(input("What is your second number?"))
    mySum = addTwoNumbers(numberOne, numberTwo)
    
    print(mySum)

    
main()