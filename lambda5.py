# Name = lambda Parameters : Logic 
# Name(___,___)....)


def EvenOdd(A):
    if (A % 2 == 0):
        return True
    else:
        return False



def main():
    Ret = EvenOdd(10)
    if (Ret == True):
        print("Even")
    else:
        print("flase")

if __name__ == "__main__":
    main()