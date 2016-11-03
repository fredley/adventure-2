from adventurelib import *

from map import UkMap

map = UkMap()

@when('go DIRECTION')
def go(direction):
    if map.can_go(direction):
        map.go(direction)
        print('You go %s.' % direction)

@when('look')
def look():
    print("You are currently in %s" % map.current_room)
    for direction in map.current_room.exits():
        print('To your %s, you see %s' % (
            direction,
            map.current_room.exit(direction)
        ))

@when('look DIRECTION')
def look_direction(direction):
    print(current_location)
    print(direction)
    if current_location.items:
        for i in current_location.items:
            print('A %s is here.' % i)

look()
start()
