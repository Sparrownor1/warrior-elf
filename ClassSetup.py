from random import randint
import time
#Change: Positions not printed
#Changed inputs to sleep

class Player:

    def __init__(self, myClass, myRace, hp = 20, position = 0, speed = 5):

        self.myClass = myClass
        self.myRace = myRace
        self._hp = hp + self.myRace.healthModifier
        self._position = position
        self._speed = speed + self.myRace.speedModifier
        self._mana = 0
        self.hasMoved = False
        self.hasAttacked = False
        self.hasCast = False

    def basicAttack(self, target):
        #Checks if target is in range
        if abs(self.getPosition() - target.getPosition()) <= self.myClass.basic.getRange():
            target.takeDamage(self.myClass.basic.getDamage())
            print("Attack successful: Enemy is now at a health of", target.getHealth(), "\n")
            self.attacked()
        else:
            print("Enemy is out of range. \n")
            self.attacked()

    def move(self, distance):

        if distance <= self.getSpeed():
            self._position += distance
            # print("You are now at a position of", self.getPosition(), "\n")
            self.moved()
        else:
            print("This movement is out of range. Try again \n")

    def spellCast(self, player, enemy):

        if self.getMana() >= self.myClass.spell.getManaCost():
            self.myClass.spell.cast(player, enemy)
            self.decreaseMana(self.myClass.spell.getManaCost())
            self.casted()
            self.printStats()
        else:
            print("You do not have the available mana to cast this spell \n")
            self.casted()

    def printStats(self):
        print(
            "You are a", self.myClass.name, self.myRace.name, "\n"
            "Your health is", self.getHealth(), "\n"
            "You have", self.getMana(), "mana available \n"
            "Your basic attack damage is", self.myClass.basic.getDamage(),
            "with a range of", self.myClass.basic.getRange(), "\n"
            # "You are at position of", self.getPosition(), "\n"
            "You can move", self.getSpeed(), "blocks", "\n"
            )

    def printDistance(self, enemy):
        print("You are", abs(self.getPosition() - enemy.getPosition()),
        "blocks away from your enemy\n")
        time.sleep(2)

    def printControls(self):

        print("""CONTROLS:
Type 'move' or 'm' to move
Type 'attack' or 'a' to attack
Type 'spell' or 'cast' to cast a spell
Type 'end' or 'e' to end your turn
                """)

    def turn(self, player, enemy):
        print("It is your turn \n")
        self.resetMoved()
        self.resetAttacked()
        self.resetCast()
        self.increaseMana(1)
        self.printStats()
        self.printDistance(enemy)
        self.printControls()
        while self.getMoved() == False or self.getAttacked() == False or self.getCast() == False:
            decision = input("What would you like to do? \n")
            if (decision == 'move' or decision == 'm'):
                if self.getMoved() == True:
                    print("You have already moved.")
                while self.getMoved() == False:
                    self.move(int(input(
                                    "How far would you like to move? \n"
                                    )))
                    self.printDistance(enemy)
            elif decision == 'attack' or decision == 'a':
                if self.getAttacked() == True:
                    print("You have already attacked.")
                while self.getAttacked() == False:
                    self.basicAttack(enemy)
                if enemy.getHealth() <= 0:
                    break
            elif (decision == 'cast' or decision == 'spell'):
                if self.getCast() == True:
                    print("You have already cast a spell.")
                while self.getCast() == False:
                    self.spellCast(player, enemy)
            elif decision == 'end' or decision == 'e':
                break
            else:
                print("Invalid Input \n")
    'Health'
    def takeDamage(self, damage):
        self._hp -= damage

    def buffHealth(self, healthBuff):
        self._hp += healthBuff

    def setHealth(self, newHealth):
        self._hp = newHealth

    def getHealth(self):
        return self._hp

    'Position'
    def getPosition(self):
        return self._position

    def setPosition(self, position):
        self._position = position

    'Speed'
    def getSpeed(self):
        return self._speed

    'Mana'
    def getMana(self):
        return self._mana

    def decreaseMana(self, amount):
        self._mana -= amount

    def increaseMana(self, amount=1):
        self._mana += amount

    'Turn Booleans'
    def resetMoved(self):
        self.hasMoved = False

    def moved(self):
        self.hasMoved = True

    def getMoved(self):
        return self.hasMoved

    def resetAttacked(self):
        self.hasAttacked = False

    def getAttacked(self):
        return self.hasAttacked

    def attacked(self):
        self.hasAttacked = True

    def getCast(self):
        return self.hasCast

    def resetCast(self):
        self.hasCast = False

    def casted(self):
        self.hasCast = True


'Classes'
class Class:

    def __init__(self):
        pass

class Warrior(Class):

    def __init__(self):

        'Sword basic attack'
        self.basic = Basic(5,2)
        self.name = "Warrior"
        self.spell = TankUp()

