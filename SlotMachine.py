#Slot Machine Game

import random
symbols =['Carrot','Apples','Cherry','Chives']

while True:
    Dollars = 100
    print("Welcome to Denis's slot machine game")
    while Dollars > 0:
        print("You have",Dollars,'dollars.')
        try:
            bet = int(input('How many dollars will you bet?:'))
        except:
            print('Type a whole amount of dollars, no decimals or words')
            continue #repeats the loop to test the condition again
        if bet > Dollars:
            print('Not enough money.')
        else:
            Dollars -= bet

            
            #Designing the slot game
            square1=random.choice(symbols)
            square2=random.choice(symbols)
            square3=random.choice(symbols)
            square4=random.choice(symbols)
         

            print()
            print('================================================')
            print('[|]',random.choice(symbols),'|\|',random.choice(symbols),'|||',random.choice(symbols),'|/|',random.choice(symbols),'[|]')
            print('------------------------------------------------')
            print('[|]',square1,'|\|',square2,'|||',square3,'|/|',square4,'[|]')
            print('------------------------------------------------')
            print('[|]',random.choice(symbols),'|\|',random.choice(symbols),'|||',random.choice(symbols),'|/|',random.choice(symbols),'[|]')
            print('================================================')
            print()


            #Odds of the slot machine (each win has it's own different message depending on the amount won)
            if square1 == square2 and square2 == square3 and square3 == square4:
                amountwon = bet*32
                print('JACKPOT! YOU WON',amountwon,'DOLLARS!!!!')
                Dollars += amountwon
            if square1 == square2 and square2 == square3:
                amountwon = bet*16
                Dollars += amountwon
                print('You won',amountwon,'dollars!')
            if square2 == square3:
                amountwon = bet*2
                Dollars += amountwon
                print('You got',amountwon,'dollars')
            else:
                print('You lost!')
print('You are out of money.')
print('Come back next time!')
print()
            
                      
            

        

            


        

        

            
                


          
