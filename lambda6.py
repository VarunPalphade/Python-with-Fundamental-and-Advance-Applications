# Name = lambda Parameters : Logic 
# Name(___,___)....)


def EvenOdd(A):
    return (A%2 == 0)


EvenOddX = lambda A: (A%2==0)

def main():
    Ret = EvenOddX(10)
    if (Ret == True):
        print("Even")
    else:
        print("flase")

if __name__ == "__main__":
    main()