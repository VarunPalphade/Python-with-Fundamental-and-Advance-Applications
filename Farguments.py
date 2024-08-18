#Type of function arguments 
# 1 : Positional arguments 
# 2 : Keyword arguments
# 3 : Default arguments 
# 4 : Variable number of arguments 


def Information(Name ,age ,salary):
    print("Name is : ", Name)
    print("age is :" , age)
    print("salary is", salary)

# 1 jase parameters sequence ahet tyat ch order madhe call karaycha 
Information("amit",32,90000)
Information("shreya",25,50000)


#2 parameter pathavant asatna kashat pathvaycha he mention karaycha 
Information(age = 31 , salary= 10000, Name="varun")



print("-------------------------------------")
#3 function chya parameter madhech already value dileli asti
def Area (Radius , PI = 3.14):
    Result = PI * Radius * Radius
    return Result

Ans = Area(10.7)
print("Area of circle is :" , Ans)



print("-------------------------------------")
# 3.1 
Ans1 = Area(10.7 , 7.20 )
print("Area of circle is :" , Ans1)


