#VARIABLES
#************
#Rules to create a var
#1.var do not start with number
#2.var is a case sensitive
#3.var should be A-z,a-z,0-9 and _ . It does not start with symboles like @#!% and numbers 1245

#VAR EXAMPLE :
#Defalut datatype assing
a=22
b="hari"
print("my name is",b,"and i am",a,"years old")

#Multiple var for single data
a=b=c="Byeee"
print(a,b,c)

#More var in single line with more data
a,b,c=10,"apple",15000
print(a,"kg of",b,"price was",c,"rs")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#DATA TYPES
#*************
#Python is a dynamic language so that the data type can be defaultly assiend
#only the user declare variables are no need to mention
#when the input get from the user at the run time it take the datatype has string defaultly we have to mention the datatype for each data other then string data
#we also type cast the datatype

#DATATYPE EXAMPLE:
#Default Assing
a=1102
b="Mathu"
c=9.0
print("ID           :",a,"\nStudent Name :",b,"\nStudent CGP  :",c,"\n")

#Type cast:
a=10;print("Int value",a)
a=float(10);print("Int value change has float value",a)

#Runtime datatype
a=input("Enter any data even symboles : ");
print(a)
a=int(input("Enter only Number : "))
print("The num you entered is ",a)
