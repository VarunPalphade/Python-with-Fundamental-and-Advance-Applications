def Addition(No1 , No2):
    print("inside addition fuction ")
    Ans = 0 
    Ans = No1 + No2
    return Ans

def main():
    print("inside main fuction ")
    print("Enter first number :")
    A = int(input())

    print("Enter 2nd number :")
    B = int(input())

    Result = Addition(A,B)

    print("Addition is : " ,Result)

main()
print("end of application")