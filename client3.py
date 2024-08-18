import Marvellous as M

def main():
    print("Enter first number :")
    A = int(input())
    
    print("Enter second number :")
    B = int(input())

    Ans = M.Addition(A,B)
    print("Addition is :",Ans)
                                                #All import
    Ans = M.Multiplication(A,B)
    print("Multiplication is :",Ans)

main()