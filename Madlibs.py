"""Hello, today we are going to create a program called Madlibs. Mad Libs are stories with blank spaces that a reader can fill in with their own words.

"""

#informing the user the program has started
print "Mad Libs is starting!"

name = raw_input("Enter a name: ")
adjective1 = raw_input("Enter an adjective: ")
adjective2 = raw_input("Enter another adjective: ")
adjective3 = raw_input("Enter the last adjective: ")
verb1 = raw_input("Enter a verb: ")
verb2 = raw_input("Enter another verb: ")
verb3 = raw_input("Enter the last verb: ")
noun1 = raw_input("Enter a noun: ")
noun2 = raw_input("Enter another noun: ")
noun3 = raw_input("Enter the third noun: ")
noun4 = raw_input("Enter the last noun: ")
animal = raw_input("Enter a type of animal: ")
food = raw_input("Enter a type of food: ")
fruit = raw_input("Enter a type of fruit: ")
number = raw_input("Enter a number: ")
superhero = raw_input("Enter a superhero name: ")
country = raw_input("Enter the name of a country: ")
dessert = raw_input("Enter a type of dessert: ")
year = raw_input("Enter a year: ")

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (adjective1, name, verb1, adjective2, noun1, noun2, animal, food, verb2, noun3, fruit, adjective3, name, verb3, number, name, superhero, superhero, name, country, name, dessert, name, year, noun4)