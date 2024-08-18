def main():
    Ans = 0

    try:
        print("enter the first number :")
        No1 = int(input())

        print("enter the second number :")
        No2 = int(input())

        Ans = No1 / No2
    
    except ZeroDivisionError as zobj:

        print("Exception occured ", zobj)
    
    except ValueError as vobj:
        print("Exception occured ", vobj)
    
    except Exception as eobj:
        print("Exception occured :", eobj)

    finally:
        print("Inside Finally block :")     
           
    print("Multimucation is :" ,Ans)


if __name__ == "__main__":
    main()