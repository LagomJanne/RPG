import random


loot = ["sten", "äpple", "1kg jord", "5g mjöl", "lång pinne"]

randomLoot = random.randint(0, 4)

def get_loot():
    print(loot[randomLoot])


get_loot()

