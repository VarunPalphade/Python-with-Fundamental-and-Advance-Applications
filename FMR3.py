from functools import reduce


# demonstration with lambda fucntions 


def main():
    Data = [11,14,20,23,18,16,15,20]
    print("Data from input list : ", Data)
                     #kay karaychay                  kashavar karaychay
    FData = list(filter(lambda No : (No % 2 == 0),     Data))
    print("Data after Filter Activity", FData)

                             #kay karaychay  kashavar karaychay
    MData = list(map((lambda No : (No + 1)) ,       FData))
    print("Data after Map Activity is : ",MData)

                          #kay              kashavar
    RData = reduce((lambda A, B : (A + B)), MData)
    print("Data after reduce Activity is :", RData)

if __name__ == "__main__":
    main()