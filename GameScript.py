from ClassSetup import *
from GameFunctions import *

select = chooseCharacter()

player = setupCharacter(select[0], select[1])
player.printStats()
monster = chooseMonster()
print("You are fighting a", monster._race + "!")
time.sleep(2)
monster.printStats()
print("LET THE BATTLE BEGIN! \n")
time.sleep(2)

while True:
    player.turn(player, monster)
    if checkGameOver(player, monster) == True:
        break
    monster.turn(player)
    if checkGameOver(player, monster) == True:
        break
