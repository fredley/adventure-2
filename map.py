from adventurelib import *
from knowledge import map_text

class Map():

  def can_go(self, direction):
    return self.current_room.exit(direction)

  def go(self, direction):
    self.set_location(self.current_room.exit(direction))
    print(self.descriptions[self.current_room_name])

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

    self.descriptions = {
      'scotland': map_text['scotland']['arrive'],
      'wales': map_text['wales']['arrive'],
      'west_country': map_text['west_country']['arrive'],
      'the_north': map_text['the_north']['arrive'],
      'london': map_text['london']['arrive']
    }

    self.rooms['london'].west = self.rooms['west_country']
    self.rooms['london'].north = self.rooms['the_north']

    self.rooms['west_country'].west = self.rooms['wales']
    self.rooms['west_country'].east = self.rooms['london']

    self.rooms['wales'].east = self.rooms['west_country']

    self.rooms['the_north'].north = self.rooms['scotland']
    self.rooms['the_north'].south = self.rooms['london']

    self.rooms['scotland'].south = self.rooms['the_north']

    self.set_location('london')
