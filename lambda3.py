# Name = lambda Parameters : Logic 
# Name(___,___)....)


def cube(A):
    Ans = 0
    Ans = A*A*A
    return Ans

Cube = lambda A: A *A * A

def main():
    Ret = Cube(11)
    print("cube is :",Ret)

if __name__ == "__main__":
    main()