#Normal input() :
a=input("Enter name = ")#Take all values has string

#input() mention with particular datatype :
#int(),folat(),ect
b=int(input("Enter number = "))#Mention input type only has number

#more then one input :
#split()
c,d,e=input("Enter Date Of Birth :\nDate/Month/Year = ").split("/")

#input() mention with any data type :
#eval()
#can execute arbitrary code, so use it cautiously.
ev = eval(input("Enter any value: "))

print("Hai",a,"welcome\nYour mobile number is",b,"\nAnd you born in ",c+"/"+d+"/"+e)
print("You entered value is =",ev,"and the type of value is =",type(ev))
