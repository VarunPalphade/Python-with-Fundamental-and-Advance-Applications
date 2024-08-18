import sys
i = 1
def DisplayR(num):
    global i 

    if(i <= num):
        print(i)
        i = i + 1
        DisplayR(num)  #recursive call
        
        
def main():
    value = int(input("Give me a value "))
    DisplayR(value)

if __name__ == "__main__":
    main()