print("Demostration of object orientation ")

##################################################################################
class Arithematic:
    def __init__(self, Value1 , Value2):   #Constructor 
        self.No1 = Value1                   #Characteristics  (i e data)
        self.No2 = Value2                   #Characteristics 

    def Addition(self):                     #behaviour         (i e fuction )
        Ans = self.No1 + self.No2
        return Ans 
    
    def Substraction(self):                     #behaviour
        Ans = self.No1 - self.No2
        return Ans  
###################################################################################

print("Enter 1st number :")
A = int(input())

print("Enter 1st number :")
B = int(input())

obj = Arithematic(A,B)

Ret = obj.Addition()
print("Addition is :", Ret)

Ret = obj.Substraction()
print("Substraction is :",Ret)