from MarvellousFMR import *

def main():
    Data = []

    print("eneter how many element ")
    size = int(input())

    print("enter elemnts ")
    iCnt = 0
    for iCnt in range(0,size):
        No = int(input())
        Data.append(No)


    print("Data from input list : ", Data)

    FData = list(filterX(CheckEvenX, Data))
    print("Data after Filter Activity", FData)

    MData = list(mapX(IncreaseX ,  FData))
    print("Data after Map Activity is : ",MData)

    RData = reduceX(AddX, MData)
    print("Data after reduce Activity is :", RData)

if __name__ == "__main__":
    main()