class Hero(object):
    """Class of Hero creation"""
    def __init__(self, name, level, race):
        """Initiate hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all parameters of hero"""
        description = self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(self.health)
        print(description)

    def levelup(self):
        """Upgrade hero level"""
        self.level += 1

    def move(self):
        """Start hero moving"""
        print("Hero "+ self.name + " start moving")

    def set_health(self, new_health):
        self.health = new_health
#-------------------New class-----------------------
class SuperHero(Hero):
    """Class of SuperHero"""

    def __init__(self, name, level, race, magiclevel):
        """Initiate superpower"""
        super(SuperHero, self).__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        """Use magic"""
        self.magic -= 10

    def show_hero(self):
        """Print all parameters of hero"""
        description = self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(
            self.health) + " Magic is " + str(self.magic)
        print(description)
