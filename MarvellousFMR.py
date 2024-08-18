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


def mapX(Task , Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    
    return Result


def reduceX(Task , Elements):
    Sum = 0
    
    for no in Elements:
        sum = Task(Sum, no)

    return Sum
