daVe = "Dave: "
steVen = "Steven: "

#options y/n
def option():
    global checK
    yN = input("Yes or No: ")
    if yN == ("Yes"):
        checK = 1
    else:
        checK = 2

#option 1/2
def optionTwo():
    global checKtwo
    yNtwo = input("1 or 2: ")
    if yNtwo == ("1"):
        checKtwo = 1
    else:
        checKtwo = 2

#finaly
def breakDown():
    print(daVe + "Nice seeing you again")
    print(daVe + "This last games simple")
    print(daVe + "Fight Me(1) or Steven(2) ?")
    optionTwo()
    if checKtwo == 1:
        print(daVe + "Okay, my games pretty simple, just tell me 1 or 2, one ends the game the other lets you get the Dough")
        print(daVe + "Simple enough")
        optionTwo()
        if checKtwo == 1:
            print(daVe + "You win!")
            print(daVe + "Heres the Doug!")
            print(daVe + "(8-(=o=)-8)")
            print(daVe + "I hope it was worth it :)")
            print(daVe + "Play again and see if you can find the egg!")
            print(daVe + "if you can ill give you a gift!")
        else:
            print(daVe + "Awww you died :(")
            print(daVe + "Now you have to reset :(")
    else:
        print(steVen + "B A R K")
        option()
        if checK == 1:
            option()
            if checK == 1:
                option()
                if checK == 1:
                    print(steVen + "Y o u d i e d ")
                    breakDown()
                else:
                    print(daVe + "You won!")
                    print(daVe + "Heres the Doug!")
                    print(daVe + "(8-(=o=)-8)")
                    print(daVe + "I hope it was worth it :)")
                    print(daVe + "Play again and see if you can find the egg!")
                    print(daVe + "if you can ill give you a gift!")
            else:
                print(steVen + "Y o u d i e d")
                breakDown()
        else:
            print(steVen + "Y o u  d i e d")
            breakDown()

#mkeke
m = ("=======================")
mm = ("Congrats you found the egg!")
mmm = ("0  <--- heres the egg!")
def mekke():
    mkeek()
def mkeek():
    print(m)
    print(mm)
    print(mmm)
    print(m)
    print(m)
    print(daVe + "great job finding the egg! in one of the ending I told you id get you a gift if you got the egg so its time to keep my promise")
    print(daVe + "heres my favorite bianary code line ")
    print(daVe + "01110100 01101000 01100101 00100000 01110011 01101110 01100001 01101001 01101100 01110011 00100000 01100011 01101111 01101101 01101001 01101110 01100111 00100000 01100110 01101111 01110010 00100000 01110101 01110011 ")
    menu()
def mkeke():
    mekke()

   

#dying
def dead():
    print(daVe + "You die :(")
    print(daVe + "sending you back to the last save")

#steve
def steve():
    print(steVen + "bark")
    print(steVen + 'bark bark, bark... ba. bark')
    option()
   
   
#sneeze
def sneeze():
    global bark
    BARK = input("Bless you(1) or Steve, Daves malfunctioning again tell the dev(2): ")
    if BARK == ("1"):
        bark = 1
    else:
        bark = 2
#last floor
def lastF():
    print(daVe + "congrats on getting to the last floor")
    print(daVe + "this foors pretty basic")
    print(daVe + "In exchange for completing this level you get secret codes for prompts")
    print(daVe + "plus you get the Doug ofc")
    print(daVe + "All you have to do isssss")
    print(daVe + "Achoo...")
    sneeze()
    if bark == 1:
        print("You: " + ": Bless you Dave")
        print(daVe + "Thank you, sorry about that dont worry about it")
        print(daVe + "Anyways im gonna tell you my favorite number")
        print(daVe + "Copy it and restart the game to when I asked to finish the game")
        print(daVe + "29850948602984609286")
        print(daVe + "Its been fun talking to you, see you soon!")
    else:
        print(steVen + "bark bark.")
        print(daVe + "OH NO NOT AGAIN")
        for i in range(10):
            print(daVe + " DONT LET HIM TAKE ME")
        for i in range(10):
            print(steVen + "bark bark bark")
        print(steVen + "n o w  i t s  t i m e  t o  g o  d a v e")
        print("Ethan: hi its the dev sorry that happened, in exchange for seeing that ill tell you a secret")
        print("Ethan: when the program starts up type easterEgg instead on go")
        print("Ethan: anyways I have to go fix dave quickly")
        print("hopefully we wont meet again")
        print("anyways you can reset now")





#second floor
def med():
    print(daVe + "Welcome too floor two congrats on making it this far!")
    print(daVe + "ok since were such good friends now")
    print(daVe + "ill give you a choice")
    print(daVe + "Ill give you half the Doug now BUT if you get the question I ask for it wrong you have to reset?(1)")
    print(daVe + "orrrrr just play the second level normally(2)")
    optionTwo()
    if checKtwo == 1:
        print(daVe + "whats my favorite number?")
        favNumber = input("enter my favorite number here: ")
        if favNumber == "29850948602984609286":
            breakDown()
        else:
            print(daVe + "nice try, ill give you a hint for next time, it starts with a 2 and ends in a 6 ;)")
            dead()
           
    elif checKtwo == 2:
        print(daVe + "That was the right choice;)")
        print(daVe + "ok well this level is simple")
        print(daVe + "Just a normal 1 or 2 question")
        print(daVe + "one kills you the other passes you")
        print(daVe + "Im not supposed to tell you this but 1 will kill you and 2 will let you pass")
        optionTwo()
        if checKtwo == 1:
            print(daVe + "wow you didnt trust me:(")
            print(daVe + "Its alright i was lying anyways")
            print(daVe + "congrats on passing ill send you up in one sec")
            lastF()
        else:
            print(daVe + "Lol dont belive everything you hear kids!")
            dead()
            med()
    else:
        med()
           

#start
def start():
        print(daVe + 'Whats your name?')
        name = input("Name: ")
        print(daVe + "Nice to meet you " + name + " im dave!")
        print(daVe + "Ok so you walk in a dungeon for a quest")
        print(daVe + "Do you got left(1) or right(2) ?")
        optionTwo()
        if checKtwo == 1:
            print(daVe + "You go left and find a dog named Steven")
            steve()
            if checK == 1:
                print(steVen + "bark...")
                dead()
                start()
            else:
                print("bark!")
                print(daVe + "good job im sending you too the next floor now!")
                med()
        elif checKtwo == 2:
            dead()
            start()
       

#first part
def firstGame():
    print(daVe + "Wanna play a game?")
    option()
    if checK == 1:
        print(daVe + "Alright lets get started!")
        start()
    else:
        print(daVe + ":(")
        firstGame()
       
       
#menu
def menu():
    print("=======================")
    print("Quest for the Doug!")
    print("=======================")
    print("Type go in the box to start!")
    introStart = input("Write answers here: ")
    if introStart == "easterEgg":
        mkeke()
    elif introStart == "ethan":
        breakDown()
    else:
        firstGame()

#prompt to start
menu()
