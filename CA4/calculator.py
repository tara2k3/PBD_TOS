import math

def factorial(n):  # def is a function
    if n > 1:
        return n * factorial(n - 1)
    if n < 0:
        return "inf"
    return 1


def fibonacci(n):
    n_2 = 0
    yield n_2
    n_1 = 1
    yield n_1
    for i in range(1, n):
        n = n_1 + n_2
        yield n_1 + n_2
        n_2 = n_1
        n_1 = n


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return (first * second)


def divide(first, second):
    return (float(first) / second)


def exponent(first, second):
    return (first ** second)


def sqrt(first):
    return (float(first ** 0.5))


def squared(first):
    return (first ** 2)


def cubed(first):
    return (first ** 3)


def sine(first):
    return math.sin(math.radians(first))


def cos(first):
    return math.cos(math.radians(first))


def tan(first):
    return math.tan(math.radians(first))


def read_values():
    numbers_strings = raw_input("\n	Enter a list of numbers separated by spaces: ").split(" ")
    numbers = []
    for number_string in numbers_strings:
        try:
            numbers.append(float(number_string))
        except:
            # just ignore errors
            pass

    return numbers


def main():
    print " \n	Welcome to my python calculator on steroids!!\n"

    print("	Select an option:\n")
    print("	1.Sum")
    print("	2.Filter odd numbers")
    print("	3.Filter even numbers")
    print("	4.Multiplication")
    print("	5.Square")
    print("	6.Square root")
    print("	7.Power of: ")
    print("	8.Fibonacci")

    choice = raw_input("\n	Enter choice (1/2/3/4/5/6/7/8) : ")

    if choice == '1':
        numbers = read_values()
        result = reduce(add, numbers)
        print("		The sum of {0} is {1}\n".format(numbers, result))
    elif choice == '2':
        numbers = read_values()
        # Using a lambda function
        result = filter(lambda x: x % 2 != 0, numbers)
        print("		The the odd numbers in the list are: {0}\n".format(result))
    elif choice == '3':
        numbers = read_values()
        # Using a lambda function
        result = filter(lambda x: x % 2 == 0, numbers)
        print("		The the even numbers in the list are: {0}\n".format(result))
    elif choice == '4':
        numbers = read_values()
        result = reduce(multiply, numbers)
        print("		The multiplication of {0} is {1}\n".format(numbers, result))
    elif choice == '5':
        numbers = read_values()
        result = map(squared, numbers)
        print("		The squares of {0} are {1}\n".format(numbers, result))
    elif choice == '6':
        numbers = read_values()
        result = map(sqrt, numbers)
        print("		The square roots of {0} are {1}\n".format(numbers, result))
    elif choice == '7':
        number = float(input("\n	Enter base number:	"))
        power = int(input("\n	Enter max power:	"))

        #  List Comprehensions
        result = [number ** x for x in range(1, power)]
        print("		The power of {0} is {1}\n".format(number, result))
    elif choice == '8':
        number = int(input("\n	Enter a number:	"))
        #  List Comprehensions + Generator
        result = [x for x in fibonacci(number)]
        print("		The fibonacci sequence for {0} is {1}\n".format(number, result))
    else:
        print("Adahh!!, You entered an invalid option")

if __name__ == "__main__":
    main()