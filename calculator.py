import art
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2
def multi(n1,n2):
    return n1*n2
operators={"+":add ,"-":sub,"/":divide,"*":multi,}
def calculator():
    print(art.logo)
    values=True
    number_1 = float(input("Enter the first number:"))
    while values:
        for signs in operators:
            print(signs)
        operation=input("Pick an operation:")
        number_2=float(input("Enter the second number:"))
        output=operators[operation](number_1,number_2)
        print(f"{number_1} {operation} {number_2}={output}")
        more_calc=input(f"Type 'yes' to continue calculating with {output}, or type 'no' to start with new calculation:").lower()
        if more_calc=='yes':
            number_1=output
        elif more_calc=='no':
            values = False
            print("\n"*100)
            calculator()
        else:
            print("The calculator stops here!!")
print()
calculator()
