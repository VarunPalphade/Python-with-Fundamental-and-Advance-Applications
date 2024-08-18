import sys
i = 1
def Fun():
    global i 
    print("Insode fun",i)
    i = i + 1
    Fun()     #recursive call

def main():
    Fun()

if __name__ == "__main__":
    main()