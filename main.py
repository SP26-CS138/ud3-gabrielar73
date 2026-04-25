'''
DEVELOPER(S): Gabriela Ramirez
COLLABORATORS: <anyone who helped you>
DATE: 04/17/2026
'''

"""
This program takes user input of number of cats, their names and weights and uses this information to calculate the amount of dry food and water a cat should consume each day based on their body weight. It then uses this to make a list of each cat and create a file output.

Leave one blank line.  The rest of this docstring should contain an
overall description of the program.
"""

##########################################
# IMPORTS:
# No external modules needed.
##########################################
# I chose to use lists to store my cats data as I personally am more comfortable with them and I also feel they would allow me to make my code organized and easy to read.
##########################################
# FUNCTIONS:
##########################################

def cat_data():
    cats = []
    number = int(input("How many cats do you own? "))
    for i in range(number):
        name = input("What is your cat's name? ")
        weight = float(input(f"What is {name}'s body weight in pounds? "))

        dry_food = weight * 0.2 
        water = weight * 0.8
        cats.append([name, "dry food:", dry_food, "water:", water])
    print("Data for cats daily diet in ounces:")
    print(cats)
    return cats

def catfile(cats):
    with open("catfile", "w") as file:
        for cat in cats:
            file.write(str(cat) + "\n")

##########################################
# MAIN PROGRAM:
##########################################
if __name__ == "__main__":
    cats = cat_data()
    catfile(cats)