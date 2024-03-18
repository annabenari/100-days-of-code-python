#Day 1


print("hello")
print("I am learning Python")
# This prints to the Console

print("""This Prints
      To The Console 
            Exactly how I 
                typed  it on the screen""")
# Using triple "" will print the text to the console exactly how I i typed it e.g. spacing and different line


#Day 2

#This comes up with the line and it gives the user a chance to put an input in e.g put "Anna" and then press enter
input("What's your name?: ")

#input asks for something, takes it, but then has nowhere to put it. We can change that with a variable which is a value that we can use to name and store data.
myName = input("What's you name?: ")
myAge = input("How old are you? :")
print("Gee, that's REALLY OLD")
replit = input("Do you like Replit?")
print("OF COURSE YOU DO!")

#We now have three variables, myName, myAge and replit.

#if there is nothing inside the () then a blank line is added for a bit of space
print()
print("So, you are")
print(myName)
print("and are the ripe old age of")
print(myAge)
print("and clearly think that Replit is")
print(replit)


#Challenge
#Asks for the user's name, favorite food, favorite music and where they live (or you can create other questions!)

userName = input("What is your Username?")
favFood = input("What is your favorite food?")
favMusic = input("What is your favorite music?")
print()
print("So you are telling me your favourite things are " + favFood + " " + favMusic + "?")
print("Thank you for sharing " + userName + "!")