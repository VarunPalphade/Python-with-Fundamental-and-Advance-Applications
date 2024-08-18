import multiprocessing
import os

def DisplayEven(No):
    print("PID of even process ", os.getpid())
    print("List of even numbers are :")
    x = 2 
    for i in range(No):
        print(x)
        x = x+2

def DisplayOdd(No):
    print("PID of odd process", os.getpid())
    print("List of odd number are :")
    x = 1 
    for i in range(No):
        print(x)
        x = x + 2


def main():
    print("PID of main ", os.getpid())
    print("Enter Number : ")
    Value = int(input())

    p1 = multiprocessing.Process(target= DisplayEven, args=(Value, ))
    p2 = multiprocessing.Process(target= DisplayOdd, args=(Value, ))

    p1.start()
    p2.start()
    
                   #not a good programming practice
    p1.join()
    p2.join()

    print("End of main process")
    print("PID of main ", os.getpid())
    

if __name__ == "__main__":
    main()