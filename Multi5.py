import multiprocessing
import multiprocessing.process

def DisplayEven(No):
    print("List of even numbers are :")
    x = 2 
    for i in range(No):
        print(x)
        x = x+2

def DisplayOdd(No):
    print("List of odd number are :")
    x = 1 
    for i in range(No):
        print(x)
        x = x + 2


def main():
    print("Enter Number : ")
    Value = int(input())

    p1 = multiprocessing.Process(target= DisplayEven, args=(Value, ))
    p2 = multiprocessing.Process(target= DisplayOdd, args=(Value, ))

    p1.start()
    p1.join()
                         #not a good programming practice
    p2.start()
    p2.join()

    print("End of main process")
    

if __name__ == "__main__":
    main()