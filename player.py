# ============================================
# Getters and Setters
# ============================================

# As we saw in previous sections, python classes do not need "Getters and Setters" to allow you to read
# and change the values of data attributes.
# Python does not make class attributes private like other OOP languages.
# Getters and setters are still useful in python even if they are not essential, so we will study them here

# In this case, we will put each of our classes in a separate python file, even if this is not necessary in python.
# In normal times, we create related classes in the same file, so that we can organize files based on functionality.

# But its easier to view them here in different files.
# We will also see a new way of importing a class.

# ==================
# player.py
# ==================

# First we will create this python file called player.py to represent people playing the game.
# Each player will have a Name, Number of lives they have, and their score

# we will start with this basic Player class.
# NOTE: Player class start with Capital P.
# NOTE: The convention is that class names should start with Capital letter,
# although some built in classes don't follow that convention.

# NOTE that we pass parameter "name" to Player class so that when each instance of Player is created
# it is given a name. The other parameters (lives, level, score) are given to each instance by default as shown.

class Player(object):

    def __init__(self, name):  # We will pass it a name in the class constructor (__init__)
        self.name = name  # this is the name we pass
        # self.lives = 3  # Player will have 3 lives initially. Use this initially without getter/setter
        self._lives = 3  # Use this with getter and setter. We hide lives attribute by prefixing it with underscore
        self.level = 1  # Player starts at level 1
        self.score = 0  # Player start with score 0


    # Now we will put all the code that uses the Player class in a python file called main.py


    # We will now add "Getter" and "setter" in our Player class
    # first we use self._lives = 3 (this hides the lives attribute)

    # Now we will create "setter" method (to set the value) and "getter" method (to get the value)
    # NOTE we are hiding these methods by starting their names with underscore ( _get_lives and _set_lives )
    # The underscore at the beginning informs users that they should not be calling these methods

    # getter method returns self._lives

    def _get_lives(self):
        return self._lives

    # setter method is passed parameter lives, which is the number of lives you want to set to self._lives
    # This method also checks that we don't set lives to negative number
    # we will go to main.py to test if this test for negative works. Check code under "Check test for negative"

    def _set_lives(self, lives):
        if lives >= 0:              # if lives we pass it is 0 or more
            self._lives = lives     # we set self._lives to the value we pass
        else:  # if we are passing a number less than 0 (negative number)
            print("Lives cannot be negative")
            self._lives = 0   # we give above message and set self._lives to 0



    # The last step is to define a property called lives that uses these methods when reading or writing our lives attributes
    # our original data attributes was "_lives" and we have replaced it with this property called "lives" that uses these
    # two methods to access the number of lives that the player has.

    lives = property(_get_lives, _set_lives)  # NOTE the _get_lives and _set_lives have no ()


# Now we can go to main.py file and run it and it still works using this command in line 56
# print("Dylan's New lives = {}".format(dylan.lives))


    # we will also create a method to print the output in string representation

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)



# =================================================================================
# Challenge: using property
# =================================================================================

# Modify the player class so that the player's scores are increased by one thousand
# Every time their levels are increased by one.

# So if they jump up two levels, they get a bonus of two thousand added to their score.
# If the player drops back a level, they lose one thousand for each level they drop back.

# The aim of this challenge is to use "properties", so although it may make more sense to
# add methods to increase and decrease the level, please use a property.

# ====================
# Solution
# ====================

# Because this video is about getters and setters, we will create a "property" for the level
# And then create a getter and a setter to change the score as the level changes.

# We will create a property called "level", so the first thing is to hide our "level" attribute by
# renaming it _level.

# Then we will create a getter (_get_level) and setter (_set_level) methods.

# Then lastly we will define a property and tell it to use the two methods (_get_level) and (_set_level) as getter and setter


class Player(object):

    def __init__(self, name):  # We will pass it a name in the class constructor (__init__)
        self.name = name  # this is the name we pass
        # self.lives = 3  # Player will have 3 lives initially. Use this initially without getter/setter
        self._lives = 3  # Use this with getter and setter. We hide lives attribute by prefixing it with underscore
        self._level = 1  # Player starts at level 1 (we will refactor it to become _level)
        self.score = 0  # Player start with score 0


    # Now we will put all the code that uses the Player class in a python file called main.py


    # We will now add "Getter" and "setter" in our Player class
    # first we use self._lives = 3 (this hides the lives attribute)

    # Now we will create "setter" method (to set the value) and "getter" method (to get the value)
    # NOTE we are hiding these methods by starting their names with underscore ( _get_lives and _set_lives )
    # The underscore at the beginning informs users that they should not be calling these methods

    # getter method returns self._lives

    def _get_lives(self):
        return self._lives

    # setter method is passed parameter lives, which is the number of lives you want to set to self._lives
    # This method also checks that we don't set lives to negative number
    # we will go to main.py to test if this test for negative works. Check code under "Check test for negative"

    def _set_lives(self, lives):
        if lives >= 0:              # if lives we pass it is 0 or more
            self._lives = lives     # we set self._lives to the value we pass
        else:  # if we are passing a number less than 0 (negative number)
            print("Lives cannot be negative")
            self._lives = 0   # we give above message and set self._lives to 0


    # We will create the getter for level here. called _get_level

    def _get_level(self):
        return self._level  # This will return the value of _level data attribute in line 118 above

    # We create the setter method (_set_level)
    # It has to check that the new level is greater than 0 and calculate the bonus that will be added to the score
    # NOTE that this will work both ways. e.g. if initial level is 1 and new level is 2, we add (2-1) x 1000 = 1000
    # If initial level is 2 and new level is one, we add (1-2) * 1000 = -1000 (hence we subtract 1000 from score)

    def _set_level(self, level):  # we will also pass it a parameter named level
        if level > 0:
            delta = level - self._level  # Where self._level is initially level 1
            self.score += delta * 1000  # In level = 2, delta = 2-1 = 1 hence self.score will be self.score + 1 x 1000
            self._level = level  # then we make self._level to be level = 2 in this case
        else:
            print("Level cannot be less than 1")


    # The last step is to define a property called lives that uses these methods when reading or writing our lives attributes
    # our original data attributes was "_lives" and we have replaced it with this property called "lives" that uses these
    # two methods to access the number of lives that the player has.

    lives = property(_get_lives, _set_lives)  # NOTE the _get_lives and _set_lives have no ()

    # Now we define a property and tell it to use the two methods (_get_level) and (_set_level) as getter and setter
    # This property will be called "level"

    level = property(_get_level, _set_level)   # Note don't use the () for level method names here. because it will call the method and use their values.


    # Now we can go to main.py file and run it and it still works using this command in line 56
    # print("Dylan's New lives = {}".format(dylan.lives))


    # we will also create a method to print the output in string representation

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)


