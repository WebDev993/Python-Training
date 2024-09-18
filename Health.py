import random

#setting vars
health = 50
difficulty = 2

#random number generation
potionHealth = int(random.randint (25,50)/ difficulty)


#adding potionHealth to Health
health = health + potionHealth


#showing new health
print(health)
