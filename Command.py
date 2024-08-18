import sys
def main():
    print("Demonstration of commend line arguments ")
    print("Name of application :", sys.argv[0])
    print("Datatype of Argv is ",type(sys.argv))
    print("Number of command line arguments are :",len(sys.argv))

if __name__ == "__main__":   #special variable(__name__) or (__anyname__)
    main()