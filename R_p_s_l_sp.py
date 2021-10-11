import random
numwins=0
numlosses=0
numties=0
done=False
while(done==False):
    num=random.randint(1,5)
    if num==1:
        compchoice="r"
    elif num==2:
        compchoice="p"
    elif num==3:
        compchoice="s"
    elif num==4:
        compchoice="l"
    else:
         compchoice="sp"
    userchoice = (input("Enter r(rock) p(paper) s(scissors) l(lizard) sp(spock) ex(exit):"))
    if userchoice =="r":
        if compchoice =="r":
            print("You both chose rock(TIE)")
            numties=numties+1
        elif compchoice =="p":
            print("Paper covers rock so you LOSE")
            numlosses=numlosses+1
        elif compchoice =="l":
            print("Rock crushes lizard's scull,you WIN")
            numwins=numwins+1
        else:
            print("Rock beats scissors you WIN")
            numwins=numwins+1
    if userchoice=="p":
        if compchoice=="p":
            print("You both chose paper(TIE)")
            numties=numties+1
        elif compchoice =="s":
            print("Scissors cuts paper so you LOSE")
            numlosses=numlosses+1
        elif compchoice =="l":
            print("Lizard eats paper so you LOSE")
            numlosses=numlosses+1
        elif compchoice =="sp":
            print("Paper disproves Spock you WIN")
            numwins=numwins+1
        else:
            print("Paper covers rock(not really) you WIN")
            numwins=numwins+1  
    if userchoice =="s":
        if compchoice =="s":
            print("You both chose scissors(TIE)")
            numties=numties+1
        elif compchoice =="r":
            print("Rock VICIOUSLY PULVERIZERS SCISSORS INTO A PILE OF TWISTED METAL so you LOSE")
            numlosses=numlosses+1
        elif compchoice =="sp":
            print("Spock dismantles scissors you LOSE")
            numlosses=numlosses+1
        elif compchoice =="l":
            print("Scissors DECAPITATES lizard, you WIN")
            numwins=numwins+1
        else:
            print("Scissors cuts paper you WIN")
            numwins=numwins+1
    if userchoice=="l":
        if compchoice=="l":
            print("You both chose lizard(TIE)")
            numties=numties+1
        elif compchoice=="r":
            print("Rock VICIOUSLY BEATS LIZARD'S SKULL so you LOSE")
            numlosses=numlosses+1
        elif compchoice=="s":
            print("Scissors DECAPITATES lizard so you LOSE")
            numlosses=numlosses+1
        elif compchoice=="sp":
            print("Lizard POISIONS spock,you WIN")
            numwins=numwins+1
        else:
            print("Lizard eats paper,you WIN")
            numwins=numwins+1
    if userchoice =="sp":
        if compchoice =="sp":
            print("You both chose Spock(TIE)")
            numties=numties+1
        elif compchoice =="l":
            print("Lizard poisons Spock,so you LOSE")
            numlosses=numlosses+1
        elif compchoice =="p":
            print("Paper DISPROVES Spock, you LOSE")
            numlosses=numlosses+1
        elif compchoice =="s":
            print("Spock dismantles scissors, you WIN")
            numwins=numwins+1
        else:
            print("Spock VAPORIZES rock,you WIN")
            numwins=numwins+1
    if userchoice=="ex":
        print ("Ties:",numties)
        print ("Wins:",numwins)
        print ("Losses:",numlosses)
        print ("Your W/L ratio:",(numwins/numlosses))
        done=True
