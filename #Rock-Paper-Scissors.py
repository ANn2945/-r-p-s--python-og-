#Its stupid,its a beginner thing b'cos I'm a beginner.....ik,maybe its stupid to put it as a repository :D

#Rock-Paper-Scissors
import random


user_points=0
computer_points=0
print("_________________________________\nLet's Start" )
chance=0




while chance<5:
    dictionary={
    "r":0,
    "p":1,
    "s":2
}
   


    user_input=input("(r/p/s) > ")
    computer=random.randint(0,2)




    user=dictionary.get(user_input)




    if user==0:
        if computer==0:
            print("Draw")
        if computer==1:
            print("computer won")
            computer_points+=1
        if computer==2:
            print("user won")
            user_points=+1
        chance+=1
        print(f"computer= {computer_points} and user= {user_points}")




    elif user==1:
        if computer==1:
            print("Draw")
        if computer==2:
            print("computer won")
            computer_points+=1
        if computer==0:
            print("user won")
            user_points+=1
        chance+=1
        print(f"computer= {computer_points} and user= {user_points}")




    elif user==2:
        if computer==2:
            print("Draw")
        if computer==0:
            print("computer won")
            computer_points+=1
        if computer==1:
            print("user won")
            user_points+=1
        chance+=1
        print(f"computer= {computer_points} and user= {user_points}")                                          
       
    else:
        print("Invalid input")
        print("_____________________")
        continue
       
       
   
   
   
    print("_____________________")




if computer_points>user_points:
    print("\nCOMPUTER WON THE ROUND!!! 🎉🎉\n")
elif computer_points<user_points:
    print("\nUSER WON THE ROUND!!! 🎉🎉\n")
else:
    print("\nTHIS ROUND IS DRAW\n")

