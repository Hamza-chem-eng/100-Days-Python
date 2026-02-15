def add(n1, n2):
    return n1 + n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1,n2):
    if n2 == 0:
        return "infinity"
    return n1 / n2
    return n1/n2
def subtract(n1,n2):
    return n1 - n2
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
import art
print(art.logo)
v = True
while v is True:

    first_number = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input('Enter operation: ')

    second_number = float(input("Enter the second number: "))
    result = operations[operation_symbol](first_number, second_number)
    print(f"{first_number} {operation_symbol} {second_number} = {result}")
    cont = input(f"Do you want to continue  working with {result} as a first number.(y/n): ")
    if cont == "y":
        co = True
        while co is True:
            first_number = result
            for symbol in operations:
                print(symbol)
            operation_symbol = input('Enter operation: ')

            second_number = float(input("Enter the second number: "))
            result = operations[operation_symbol](first_number, second_number)
            print(f"{first_number} {operation_symbol} {second_number} = {result}")
            cont = input(f"Do you want to continue working with {result} as a first number.(y/n): ")
            if cont == "n":
                co = False
    if cont == "n":
        print("\n" * 100)
        print(art.logo)
