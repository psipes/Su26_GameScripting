import Player
import Weapons
userInventory = Player.inventory
userInventory["weapons"] = Weapons.weaponList
print(userInventory["weapons"][1][0])
print(Weapons.attack(userInventory["weapons"][1][1], userInventory["weapons"][1][2]))