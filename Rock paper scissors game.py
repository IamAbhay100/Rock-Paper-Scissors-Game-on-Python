import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif you=='r':
        if comp=='p':
            return False
        elif comp=='s':
            return True  
    elif you=='p':
        if comp=='s':
            return False
        elif comp=='r':
            return True        
    elif you=='s':
        if comp=='r':
            return False
        elif comp=='p':
            return True        
                  
print("comp turn:Rock(r) Paper(p) Scissor(s)")
randno=random.randint(1,3)
if randno==1:
    comp='r'
elif randno==2:
    comp='p'
elif randno==3:
    comp='s'

you=input("your turn:Rock(r) Paper(p) Scissor(s)")
a = gamewin(comp,you)

print(f"comp choose: {comp}")
print(f"you choose: {you}")

if a == None:
    print("Game Tie!")
elif a:
    print("you Won!")
else:
    print("you Lose!")        
