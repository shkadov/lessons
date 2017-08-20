from hero import *

myhero1 = Hero("Vurdalak", 5, "ork")
myhero2 = Hero("Al", 4, "human")

myhero1.show_hero()
myhero2.move()
myhero1.levelup()
myhero1.show_hero()
myhero1.set_health(60)
myhero2.set_health(70)

myhero1.show_hero()
myhero2.show_hero()

mySuperHero = SuperHero("Moisey", 10, "human", 5)
mySuperHero.show_hero()