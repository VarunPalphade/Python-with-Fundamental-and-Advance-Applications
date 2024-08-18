def Display(Cnt):
    i = 0

    if(Cnt <= 0):
        print("invalid input")
        return
    
    while (i < Cnt):
        print("jay ganesh....", end = " ")
        i = i + 1

def main():

    No = int(input("please enter a number "))
    Display(No)
    

if __name__ == "__main__":       #starter 
    main()