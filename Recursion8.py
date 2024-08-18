import sys
def DisplayR(num):
    global i 

    if(num >= 1):
        print(num)
        num = num - 1
        DisplayR(num)  #recursive call
        
        
def main():
    value = int(input("Give me a value "))
    DisplayR(value)

if __name__ == "__main__":
    main()