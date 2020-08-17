import random

def convert_into_choice(word):
    """This function will convert the character you've entered in a choice ex==>  s: snake """
    word=word.lower()
    if word=="s":
        return "snake"
    elif word=="w":
        return "water"
    elif word=="g":
        return "gun"
    else:
        print("INVALID INPUT!!!! PLEASE TRY AGAIN :-(")



#=======================> MAIN PROGRAM START'S HERE
rounds=10                                          #10 rounds will be played
h_win=0                                            #no.of rounds human won
c_win=0                                            #no.of rounds computer won
draw=0                                             #no. of rounds nobody won

print("***********************SNAKE WATER GUN GAME*******************************")
print("LET's PLAY NOW")


while(rounds>0):
 computer=["snake","water","gun"]
 c_choice=random.choice(computer)
 # print(c_choice)

 print("\nChoose Your Call ==> ")

 print("s/S: snake")
 print("w/W: water")
 print("g/G: gun\n")

 human=input("Please Enter Your Choice: ")

 h_choice=convert_into_choice(human)   #get the choice from the convert_into_choice()


 if (c_choice=="snake" and h_choice=="snake"):                    #snake
    # print("..........DRAW CHANCE.........\n")
    draw+=1
    rounds-=1
 elif (c_choice=="snake" and h_choice=="water"):                  #snake
    # print("COMPUTER WON !!!!\n")
    c_win+=1
    rounds -= 1
 elif (c_choice=="snake" and h_choice=="gun"):                    #snake
    # print("HUMAN WON !!!!\n")
    h_win+=1
    rounds -= 1
 elif (c_choice=="water" and h_choice=="snake"):                  #water
    # print("HUMAN WON !!!!\n")
    h_win+=1
    rounds -= 1
 elif (c_choice=="water" and h_choice=="water"):                  #water
    # print("..........DRAW CHANCE.........\n")
    draw+=1
    rounds -= 1
 elif(c_choice=="water" and h_choice==" gun"):                    #water
    # print("COMPUTER WON !!!!\n")
    c_win+=1
    rounds -= 1
 elif(c_choice=="gun" and h_choice=="snake"):                     #gun
    # print("COMPUTER WON !!!!\n")
    c_win+=1
    rounds -= 1
 elif(c_choice=="gun" and h_choice=="water"):                     #gun
    # print("HUMAN WON !!!!\n")
    h_win+=1
    rounds -= 1
 elif(c_choice=="gun" and h_choice=="gun"):                       #gun
    # print("..........DRAW CHANCE..........\n")
    draw+=1
    rounds -= 1

print("*********************************************************************************************")
print("RESULT OF THE GAME: \n")
print("No. of rounds: 10")
print("No. of wins HUMAN: ",h_win)
print("No. of wins COMPUTER: ",c_win)
print("No. of draws: ",{draw})

if c_win>h_win:
    print("Oops !!!! Computer won.")
elif h_win>c_win:
    print("Congratulations !!!! You Won.")
elif draw>c_win and draw>h_win :
    print("Nobody !!!! WON")