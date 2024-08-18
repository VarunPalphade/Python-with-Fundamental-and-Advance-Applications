import threading
import os

def DisplayEven(No):
    print("PID of even process ", os.getpid())
    print("TID of even thread ", threading.get_ident())
    print("List of even numbers are :")
    x = 2 
    for i in range(No):
        print(x)
        x = x+2

def DisplayOdd(No):
    print("PID of odd process", os.getpid())
    print("TID of odd thread ", threading.get_ident())
    print("List of odd number are :")
    x = 1 
    for i in range(No):
        print(x)
        x = x + 2


def main():
    print("PID of main ", os.getpid())
    print("TID of main thread", threading.get_ident())
    print("Enter Number : ")
    Value = int(input())

    p1 = threading.Thread(target= DisplayEven, args=(Value, ))
    p2 = threading.Thread(target= DisplayOdd, args=(Value, ))

    p1.start()
    p2.start()
    
                   #not a good programming practice
    p1.join()
    p2.join()

    print("End of main process")
    

if __name__ == "__main__":
    main()