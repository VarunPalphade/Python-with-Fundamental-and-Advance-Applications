from functools import reduce


# demonstration with lambda fucntions 
CheckEvenX = lambda No : (No % 2 == 0)

IncreaseX = lambda No : (No + 1)

AddX = lambda A, B : (A + B)


def main():

    Data = []

    print("eneter the number of elements :")
    Size = int(input)

    print("Enter the elements :")
    iCnt = 0 
    for iCnt in Size:
        Data.append


                     #kay karaychay  kashavar karaychay
    FData = list(filter(CheckEvenX,     Data))
    print("Data after Filter Activity", FData)

                     #kay karaychay  kashavar karaychay
    MData = list(map(IncreaseX ,       FData))
    print("Data after Map Activity is : ",MData)

              #kay      kashavar
    RData = reduce(AddX, MData)
    print("Data after reduce Activity is :", RData)

if __name__ == "__main__":
    main()