# Now we will got to main.py and test the new program







# ======================================================================================
# Alternate syntax for writing property
# ======================================================================================

# NOTE that this alternate way of coding property is more common
# It uses something called "decorators" and does the same thing as we've seen above, but just the syntax differs

# to use this new property syntax, we will add a property for our "score" attribute
# First we will hide our score variable by refactor/renaming it to _score (from self.score to self._score)

# Then we add the getter and setter methods but we decorate those methods
# by putting a special comment (@property) before them.

# NOTE that we have not covered decorators yet, so take this is as an alternative syntax for now.


class Player(object):

    def __init__(self, name):  # We will pass it a name in the class constructor (__init__)
        self.name = name  # this is the name we pass
        # self.lives = 3  # Player will have 3 lives initially. Use this initially without getter/setter
        self._lives = 3  # Use this with getter and setter. We hide lives attribute by prefixing it with underscore
        self._level = 1  # Player starts at level 1 (we will refactor it to become _level)
        self._score = 0  # Player start with score 0


    # Now we will put all the code that uses the Player class in a python file called main.py


    # We will now add "Getter" and "setter" in our Player class
    # first we use self._lives = 3 (this hides the lives attribute)

    # Now we will create "setter" method (to set the value) and "getter" method (to get the value)
    # NOTE we are hiding these methods by starting their names with underscore ( _get_lives and _set_lives )
    # The underscore at the beginning informs users that they should not be calling these methods

    # getter method returns self._lives

    def _get_lives(self):
        return self._lives

    # setter method is passed parameter lives, which is the number of lives you want to set to self._lives
    # This method also checks that we don't set lives to negative number
    # we will go to main.py to test if this test for negative works. Check code under "Check test for negative"

    def _set_lives(self, lives):
        if lives >= 0:              # if lives we pass it is 0 or more
            self._lives = lives     # we set self._lives to the value we pass
        else:  # if we are passing a number less than 0 (negative number)
            print("Lives cannot be negative")
            self._lives = 0   # we give above message and set self._lives to 0


    # We will create the getter for level here. called _get_level

    def _get_level(self):
        return self._level  # This will return the value of _level data attribute in line 118 above

    # We create the setter method (_set_level)
    # It has to check that the new level is greater than 0 and calculate the bonus that will be added to the score
    # NOTE that this will work both ways. e.g. if initial level is 1 and new level is 2, we add (2-1) x 1000 = 1000
    # If initial level is 2 and new level is one, we add (1-2) * 1000 = -1000 (hence we subtract 1000 from score)

    def _set_level(self, level):  # we will also pass it a parameter named level
        if level > 0:
            delta = level - self._level  # Where self._level is initially level 1
            self._score += delta * 1000  # In level = 2, delta = 2-1 = 1 hence self.score will be self.score + 1 x 1000
            self._level = level  # then we make self._level to be level = 2 in this case
        else:
            print("Level cannot be less than 1")


    # The last step is to define a property called lives that uses these methods when reading or writing our lives attributes
    # our original data attributes was "_lives" and we have replaced it with this property called "lives" that uses these
    # two methods to access the number of lives that the player has.

    lives = property(_get_lives, _set_lives)  # NOTE the _get_lives and _set_lives have no ()

    # Now we define a property and tell it to use the two methods (_get_level) and (_set_level) as getter and setter
    # This property will be called "level"

    level = property(_get_level, _set_level)   # Note don't use the () for level method names here. because it will call the method and use their values.


    # Then we add the getter method and put a special comment (@property) before them.
    # we add the @property decorator before the method (score) and the decorator serves same purpose of
    # "score = property(_get_score)" that we would have had to write

    @property
    def score(self):
        return self._score

    # Now we add the setter method
    # The setter method is similar method that we used for the other setter.
    # The difference here is the decorator @score.setter is the name of the property (score) followed by .setter

    @score.setter
    def score(self, score):
        self._score = score  # NOTE: always type self._score (not self.score) otherwise you will get a recursive error


    # we will also create a method to print the output in string representation

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)



# ======================================================
# Link to Documentation for property built in function:
# ======================================================

# https://docs.python.org/3/library/functions.html#property



