#Looping Statements
#Looping Statements are used to repeat the statement in one or more then a one time.
"""
A range can be set and the block of code will be repeat until the condition get failed
For loop used to iterate / redpeatedly over a sequence like Lists,Tupple,String or Range and execute the code block
SYNTAX
for variable in sequence:
"""

#1. for loop
for i in range(1,5) :#range(start(index 0),end)
    print(i,end="")#end - Printing without a newline
print('\n')

#1.1 Nested loop
for i in range(0,2):
    print("i=",i)
    for j in range(0,2):
        print("j=",j)

#2. While loop

# Predefined username and password
name = "hari"
pas = "123"

tri = 3  # Number of attempts
name_v= False  # Flag to check if username is correct

while tri > 0:
    if not name_v:
        name_ = input("Enter username: ")
        if name_ == name:
            name_v = True
        else:
            print("Incorrect username. Please try again.")
            continue  # Skip asking for password

    pas_ = input("Enter password: ")

    if pas_ == pas:
        print("Login successful! 🎉")
        break
    else:
        tri -= 1
        if tri == 2:
            print(f"What a shame! Even you can't remember your password 😅\nAttempts left: {tri}")
        elif tri == 1:
            print(f"Incorrect password. Attempts left: {tri} 😟")
        elif tri == 0:
            print("WRONG PASSWORD 😱 Account locked.")

a=0
while a<5:
    print(a)
    a+=11