class Hero():
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

