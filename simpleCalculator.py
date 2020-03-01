import math


class calculator:

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def subtraction(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        return num1 / num2

    @staticmethod
    def square(num1):
        return num1 * num1

    @staticmethod
    def squareRoot(num1):
        return math.sqrt(num1)


if __name__ == '__main__':

    choice = ""

    while choice != "7":
        print("Select the operation:")
        print("1. Add")
        print("2. Subtraction")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square")
        print("6. Square Root")
        print("7. Quit")

        choice = input("Enter Choice: ")

        if choice == "1":
            firstNum = float(input("Enter first number"))
            secondNum = float(input("Enter Second Number"))
            print(calculator.add(firstNum, secondNum))

        elif choice == "2":
            firstNum = float(input("Enter first number"))
            secondNum = float(input("Enter Second Number"))
            print(calculator.subtraction(firstNum, secondNum))

        elif choice == "3":
            firstNum = float(input("Enter first number"))
            secondNum = float(input("Enter Second Number"))
            print(calculator.multiply(firstNum, secondNum))

        elif choice == "4":
            firstNum = float(input("Enter first number"))
            secondNum = float(input("Enter Second Number"))
            print(calculator.divide(firstNum, secondNum))
        elif choice == "5":
            firstNum = float(input("Enter first number"))
            print(calculator.square(firstNum))
        elif choice == "6":
            firstNum = float(input("Enter first number"))
            print(calculator.squareRoot(firstNum))
        elif choice == "7":
            break

        else:
            print("Invalid Choice")

