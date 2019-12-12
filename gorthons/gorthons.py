from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene it not yet configured.")
        print("Subclass it and emplement enter().")

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()

class Death(Scene):

    quips = [
            "You died.  You kinda suck at this.",
            "Your mom would be proud... if she were smarter.",
            "Such a luser",
            "I have a small puppy that's better than this.",
            "You're worse than your Dad's jokes.",
        ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCooridor(Scene):
    def enter(self):
        print((dedent("""
        The Gorthons of Planet Percal #25 have invaded your ship and
        destroyed your entire crew.  You are the last surviving member
        and your last mission is to get to the neutron destruct bomb
        and blow the ship up after getting into an excape pod.

        You are running down the central coordidor to the Weapons
        Armory when a Gothon jumps out, red, scaly skin, dark grimy
        teeth, and evil clown costume flowing around his hate filled
        body. He's blocking the door the Armory and about to pull
        a weapon to blast you.
        """)))

        action = input("> ")

        if action == "shoot!":

            print((dedent("""
            Quick on the draw you yank out your blaster and fire it at the Gothon.
            His clown costume is flowing and moving around his body, which throws
            off your aim. Your lazer hits his costume, but misses him entirely.
            This completely ruins his brand new costume his mother bought him, which
            makes him fly into an insane rage and blast you repeatedly in the face
            until you are dead.  Then he eats you.
            """)))
            return 'death'

        elif action == "dodge":
            print((dedent("""
            Like a world class boxer you dodge, weave, slip and slide ride as the
            Gothon's blaster cranks a laster past your head.  In the middle of your
            artful dodge your foot slips and you bang your head on the metal wall and
            pass out.  You wake up shortly only after to die as the Gothon stomps on
            your head and eats you.
            """)))
            return 'death'

        elif action == 'tell a joke':
            print((dedent("""
            Lucky for you, they made you learn Gothon insults in the academy.
            You tell the one Gothon joke you know: 
            Tefed hi kobab zi nkop trulu. Zig montol kepkoi zi nkop. Tefedi
            jopjan zi nkop trili sojo sojo.  
            The Gothon stops, tries to not laugh, then bursts our laughing and
            can't move.  While he's laughing you run up and shoot him square
            in the head putting him down, and jump though the Weapon Armory door.
            """)))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_cooridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):
    
    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_cooridor')
a_game = Engine(a_map)
a_game.play()