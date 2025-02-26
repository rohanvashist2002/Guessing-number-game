# guess the number correctly
import random
n=random.randint(1,100)
a=-1 
guess=1
while (a!=n):
    a= int(input("Guess the number : "))
    if(a>n):
        print("Guess the lower number!!")
        guess+=1
    elif(a<n):
        print("Guess the higher number!!")
        guess+=1
    
print(f"Your have guessed the {n} corrected in {guess} attempt!! ")


