print("Demostration of procedural ")

def Addition(No1 , No2):
    Ans = No1 + No2
    return Ans

def Substraction(No1 , No2):
    Ans = No1 - No2
    return Ans

def main():
    print("Enter the 1st number :")
    A = int(input())

    print("Enter the 2st number :")
    B = int(input())

    Ret  = Addition(A,B)
    print("Addition is : ", Ret)

    Ret  = Substraction(A,B)
    print("substraction is : ", Ret)