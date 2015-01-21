import random
from combat import Combat

COLORS = ['blue', 'yellow', 'green', 'red', 'orange', 'purple']


class Monster(Combat):
  min_hit_points = 1
  max_hit_points = 1
  min_experience = 1
  max_experience = 1
  description = 'A default monster.'
  
  def __init__(self, **kwargs):
    self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
    self.experience = random.randint(self.min_experience, self.max_experience)
    self.color = random.choice(COLORS)
    
    for key, value in kwargs.items():
      setattr(self, key, value)
      
    #self.hit_points = kwargs.get('hit_points', 1)
    
  def __str__(self):
    return '{} {} | HP: {}, XP: {} |'.format(self.color.title(),
                                          self.__class__.__name__,
                                          self.hit_points,
                                          self.experience)

  def battlecry(self):
    return self.sound.upper()
  
class Goblin(Monster): #subclass of Monster
  max_hit_points = 3
  max_experience = 1
  sound = 'squeak'

class Troll(Monster): #subclass of Monster
  max_hit_points = 5
  max_experience = 3
  sound = 'gargle'

class Ogre(Monster): #subclass of Monster
  min_hit_points = 3
  max_hit_points = 7
  max_experience = 5
  sound = 'gargle'

class Giant(Monster): #subclass of Monster
  min_hit_points = 5
  max_hit_points = 10
  max_experience = 7
  sound = 'gargle'

class Dragon(Monster): #subclass of Monster
  min_hit_points = 7
  max_hit_points = 15
  max_experience = 10
  sound = 'gargle'