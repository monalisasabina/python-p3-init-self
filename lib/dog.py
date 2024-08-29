#!/usr/bin/env python3

# class Dog:

#     def __init__(self, name):
#       self.name = name

# fido =Dog("Fido")      

# # fido.owner = "Sophie"
# # print(fido.owner)

# fido.food = "Chapati madondo"
# print(fido.food)

# def adopt(dog, owner_name):
#     dog.owner = owner_name

# adopt(fido,"Sophie")

# print(fido.owner)

# ....................................................................
# Refactoring the code above 

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print("Woof!")

#     def get_adopted(self, owner_name):
#         self.owner = owner_name

# fido =Dog("Fido")
# print(fido.name)

# fido.bark()

# fido.get_adopted("Sophie")
# print(fido.owner)     


# .....................................................................
# optional argument

# class Dog:
#     def __init__(self, name, favorite_toy="Any"):
#         self.name = name
#         self.favorite_toy = favorite_toy

# fido = Dog("Fido")
# fido.favorite_toy
# print(fido.favorite_toy)


# snoopy = Dog("Snoopy", "Tennis Ball")
# snoopy.favorite_toy
# print(snoopy.favorite_toy)

# old_yeller = Dog()

# ..............................................................
# LAB

class Dog:
    def __init__(self,name,breed = "Mutt"):
        self.name = name
        self.breed = breed





    



    
 

