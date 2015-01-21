import sys
from character import Character
from monster import Goblin, Troll, Ogre, Giant, Dragon

class Game:
  def setup(self):
    print("________________________ _______    _______ _______    _       _______ _______ _______ _       ______  _______ ")
    print("\\__   __\\__   __(       (  ____ \\  (  ___  (  ____ \\  ( \\     (  ____ (  ____ (  ____ ( (    /(  __  \\(  ____ \\")
    print("   ) (     ) (  | () () | (    \/  | (   ) | (    \/  | (     | (    \| (    \| (    \|  \  ( | (  \  | (    \/")
    print("   | |     | |  | || || | (__      | |   | | (__      | |     | (__   | |     | (__   |   \ | | |   ) | (_____ ")
    print("   | |     | |  | |(_)| |  __)     | |   | |  __)     | |     |  __)  | | ____|  __)  | (\ \) | |   | (_____  )")
    print("   | |     | |  | |   | | (        | |   | | (        | |     | (     | | \_  | (     | | \   | |   ) |     ) |")
    print("   | |  ___) (__| )   ( | (____/\  | (___) | )        | (____/| (____/| (___) | (____/| )  \  | (__/  /\____) |")
    print("   )_(  \_______|/     \(_______/  (_______|/         (_______(_______(_______(_______|/    )_(______/\_______)")
    print("                                                                                                               ")
    self.player = Character()
    print('\n' + '#' * 60)
    print("Instructions:")
    print("(1) Fight the monsters!")
    print("(2) Attempting to dodge attacks uses 1 stamina.")
    print("(3) Resting replenishes random HP and 1 Sta.")
    print('#' * 60)
    self.monsters = [
      Goblin(),
      Troll(),
      Ogre(),
      Giant(),
      Dragon()
    ]
    self.monster = self.get_next_monster()
    
  def get_next_monster(self):
    try:
      return self.monsters.pop(0)
    except IndexError:
      return None
    
  def monster_turn(self):
    # check to see if the monster attacks
    # if so, tell the player
    #    Check, if the player wants to dodge
    #    If so, see if dodge is successful
    #      If it is move on
    #    If not, remove one player hit point
    # If the monster isn't attacking, tell that to the player too.
    if self.monster.attack():
      print("{} is attacking!".format(self.monster))
      if self.player.stamina > 0:
        if input("Dodge Y/N? ").lower() == 'y':
          self.player.stamina -= 1
          if self.player.dodge():
            print("You dodged the attack!")
          else:
            print("You got hit anyway!")
            self.player.hit_points -= 1
        else:
          print("{} hit you for 1 point!".format(self.monster))
          self.player.hit_points -= 1
      else:
        print("{} hit you for 1 point!".format(self.monster))
        self.player.hit_points -= 1
    else:
      print("{} isn't attacking this turn.".format(self.monster))

  def player_turn(self):
    # let the player attack, rest, or quit
    # if they attack:
      # see if the attack is successful
        # if so, see if the monster dodges
          # if dodge, print that
          # if not dodged, subtract right num of hit points
        # if not good attack, tell player
    # if they rest:
      # call the player rest method
    # if they quit, exit the game
    # if they pick anything else rerun this method
    player_choice = input("[A]ttack, [R]est, [Q]uit? ").lower()
    if player_choice == 'a':
      print("You're attacking {}!".format(self.monster))
      if self.player.attack():
        if self.monster.dodge():
          print("{} dodged your attack!".format(self.monster))
        else:
          if self.player.leveled_up():
            self.monster.hit_points -= 2
          else:
            self.monster.hit_points -= 1
          print("You hit {} with your {}!".format(self.monster, self.player.weapon))
      else:
        print("You missed!")
    elif player_choice == 'r':
      self.player.rest()
    elif player_choice == 'q':
      sys.exit()
    else:
      self.player_turn()

  
  def cleanup(self):
    # if the monster has no more hit points:
      # up the player's experience
      # print a message
      # Get a new monster
    if self.monster.hit_points <= 0:
      self.player.experience += self.monster.experience
      print("You killed {}!".format(self.monster))
      print("{} experience gained.".format(self.monster.experience))
      self.monster = self.get_next_monster()
      
  def __init__(self):
    self.setup()
    
    while self.player.hit_points and (self.monster or self.monsters):
      print('\n' + '=' * 60)
      print(self.player)
      print('-' * 60)
      self.monster_turn()
      print('-' * 60)
      self.player_turn()
      self.cleanup()
      
    if self.player.hit_points:
      print("You win!")
    elif self.monsters or self.monster:
      print("You lose!")
    sys.exit()
    
Game()