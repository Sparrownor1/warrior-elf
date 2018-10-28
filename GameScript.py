from ClassSetup import *
from GameFunctions import *

select = chooseCharacter()

player = setupCharacter(select[0], select[1])
player.printStats()
monster = monsterList[randint(0,2)]
print("You are fighting a", monster._race + "!")
input()
monster.printStats()
print("LET THE BATTLE BEGIN! \n")
input()

while True:
    player.turn(player, monster)
    if checkGameOver(player, monster) == True:
        break
    monster.turn(player)
    if checkGameOver(player, monster) == True:
        break
