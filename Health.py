import random

#setting vars
health = 50
difficulty = 2

#random number generation between 25-50 for potion health 
potionHealth = int(random.randint (25,50)/ difficulty)


#adding health to potion health
health = health + potionHealth


#showing new health of the player
print(health)
