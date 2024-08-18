def Display(Cnt):
    i = 0

    if(Cnt <= 0):
        print("invalid input")
        return
    
    for i in range(Cnt):
        print("jay ganesh....", end = " ")

def main():

    No = int(input("please enter a number "))
    Display(No)
    

if __name__ == "__main__":
    main()