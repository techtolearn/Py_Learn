# https://www.youtube.com/watch?v=KzqSDvzOFNA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=27
'''
Generate Random Numbers and Data Using the random Module
'''
import random

vale = random.random()
print(vale)
vale1 = random.randint(1,6)
print(vale1)
print("\n")
val1 = random.uniform(1,10)
print(val1)
print("\n")

# string random from the list
Greetings = ['Hi','Hello','Hey','Howdy','Hola']

val = random.choice(Greetings)
print(val,', Satheesh!')

# this example results picking random colors for 10 times, print those
Colors = ['Red','Green','Black']
col = random.choices(Colors, k=10)
print(col)
print("\n")
# this example results picking random colors for 10 times,  weights limit the number of occurrance for particular, eg [5,5,2]
# black will pick only 2 tims
Color1 = ['Red','Green','Black']
col1 = random.choices(Color1, weights=[5,5,2], k=10)
print(col1)


# this example results picking random and display after shuffling
deck = list(range(1,52))
random.shuffle(deck)
print(deck)
print("\n")

# this example results picking random and display after shuffling
deck = list(range(1,52))
hand =  random.sample(deck,k=5)  #it will random number between rangs and print 5 random numbers
print(hand)
print("\n")


