def beginning():
    print("This program adds two numbers. ")

def get_num(answer):
    while True:
        yea = input(answer)
        if yea.isdigit():
            return int(yea)
        print("Type something correctly")

def main():
    beginning()
    while True:
        num1 = get_num("Enter first number: ")
        num2 = get_num("Enter second number: ")
        print("Your sum is:", num1 + num2)
        total = input(" Do you wish to proceed? Say yes or no: ").lower().strip()
        if total == "no":
            break
    print("Thanks come again.")

if __name__ == "__main__":
    main()
