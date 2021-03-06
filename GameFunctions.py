from random import randint
from ClassSetup import *

raceList = [None, Elf(), Human(), Dwarf()]
classList = [None, Warrior(), Mage(), Hunter()]
monsterList = [None, Orc(), Kodo(), Dragon()]

def chooseCharacter():
#add spell details
    print("CHARACTER SELECT: CHOOSE YOUR FIGHTER")
    while True:
        print(
            "Choose your race: \n"
            "1: Elf - Health = 20, Speed = 10 \n"
            "2: Human - Health = 30, Speed 8 \n"
            "3: Dwarf - Health = 40, Speed 5 \n"
            )
        classNo=0
        while True:
            try:
                raceNo = int(input())
                break
            except ValueError:
                print("Please try again")
        if raceNo >= 1 and raceNo <= 3:
            break
        else:
            print("Invalid input. Try again \n")

    while True:
        print(
            "Choose your class: \n"
            "1: Warrior - Basic Attack: Damage - 5, Range = 2 \n"
            "   Spell: Tank Up, 3 Mana - Gain 10 Health \n"
            "2: Mage - Basic Attack: Damage - 2, Range = 20 \n"
            "   Spell: Pyroblast, 3 Mana - Deal 6 Damage \n"
            "3: Hunter - Basic Attack: Damage - 3, Range = 10 \n"
            "   Spell: Teleport, 2 Mana - Teleport to any position \n"
            )
        classNo=0
        while True:
            try:
                classNo = int(input())
                break
            except ValueError:
                classNo = print("Please try again: ")
        if classNo >=1 and classNo <=3:
            break
        else:
            print("Invalid input. Try again \n")

    return classNo, raceNo

def setupCharacter(classNum,raceNum):
    character = Player(myClass = classList[classNum], myRace = raceList[raceNum])
    return character

def checkGameOver(player, enemy):
    if player.getHealth() <= 0 or enemy.getHealth() <= 0:
        print("GAME OVER \n")
        if player.getHealth() > 0:
            print("YOU WIN! \n")
        else:
            print("YOU LOSE! \n")
        return True
    else:
        return False

def chooseMonster():
    print("Press 1 to choose a monster \n"
    "Press 2 to fight a random monster\n")
    decision = 0
    while decision not in [1,2]:
        try:
            decision = int(input())
        except ValueError:
            print("Invalid Input. Try again: ")
    if decision == 2:
        monster = monsterList[randint(1,3)]
    elif decision == 1:
        print(
        """Choose a monster:
1: Orc
2: Kodo
3: Dragon """)
        decision2 = 0
        while decision2 not in [1,2,3]:
            try:
                decision2 = int(input())
            except ValueError:
                print("Invalid Input. Try again: ")
        monster = monsterList[decision2]

    return monster
