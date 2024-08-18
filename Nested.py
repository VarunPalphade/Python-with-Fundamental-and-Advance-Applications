
def Calculations(No1 ,No2):
    def Addition(X,Y):
        return X + Y
    def Substraction(X,Y):
        return X - Y
    ANS1 = Addition(No1,No2)
    ANS2 = Substraction(No1,No2)
    return ANS1, ANS2

print("Enter first number :")
A = int(input())

print("Enter secont number :")
B = int(input())

Result1,Result2 = Calculations(A,B)

print("Addition is : ",Result1)
print("Substraction is : ",Result2)