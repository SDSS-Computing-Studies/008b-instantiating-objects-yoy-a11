#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""

class pet:
    type_pet = None
    breed = None
    name = None
    owner = None
    birth_date = None

    def __init__(self, type_pet, breed, name, owner, birth_date):
        self.type_pet = type_pet
        self.breed =breed
        self.name = name
        self.owner = owner
        self.birth_date = birth_date

    def display(self):
        print(self.name + " " + self.type_pet)
        print(self.breed + "  is owned by " + self.owner)


def display_menu():
    print("1. Enter a new pet")
    print("2. Retrieve a pet")
    print("3. Exit")

def register_new_pet():
    print("Type of animal?", end=" ")
    type_pet = input()
    print("Breed?", end=" ")
    breed = input()
    print("Name?", end=" ")
    name = input()
    print("Owner?", end=" ")
    owner = input()
    print("Birthdate?", end=" ") 
    birth_date = input()
    p = pet(type_pet, breed, name, owner, birth_date)
    return p

def retrieve_pet(pet_list):
    print("Which Pet?", end=" ")
    name = input()
    for p in pet_list:
        if p.name == name:
            p.display()

def main():
    pet_list = []
    while True:
        display_menu()
        option = input()
        print()
        if option == "3":
            break
        elif option == "2": 
            retrieve_pet(pet_list)
        elif option == "1": 
            pet_list.append(register_new_pet()) 

#main()