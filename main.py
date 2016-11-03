from adventurelib import *

from map import UkMap

map = UkMap()

@when('go DIRECTION')
def go(direction):
    if map.can_go(direction):
        print('You go %s.' % direction)
        map.go(direction)
    else:
        print("You can't go any further %s." % direction)

@when('look around')
def look_around():
    print("You are currently in %s" % map.current_room)
    for direction in map.current_room.exits():
        print('To your %s, you see %s' % (
            direction,
            map.current_room.exit(direction)
        ))

@when('look DIRECTION')
def look_direction(direction):
    if map.can_go(direction):
        if str(direction) == 'south' and str(map.current_room) == 'Scotland':
            print('You look %s, and see, confusingly, %s' % (
                direction,
                map.current_room.exit(direction),
            ))
        else:
            print('You look %s, and see, confusingly, %s' % (
                direction,
                map.current_room.exit(direction),
            ))
    else:
        print('You look %s, and see nothing you like the look of.' % direction)

@when('exit')
def exit():
    global running
    running = False
    raise EOFError


@when('zero')
def increase():
    score.value += 1
    print("That's the spirit")
    look_around()

@when('one')
def decrease():
    score.value -= 1
    print('BADDDD CHOICE')
    look_around()


score = Item(name='score')
score.value = 0


@when('talk')
def talk():
    print('You are talking to {}'.format(map.current_room.person['name']))
    print('{}'.format(map.current_room.person['rally_opener']['string']))
    print('What do you say?')
    print('0: {}'.format(map.current_room.person['ripostes'][0]))
    print('1: {}'.format(map.current_room.person['ripostes'][1]))
    #print('successful_riposte: {}'.format(map.current_room.person['successful_riposte']))

look_around()

running = True
while running:
    try:
        start()
    except Exception as e:
        print("Uhhh %s" % e)
        pass
