def DisplayEven(No):
    print("List of even numbers are :")
    x = 2 
    for i in range(No):
        print(x)
        x = x+2

def DisplayOdd(No):
    print("List of odd number are :")
    x = 1 
    for i in range(No):
        print(x)
        x = x + 2


def main():
    print("Enter Number : ")
    Value = int(input())

    DisplayEven(Value)
    DisplayOdd(Value)

if __name__ == "__main__":
    main()