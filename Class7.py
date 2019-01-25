#class Shark:
    #kind = "mammal"

    #def __init__(self,start_x, start_y):
        #self.x = start_x
        #self.y = start_y

    #def move(self):
        #self.x = self.x + 1
        ##print(self.x)
        #if self.kind == "mammal":
            #print("sharky")

#
#i=0
#while i<100:
    #enemy1.move()
    #i = i + 1

#class Enemy:
    #kind = "Monster"
    #weapon = "claws"

    #def __init__(self,name,clan,ability):
        #self.name = name
        #self.clan = clan
        #self.ability = ability

#enemy1 = Enemy("Clive", "Mangekyo Uchiha", "Razor shell")
#enemy2 = Enemy("Jason", "Uzumaki", "Swords dance")
#print(enemy1.name)
#print(enemy1.clan)
#print(enemy1.ability)


#print(enemy2.name)
#print(enemy2.clan)
#print(enemy2.ability)


class Player:
    health = "playerHealth"
    mana = "playerMana"
    Stamina = "PlayerStamina"

    def __init__(self):
        self.health = 100
        self.mana = 100
        self.stamina = 100

player = Player()
print(player.health)
print(player.mana)
print(player.stamina)








#class Collectable:
    #colour = "Red"




##class Collectable2:
    #colour = "Blue"
