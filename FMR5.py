from functools import reduce

# demonstration with lambda fucntions 
CheckEvenX = lambda No : (No % 2 == 0)
IncreaseX = lambda No : (No + 1)
AddX = lambda A, B : (A + B)

def filterX(Task , Elements):
    Result = []

    for no in  Elements:

        Ret = Task(no)
        if(Ret == True):
            Result.append(no)

    return Result


def main():
    Data = [11,14,20,23,18,16,15,20]
    print("Data from input list : ", Data)
                     #kay karaychay  kashavar karaychay
    FData = list(filterX(CheckEvenX,     Data))
    print("Data after Filter Activity", FData)

                     #kay karaychay  kashavar karaychay
    MData = list(map(IncreaseX ,       FData))
    print("Data after Map Activity is : ",MData)

              #kay      kashavar
    RData = reduce(AddX, MData)
    print("Data after reduce Activity is :", RData)

if __name__ == "__main__":
    main()