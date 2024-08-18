def Addition(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no
    return Sum

def main():
    size = int(input("provide numberrs you want to display :"))
    
    Arr = list()

    print("Enter the elemets :")

    for i in range(size):
        no = int(input())
        Arr.append(no)
    
    print("entered inputs are :" ,Arr)

    Result = Addition(Arr)
    print("Summation of all values are :", Result)

if __name__ == "__main__":
    main()