def CheckEven(NO):
    if(NO % 2 == 0):
        print(NO," is even number :")
    else:
        print(NO," is odd number :")

def main():
    print("Enter Number :")
    A = int(input())

    CheckEven(A)

# Starter 
if __name__ == "__main__":
    main()