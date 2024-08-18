from functools import reduce

def CheckEven(No):
    return (No % 2 == 0)

def Increase(No):
    return No + 1

def Add(A, B):
    return A + B

def main():
    Data = [11,14,20,23,18,16,15,20]
    print("Data from input list : ", Data)
                     #kay karaychay  kashavar karaychay
    FData = list(filter(CheckEven,     Data))
    print("Data after Filter Activity", FData)

                     #kay karaychay  kashavar karaychay
    MData = list(map(Increase ,       FData))
    print("Data after Map Activity is : ",MData)

              #kay      kashavar
    RData = reduce(Add, MData)
    print("Data after reduce Activity is :", RData)

if __name__ == "__main__":
    main()