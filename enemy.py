
# =================================
# superclasss enemy.py
# =================================

# This superclass enemy has the defined properties
# and any enemy object that is created from this superclass will have the same properties
# This enemy class will be called in the main.py class

class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        return("Name: {0.name}, Hit Points: {0.hit_points}, Lives: {0.lives}".format(self))