
# =============================
# main.py
# ============================

# We will import python file player.py
# NOTE: that we import player with small p (the python.py file) and not Python with capital P.
# NOTE: that "dylan" is assigned "player.Player("Dylan") and we pass name "Dylan" to it.
# python (small p) is python.py file while Player (capital p) is the Player class defined in player.py file.

import player

dylan = player.Player("Dylan")  # dylan is assigned

# Then we print initial values for new player "dylan"

print("Dylan's initial name  = {}".format(dylan.name))
print("Dylan's initial lives = {}".format(dylan.lives))
print("Dylan's initial level = {}".format(dylan.level))
print("Dylan's initial score = {}".format(dylan.score))


# =====================================
# Another way to import Player class
# =====================================

# We can also import class Player from file player as follows
# NOTE that this method of importing is not recommended because there is risk of confusion.
# In large programs, we may not know where class Player was imported from.
# its better to use "player.Player" format above

from player import Player

dylan = Player("Dylan")  # Here we only refer to Player (already imported) instead of player.Player

# Then we print initial values for new player "dylan"

print("Dylan's initial name  = {}".format(dylan.name))
print("Dylan's initial lives = {}".format(dylan.lives))
print("Dylan's initial level = {}".format(dylan._level))
print("Dylan's initial score = {}".format(dylan._score))

# =============================
# Modifying Player attributes
# =============================

# Say someone is playing and loses some of their lives.
# we can reduce the lives as follows
# We see the code below is accessing the Player class attributes to print them or alter them
# The Player attributes (name, lives, level, score) are encapsulated in Player class but are not hidden
# So providing direct access to data attributes is allowed in python ( unlike in C or C++)

print("="*40)
dylan.lives -= 1  # reduce dylan.lives by 1
print("Dylan's New lives = {}".format(dylan.lives))  # Now we see new lives are 2


# ===============================
# Getters and setters
# ===============================

# NOTE: in python, it is not advisable to use getters and setters but we will still learn them here

# In python, you can add a getter or setter both during or after you've created a class, and any code using the
# class will continue to work fine.
# In java or C++, that is not possible. if you allow access to a class instance variables and then later decide
# to make them private, any code that uses the class will have to be changed to use the getters and setters instead
# in python, current code using the class is not affected.

# A "Getter" is a method that is used to get the value of a data attribute.
# Here are examples of getters
# The "get_name" method is called a getter and it normally returns the value of the corresponding variable.
# A getter can also do for example multilications, additions etc

# NOTE that you have to define attributes "get_name" and "set_lives" in the original Player class in player.py file
# if you run this, you get error "AttributeError: 'Player' object has no attribute 'get_name'"

# print("="*40)
# print("Using get_name:")
# print(dylan.get_name())

# A "Setter" is a method that is used to set the value of the class data attribute
# In below setter example, we are setting dylan.lives to 300
# in a setter, you can also check the value of the attribute, say make sure lives are more than 0 and not set to negative lives.

# if you run this, you get error "AttributeError: 'Player' object has no attribute 'set_lives'"
# this is because you need to create set and get methods in Player class

# print("="*40)
# print("Using set_lives:")
# dylan.set_lives(300)


# =========================
# Check test for negative:
# =========================

# We will decrement the number of lives to negative and see if our test in player.py works

print("="*40)
dylan.lives -= 1  # reduce dylan.lives by 1
print("Dylan's New lives = {}".format(dylan.lives))  # Now we see new lives are 2

print("="*40)
dylan.lives -= 1  # reduce dylan.lives by 1
print("Dylan's New lives = {}".format(dylan.lives))  # Now we see new lives are 2

# Note that below code prints "Lives cannot be negative"
# Hence the test in player.py works

print("="*40)
dylan.lives -= 1  # reduce dylan.lives by 1
print("Dylan's New lives = {}".format(dylan.lives))  # Now we see new lives are 2

# Note that even if _lives beginning with _ in player.py file is for private variable
# python does not enforce it and you can still access them from another file e.g. here in main.py
# The _ is just a way to indicate that the variable is private and you should not use it.

print("="*40)
dylan._lives = 9
print("Dylan's New lives  = {}".format(dylan.lives))


# VITAL: do not give a property the same name as a data attribute.
# Attribute ==> self._lives = 3 in player.py
# property ==> "lives = property(_get_lives, _set_lives)" in line 73 in player.py

# ================================
# Test the Challenge in player.py
# ================================

# We will now test the challenge solution in player.py here
# check the levels and scores. When level increase to 2, score is 1000
# When level increases to 7, score is existing 1000 + 5000 = 6000
# when level reduces by 4 to 3, then score is 6000 - 4000 = 2000

print("="*40)
dylan.level = 2
print(dylan)

print("="*40)
dylan.level += 5
print(dylan)

print("="*40)
dylan.level = 3
print(dylan)

# =========================================================
# Test alternate syntax for writing property in player.py:
# =========================================================

# After running this, we see score is changed to 500

print("="*40)
dylan.score = 500
print(dylan)




# =====================================================
# Inheritance
# =====================================================


# This is where you have a superclass, and subclasses
# Subclasses inherit the characteristics of superclass

# we will create a superclass called "enemy.py"


# Now that the enemy.py superclass is created, we will make an instance of enemy to test it

print("="*40)
print("Calling enemy class:")
print("="*20)
print()
# first we import Enemy from enemy.py

from enemy import Enemy

# then we create an enemy instance called random_monster with characteristics of enemy
# we pass it name = basic enemy, hit_points = 12 and lives = 1

random_monster = Enemy("Basic Enemy", 12, 1)
print(random_monster)

# Then we give it damage of 4

print("="*20)
random_monster.take_damage(4)
print(random_monster)

# Now we take 8 points of damage to bring the hit_points to 0
# We still have 1 live left

print("="*20)
random_monster.take_damage(8)
print(random_monster)

# And then take another 4 points to bring the hit_points to -4
# After hit_points goes to -4, we now have 0 lives (1-1 = 0)

print("="*20)
random_monster.take_damage(4)
print(random_monster)


