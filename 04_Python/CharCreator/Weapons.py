import random
# name, min damage, max damage
weaponList ={1: ["Grizzled Sword", 25, 75], 2: ["Hardy Bow", 10, 55]}
randColor = ["Alabaster", "Vermillion", "Scarlet", "Opalescent", "Cetrine"]

def IsCrit(randAttack, minAttack, maxAttack):
    if maxAttack - randAttack < 6:
        return True
    else:
        return False
    

def CritAttack(randAttack, mod):
    return randAttack * mod

def attack (minAttack, maxAttack):
    randAttack =random.randint(minAttack, maxAttack)
    if IsCrit(randAttack, minAttack, maxAttack):
        print("Crit Attack")
        return CritAttack(randAttack, 2)
    return randAttack