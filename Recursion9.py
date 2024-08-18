# Factorial of  5 is : 5 * 4 * 3 * 2 * 1 ie 120

fact = 1
def factorial(num):
    global fact

    if(num >= 1):
        fact = fact * num
        num = num - 1
        factorial(num)  #recursive call
        return fact
        
        
def main():
    value = int(input("Give me a value "))
    ret = factorial(value)

    print(ret)

if __name__ == "__main__":
    main()