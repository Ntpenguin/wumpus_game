# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Nathanael Baron
#               Nathanael Kamat
#               Ajith Roy
#               Kyle Grimes
# Section:      524
# Assignment:   Wumpus Code - Final Project
# Date:         12/7/22

from random import *

cave = {1: [2, 5, 8], 2: [1, 3, 10], 3: [2, 4, 12], 4: [3, 5, 14], 5: [1, 4, 6],
       6: [5, 7, 15], 7: [6, 8, 17], 8: [1, 9, 7], 9: [8, 10, 18], 10: [2, 9, 11],
       11: [19, 10, 12], 12: [11, 3, 13], 13: [12, 20, 14], 14: [4, 13, 15],
       15: [6, 14, 16], 16: [15, 17, 20], 17: [7, 18, 16], 18: [19, 17, 9],
       19: [18, 11, 20], 20: [13, 16, 19]}

#This function gets a random number excluding the list
def randomNumExcluding(bottom, top, exclude):
   return choice(
       [number for number in range(bottom, top)
        if number not in exclude]
   )
# gets all random numbers excluding the values of the other ones so no two positions overlap
unUsable = []
player_position = randint(1,20)
unUsable.append(player_position)
wumpus_position = randomNumExcluding(1,20,unUsable)
unUsable.append(wumpus_position)
unUsable.append(player_position)
bat_positions = []
bat_positions.append(randomNumExcluding(1,20,unUsable))
unUsable.append(bat_positions[0])
bat_positions.append(randomNumExcluding(1,20,unUsable))
unUsable.append(bat_positions[1])
pit_positions = []
pit_positions.append(randomNumExcluding(1,20,unUsable))
unUsable.append(pit_positions[0])
pit_positions.append(randomNumExcluding(1,20,unUsable))

#this is the function to move the player
def player_move(p_position, want_position): #takes in the players postition and the wanted position
   global player_position #gets all the variables as global to be able to be used in this function
   global wanted_room
   global wumpus_position
   global bat_positions
   for room in cave[p_position]: #loops through possible rooms
       if want_position == room: # if a possible room matches the wanted room
           p_position = want_position
           player_position = want_position #sets player position to wanted position
   if p_position != want_position: # error message if it isn't possible
       print("It is not possible to move from", p_position, "to", want_position)
       print()
   if player_position == wumpus_position: #if you move into a room with wumpus chance he moves
       wumpus_random()
       if player_position == wumpus_position: #if it is in the same room you die
           print("You were eaten by the wumpus!")
           quit()
   if player_position == pit_positions[0] or player_position == pit_positions[1]: # if you fall into a pit you die
       print("You fell into the hole!")
       quit()
   if player_position == bat_positions[0] or player_position == bat_positions[1]: # if you go into a room with a bat it randomly drops you off
       print("The bat has dropped you in a random room!")
       player_position = randint(1,20) # random

def player_shoot(p_position):
    global wumpus_position
    global arrows
    arrow_trajectory = p_position
    arrows = 5
    arrow_room = 0
    arrows_num = int(input("Shoot through how many rooms? (1 to 5): ")) #gets player input on number of rooms the arrow shall shoot through
    arrows_list = []
    for i in range(arrows_num): #turns the player input into a list in order to iterate through it
        arrows_list.append([])
    for _ in arrows_list: #this for loop will loop as much times as the player has said it should
        if 1 <= arrows_num <= 5:
            arrow_room = arrow_room + 1
            print()
            print("Room #" + str(arrow_room), "of path")
            room = int(input(""))
            if room == p_position:
                print("You shot yourself and died!") #the player dies if they shoot the arrow into their own room
                quit()
            if room == wumpus_position:
                print("You hit the wumpus! You win") #the wumpus dies if the arrow hits it
                quit()
            elif room in cave[arrow_trajectory]:
                print("Arrow is in room", str(room), "now...")
            else:
                print("Your arrow path is not a valid one... the arrow will travel randomly")
                for _ in arrows_list:
                    room = choice(cave[arrow_trajectory]) #arrow will randomly be shot in a random direction
                    print("Arrow is in room", str(room), "now...")
                    arrow_trajectory = room
                else:
                    break
            arrow_trajectory = room #sets the position of the arrow to the room, the room being the room that the player wanted the arrow to be in
        else:
            player_shoot(6)
            break #this code will run the shoot function again if the player puts an invalid input
    if 1 <= arrows_num <= 5:
        arrows = arrows - 1
        print()
        print("You have", str(arrows), "arrows left!") #tells you how many arrows you have left at the end

def arrow_count():#checks to see if out of arrows
   if arrows == 0:
       print()
       print("You ran out of arrows and died!")
       quit()
def near_by(p_position, wum_position,b_position,pit_position): #function to check whats nearby
   for room_nearby in cave[p_position]: #loops through rooms nearby
       if room_nearby == wum_position: #checks if wumpus is near
           print("I smell a Wumpus")

       if room_nearby in b_position: #checks if bats are near
           print("Bats Nearby")

       if room_nearby in pit_position: #checks if the pits are near
           print("I feel a draft")


def wumpus_random(): #function to have a chance to move wumpus used when you shoot a arrow or you move into the sam room
   global wumpus_position
   if randint(0,100) <= 25: #25 percent change to stay in same room
       wumpus_position = wumpus_position
   else:
       random_wumpus_room = choice(cave[wumpus_position]) #75 percent chance to move to a nearby room
       wumpus_position = random_wumpus_room
       print("The wumpus has randomly moved")

print("Hunt the Wumpus!")
print()
while True: #loops through till something happens
   print("You are in room", player_position) #prints basic info
   near_by(player_position,wumpus_position,bat_positions,pit_positions)
   options = ', '.join(str(item) for item in cave[player_position])
   print("Tunnels lead to rooms", options)
   print()

   while True: #will keep going into vaild info is given
       try:
           shootOrMove = int(input("(1)Shoot or (2)move? (enter 1 or 2):"))
           if shootOrMove != 1 and shootOrMove != 2:
               print("Enter 1 or 2")
               shootOrMove = input()
       except:
           shootOrMove = print("Bad entry. ENTER A NUMBER")

       else:
           break
   if int(shootOrMove) == 2:#if you choose to move
       wanted_room = input("Where to? ")
       print()
       player_move(player_position,int(wanted_room)) # calls the move function with the given input
   if int(shootOrMove) == 1: #if you choose to shoot
       player_shoot(player_position) #calls the shoot function
       wumpus_random() #chance for wumpus to move if arrow shot

