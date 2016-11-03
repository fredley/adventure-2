from adventurelib import *
from knowledge import map_text

class Map():

  def can_go(self, direction):
    return current_room.exit(direction)

  def go(self, direction):
    self.current_room = self.current_room.exit(direction)
    print(self.current_room)

  def set_location(self, room_name):
    self.current_room_name = room_name
    self.current_room = self.rooms[room_name]

  def get_location(self):
    return self.current_room

  def get_location_name(self):
    return self.current_room_name


class UkMap(Map):

  def __init__(self, room='london'):

    self.rooms = {
      'scotland': Room(map_text['scotland']['name']),
      'wales': Room(map_text['wales']['name']),
      'west_country': Room(map_text['west_country']['name']),
      'the_north': Room(map_text['the_north']['name']),
      'london': Room(map_text['london']['name'])
    }

    self.rooms['london'].west = self.rooms['west_country']
    self.rooms['london'].north = self.rooms['the_north']
    self.rooms['london'].description = map_text['london']['description']

    self.rooms['west_country'].west = self.rooms['wales']
    self.rooms['west_country'].east = self.rooms['london']
    self.rooms['west_country'].description = map_text['west_country']['description']

    self.rooms['wales'].east = self.rooms['west_country']

    self.rooms['the_north'].north = self.rooms['scotland']
    self.rooms['the_north'].south = self.rooms['london']
    self.rooms['the_north'].description = map_text['the_north']['description']

    self.rooms['scotland'].south = self.rooms['the_north']
    self.rooms['scotland'].description = map_text['scotland']['description']

    self.current_room = self.rooms['london']