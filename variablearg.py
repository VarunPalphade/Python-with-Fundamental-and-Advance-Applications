#Type of function arguments 
# 2 : Keyword arguments
# 3 : Default arguments 
# 4 : Variable number of arguments 


#4
def Addition(*No):
    print(type(No))
    print(len(No))
    Ans = 0
    
    for i in No:
        Ans = Ans + i 
    return Ans

Result = Addition(10,20,30)
print(Result)
