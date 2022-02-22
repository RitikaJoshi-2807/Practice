import random
# Here Computer will choose one of the options and you will have to select one.
def gamewin(comp,you):
    if comp==you :
        return None
    elif comp=='s':
        if you=='w':
            return False
        if you=='g':
            return True
    elif comp =='w':
        if you =='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False

print("Comp turn: Snake(s) Water(w) or Gun(g) ?")
randno=random.randint(1,3)
if randno==1:
    comp = 's'
elif randno==2:
    comp='w'
elif randno==3:
    comp = 'g'
you=input("Your turn : Snake(s) Water (w) or Gun(g) :")
print(f"Computer chose : {comp}")
print(f"You chose :{you}")
a=gamewin(comp,you)
if a==None:
    print("The game is a tie")
elif a:
    print("You win")
else:
    print("You lose")

