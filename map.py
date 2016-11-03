from adventurelib import *
from knowledge import map_text

class Map():

  def can_go(self, direction):
    return self.current_room.exit(direction)

  def go(self, direction):
    self.current_room = self.current_room.exit(direction)
    print(self.current_room.arrive_text)

  def set_location(self, room):
    self.current_room = self.rooms[room]

  def get_location(self):
    return self.current_room


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
    self.rooms['london'].arrive_text = map_text['london']['arrive']

    self.rooms['west_country'].west = self.rooms['wales']
    self.rooms['west_country'].east = self.rooms['london']
    self.rooms['west_country'].arrive_text = map_text['west_country']['arrive']

    self.rooms['wales'].east = self.rooms['west_country']
    self.rooms['wales'].arrive_text = map_text['wales']['arrive']

    self.rooms['the_north'].north = self.rooms['scotland']
    self.rooms['the_north'].south = self.rooms['london']
    self.rooms['the_north'].arrive_text = map_text['the_north']['arrive']

    self.rooms['scotland'].south = self.rooms['the_north']
    self.rooms['scotland'].arrive_text = map_text['scotland']['arrive']

    self.set_location('london')
