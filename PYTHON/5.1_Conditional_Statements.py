#Conditional Statements
"""
1. Check the condition true / false and execute the following output when the condition is only true
2. If nothing is true return nothing
3. If the 1st condition is true and it doesnt go for 2nd one
4. We can use Logical and Comparison Operators inside the ()
"""
from PIL import Image
import emoji
import turtle

# 1. if
if(a:=10)==10:
    print(a)
print("**********************************************************************************************************")

# 2. if - else
name=input("ONLY FOR GIRLS \nEnter your name = ")
love=input("DO YOU LOVE ME \nPress (y/n) = ")
if(love=='y' or love=='Y'):
    print("I Love you Tooo ",name,"\U0001F60D")
else:
    print("Nee illana varra ponnu podi \U0001F60E")
print("**********************************************************************************************************")

# 3. if - elif - else
i1 = "C:/Users/harim/Desktop/Python/Img/img_0.jpg"
i2 = "C:/Users/harim/Desktop/Python/Img/img_2.jpg"
img1 = Image.open(i1)
img2 = Image.open(i2)
n1='hari';p1='123'
n2='mathu';p2='123'
un=input("Enter Username = ");pa=input("Enter Password = ")
if(n1 == un and pa==p1):
    img1.show()
elif(n2==un and pa==p1 ):
    img2.show()
elif(n1 == un and pa!=p1):
    print("Password doesnt match")
else:
    print("Login failed")