class Hunter(Class):

    def __init__(self):

        'Bow basic attack'
        self.basic = Basic(3,10)
        self.name = "Hunter"
        self.spell = Teleport()

class Mage(Class):

    def __init__(self):

        'Fireblast basic attack'
        self.basic = Basic(2,20)
        self.name = "Mage"
        self.spell = PyroBlast()

'Weapons'
class Basic:

    def __init__(self, damage, range):
        self._damage = damage
        self._range = range

    def getDamage(self):
        return self._damage

    def setDamage(self, newDamage):
        self._damage = newDamage

    def getRange(self):
        return self._range

    def setRange(self, range):
        self._range = range

'Magic'
class Spell:

    def __init__(self, manaCost):
        self._manaCost = manaCost

    def getManaCost(self):
        return self._manaCost

class TankUp(Spell):

    def __init__(self, manaCost=3):
        super().__init__(manaCost)


    def cast(self, player, enemy):
        player.buffHealth(10)
        print("Your health increased by 10.")

class PyroBlast(Spell):

    def __init__(self, manaCost=3):
        super().__init__(manaCost)

    def cast(self, player, enemy):
        enemy.takeDamage(6)
        print("You dealt 6 damage.")

class Teleport(Spell):

    def __init__(self, manaCost=2):
        super().__init__(manaCost)

    def cast(self, player, enemy):
        while True:
            position = int(input("What position would you like to Teleport to? \n"))
            if type(position) == int:
                break
            else:
                print("You must enter an integer")
        player.setPosition(position)
        print("You teleported to position", position)



'Races'
class Race:

    def __init__(self, healthModifier=0):
        self.healthModifier = healthModifier

class Elf(Race):

    def __init__(self):
        super().__init__(healthModifier = 0)
        self.name = "Elf"
        self.speedModifier = 5

class Human(Race):

    def __init__(self, healthModifier = 10):
        super().__init__(healthModifier)
        self.name = "Human"
        self.speedModifier = 3

class Dwarf(Race):

    def __init__(self, healthModifier = 20):
        super().__init__(healthModifier)
        self.name = "Dwarf"
        self.speedModifier = 0

'Monsters'
class Monster:

    def __init__(self, race, hp, dmg, range, speed, pos=20):
        self._hp = hp
        self._damage = dmg
        self._position = pos
        self._range = range
        self._race = race
        self._speed = speed

    def attack(self, enemy):
        if abs(self.getPosition() - enemy.getPosition()) <= self.getRange():
            enemy.takeDamage(self.getDamage())
            print("Enemy attack succesful: Your health is now", enemy.getHealth(), "\n")
        else:
            print("Enemy Attack: You were out of the enemy's range. No damage taken. \n")
        time.sleep(2)

    def takeDamage(self, damage):
        self._hp -= damage

    def move(self, distance):
        self._position -= distance
        if distance == 0:
            #no move
            print("Enemy movement: The enemy did not move")
        else:
            #Enemy has moved
            print("Enemy movement:The enemy has moved and is now at a position of", self.getPosition())
        time.sleep(2)

    def getPosition(self):
        return self._position

    def getHealth(self):
        return self._hp

    def setHealth(self, health):
        self._hp = health

    def getDamage(self):
        return self._damage

    def getRange(self):
        return self._range

    def getSpeed(self):
        return self._speed

    def printStats(self):
        print(
            "The enemy's health is", self.getHealth(), "\n"
            # "They are a", self._race, "\n"
            "Their basic attack damage is", self.getDamage(),
            "with a range of", self.getRange(), "\n"
            # "They are at a position of", self.getPosition()
            )
        time.sleep(2)

    def printDistance(self, enemy):
        print("They are", abs(self.getPosition() - enemy.getPosition()),
        "blocks away from you")
        time.sleep(2)

    def turn(self, enemy):
        print("\nIt is the computer's turn. \n")
        time.sleep(2)
        self.printStats()
        self.printDistance(enemy)
        self.move(randint(0,self.getSpeed()))
        self.attack(enemy)

class Orc(Monster):

    def __init__(self, race="Orc", hp=40, dmg=2, range=3, speed=3):
        super().__init__(race, hp, dmg, range, speed)

class Kodo(Monster):

    def __init__(self, race="Kodo", hp=30, dmg=4, range=2, speed=4):
        super().__init__(race, hp, dmg, range, speed)

class Dragon(Monster):

    def __init__(self, race="Dragon", hp=20, dmg=2, range=5, speed=6):
        super().__init__(race, hp, dmg, range, speed)

raceList = [None, Elf(), Human(), Dwarf()]
classList = [None, Warrior(), Mage(), Hunter()]
monsterList = [Orc(), Kodo(), Dragon()]
