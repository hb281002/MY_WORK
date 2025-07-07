#VARIABLES
#************
#Rules to create a var
#1.var do not start with number
#2.var is a case sensitive
#3.var should be A-z,a-z,0-9 and _ . It does not start with symboles like @#!% and numbers 1245

#VAR EXAMPLE :
#Types of var:

#1.Local variable
def Localvariable():
    a1 = "Local variable"
    print(a1)
#print(a1)
Localvariable()
print()
#2.Global variable
a2 = "Global variable"

def Globalvariable():
    print(a2)

Globalvariable()
print()
#3. Nonlocal Variable
def out():
    a3 = "Nonlocal Variable"
    def inner():
        print(a3)
    inner()

out()
print()

#4.Instance Variable
class Student:
    def __init__(self, name, grade):
        self.name = name         # instance variable
        self.grade = grade       # instance variable

s1 = Student("Alice", 90)
s2 = Student("Bob", 85)

print(s1.name)  # Alice
print(s2.name)  # Bob
print()
#5.Class Variable
class Student:
    school_name = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name         # instance variable

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school_name)  # ABC School
print(s2.school_name)  # ABC School

Student.school_name = "XYZ School"

print(s1.school_name)  # XYZ School (changed for all instances)
print()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#DATA TYPES
#*************
#Python is a dynamic language so that the data type can be defaultly assiend
#only the user declare variables are no need to mention
#when the input get from the user at the run time it take the datatype has string defaultly we have to mention the datatype for each data other then string data
#we also type cast the datatype

#DATATYPE EXAMPLE:
#types of datatype
print("1.NUMBER VAR")
#Int
a=10
print(type(a))

#Float
a=10.5
print(type(a))

#Commplex
a=2+3j
print(type(a))

print("\n2.NAME VAR")
#Str
a="hari"
print(type(a))

print("\n3.Boolean")
#Bool
a=10;b=10
print(a==b)
print(a<b)
print(type(a>b))

print("\n4.Sequence Types")
#List
a=[1,a,1]
print(type(a))
b=(1,3,4)
print(type(b))
c=range(4)
print(type(c))

print("\n5.Set Types")
#Set
a={1,5,'s'}
print(type(a))

#frozenset
a=frozenset[(1,2,3,4)]
print(type(a))

print("\n6.Mapping Type")
#Dict
a={"name":"hari"}
print(type(a))

print("\n7.Binary Types")
#Bytes
b = b'hello'
print(b[1])
print(list(b))
print(type(b))

#bytearray
a = bytearray([65, 66, 67])
print("\n",a[2])
print(list(a))

#memoryview
x = memoryview(b"hello")

print("\n",x)             # <memory at 0x...>
print(x[0])          # 104  (ASCII value of 'h')
print(x[:2])         # <memory at 0x...>
print(x[:2].tobytes())  # b'he'

print("\n8. None Type")
a=None
print(type(a))

print()
#-----------------------------------------------------------------------------------------------------------------------------------------

#Default Assing
a=1102
b="Mathu"
c=9.0
print("ID           :",a,"\nStudent Name :",b,"\nStudent CGP  :",c,"\n")

#Type cast:
a=10;print("Int value",a)
a=float(10);print("Int value change has float value",a,"\n")

#Runtime datatype
a=input("Enter any data even symboles : ")
print(a,"and",type(a))
a=int(input("Enter only Number : "))
print("The num you entered is ",a)