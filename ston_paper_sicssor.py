# make it by defining the values to a matrix 
# different for all the cases that are the desired output of the game 
# taake the random value fform the computer defining the stone paper siccor and make the user  to give the input of the player'         
global game 
game = [
    [0,-1,1],
    [1,0,-1],
    [-1,1,0]
]
my_list = [0,1,2]

import random as r

def st_pap_sci():
    
    while True :
      i = int(input("Enter the number between 0 , 1 , 2 : "))
      try :
        if 0 <= i <= 2 :
            break 
        else :
           print("enter the valid number in the range !! ")
           
      except :
         raise ValueError("that's not the desired  number . Enter the number among 0 , 1 , 2 :")

    j = r.choice(my_list)
        
    if i == j :
            print(" Ohh ! 🤷‍♂️ its A draw !!")
            st_pap_sci()
    elif game[i][j] == -1 :
            print("OPPS !! Better Luck Next Time !!")
            g = input('''Want To Play again \n press "Y" for yes \n Press "N" for No ''')
            if g =='Y':
                st_pap_sci()
            else :
                return 
    else :
            print("You Won ")
            g = input('''Want To Play again \n press "Y" for yes \n Press "N" for No ''')
            if g =='Y':
                st_pap_sci()
            else :
                return 

print("THe Game Rules :\n 0 = Stone \n 1 = paper \n 2 = scissor")
st_pap_sci()
