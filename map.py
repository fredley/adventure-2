from adventurelib import *

class Map():

  def can_go(self, direction):
    return current_room.exit(direction)

  def go(self, direction):
    self.current_room = self.current_room.exit(direction)

  def set_location(self, room_name):
    self.current_room = room

  def get_location(self):
    return self.current_room

class UkMap(Map):

  def __init__(self, room='london'):

    self.rooms = {
      'scotland': Room(scotland_text),
      'wales': Room(wales_text),
      'west_country': Room(west_text),
      'the_north': Room(north_text),
      'london': Room(london_text)
    }

    self.rooms['london'].west = self.rooms['west_country']
    self.rooms['london'].north = self.rooms['the_north']

    self.rooms['west_country'].west = self.rooms['wales']
    self.rooms['west_country'].east = self.rooms['london']

    self.rooms['the_north'].north = self.rooms['scotland']
    self.rooms['the_north'].south = self.rooms['london']

    self.rooms['scotland'].south = self.rooms['the_north']

    self.current_room = self.rooms['london']