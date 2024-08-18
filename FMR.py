#demostrante FMR using normal fuctions 

print("------ Marvellous infosysytems ----")

print("Demonstration of filter map reduce")

def EvenChk(no):
    return (no % 2 == 0)

def Increse(no):
    return no+2

def Add(a,b):
    return a + b

arr = [8,9,5,16,2,4,21,30,11]

evenArr = list(filter(EvenChk,arr))

print("Data after filter", evenArr)

ModArray = list(map(Increse,evenArr))

print("data after map " , ModArray)

sum = reduce(Add,ModArray)

print("addition of even numbers" ,sum)

#demostrante FMR using lambda fuctions 


evenArr = list(filter(lambda no : (no % 2 == 0),arr))

print("data filter using lambda ", evenArr)

ModArray = list(map(lambda no : no+2, evenArr))

print("data after map using lambda", ModArray)

sum = reduce(lambda a,b : a+b, ModArray)

print("addition of even using lambda ", sum)