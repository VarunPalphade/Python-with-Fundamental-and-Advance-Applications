# Name = lambda Parameters : Logic 
# Name(___,___)....)


def cube(A):
    Ans = 0
    Ans = A**3
    return Ans

Cube = lambda A: A**3

def main():
    Ret = Cube(10)
    print("cube is :",Ret)

if __name__ == "__main__":
    main()