import sys
def Fun():
    print("Insode fun")
    Fun()     #recursive call

def main():
    Fun()

if __name__ == "__main__":
    main()