from abc import ABC
import itertools as it
from time import sleep


class Car(ABC): #Base class 
    def milage(self): #Abstract Method
        pass

class Tata(Car): #Derived class #Abstract Class
    def milage(self):
        print("This is abstract method example")

    @classmethod
    def ClassMethod(cls):
        print("This is class method")

    @staticmethod
    def ClassStaticMethod():
        print("This is class static method")

def It_repeat(): #infinite iterator
    x=it.repeat('AB',10)
    for i in x:
        print(i)
        sleep(1)

def It_Accumulate(): #Iterator termination on shortest input sequence
    y=it.accumulate([1,2,3,4,5])
    for ij in y:
        print(ij,end=" ")


def AddNumber():#Exception Handling
    try:
        n1 = int(input("Enter number 1: "))
        n2 = int(input("Enter Number 2: "))
        print("Sum is :", n1 + n2)
    except ValueError as e:
        print("Error in values :", e )
        print("Want to try again")
        ans = input("Y/N :")
        if(ans.lower() == "yes" or ans.lower() =='y'):
            AddNumber()
    else:
        pass
        
      
def Argument(*args): #Any number of arguments
    for i in args:
        print(i)

def Kwargs(**kwr): # Any number of arguments with key and value
    for i, j in kwr.items():
        print(f"{i} : {j}")


double = lambda x : x*2 #Lambda function for double the value
power = lambda x,y : pow(x,y) #Lambda funtin for power of a number
UpperCase = lambda x : x.upper() # Lambda for Upper case of string

print(double(2))
print(power(5,2))
print(UpperCase("piyush"))
#It_repeat()
#It_Accumulate()

#t1=Tata()
#t1.milage()
#t1.ClassMethod()
#t1.ClassStaticMethod()

#AddNumber()

#Argument(1,2,3,4)

#Kwargs(aa=10,bb=20,cc=30)





