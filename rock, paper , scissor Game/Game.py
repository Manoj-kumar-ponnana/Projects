import random
sr=['rock','paper','scissor']
pr={'r' :'rock','p' :'paper','s' :'scissor'}
def game(c):
    gc=random.choice(sr)
    print(f"Tony : {gc}\t{u} : {pr[c]}")
    if gc==pr[c]:
        print(f" Tony : you won this time {u} \U0001F643 let's see who will win next time")
        return True
    else:
        print(f"Tony : I won this time {u} \U0001f600 .close!! try better next time")
        return False

x=True
print("*"*15,"Welcome to the Game","*"*15)
print("\nNOTE : We are going to use 'r' for Rock, 'p' for Paper, 's' for Scissor for your convience")
u=input("Enter Your Good Name please \U0001F60A : ")
print("\nHello, I'm Tony your game opponent \U0001F60A ")
while x:
    print("\n\nEnter '1' to start the game or Enter '0' to stop the game")
    x=int(input("Enter to your choice run the game {} : ".format(u)))
    if x==0:
        break
    else:
        sc=[0,0]
        while True:
            print("\nuse 'r' for Rock, 'p' for Paper, 's' for Scissor for your convience and '0' to stop the game")
            y=input("\nyour Turn : ")
            if y=='0':
                break
            if game(y):
                sc[1]+=1
            else:
                sc[0]+=1
    print(f"\n\n\nTotal Score : Tony -{sc[0]}\t{u} -{sc[1]}\n")
    if (sc[0]+sc[1])>10 and sc[0]>sc[1] and (sc[0]-sc[1])>sc[1]:
        print("\nTony : Looser you lost ! too poor \U0001F60F")
    elif (sc[0]+sc[1])>10 and sc[0]>sc[1] and (sc[0]-sc[1])<3:
        print("\nTony : Close but I won \U0001F60A Better luck next time!!")
    elif sc[0]>sc[1] :
        print("\nTony : I won Man try to defeat me next time \U0001F92A")
    else:
        print(f"\nTony : Great {u},You Won with {sc[1]-sc[0]} points. I will beat you next time \U0001f600")
    print("\nAnyway It's delight playing with you.Hope to play another game with you \U0001f600")
print("*"*15,"Thankyou for using the game ",u,"*"*15)
