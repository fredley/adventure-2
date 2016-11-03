"""

Rally openers and ripostes:

    from knowledge import rally_openers, ripostes

    # Open a ralley
    rally_opener = rally_openers[0]
    rally_opener['string']

    # Get the available ripostes
    available_ripostes = [riposte for riposte in ripostes if riposte['id'] in rally_opener['available_ripostes']]

    # Choose a riposte
    riposte = available_ripostes[0]

    # Did you vote leave?
    bool(riposte['id'] == rally_opener['successful_riposte'])

Information:

    from knowledge import information

    # Look up by index
    piece = information[0]

    # Access information via 'string' attribute.
    piece['string']

"""

map_text = {
  'scotland': {
    'arrive': "You arrive at the Canon's Gait pub on the Royal Mile, the crowd is a bit rowdy...",
    'name': "Scotland"
  },
  'wales': {
    'arrive': "You arrive in Wales feeling hungry, and feel like going out for a 'Chinese'.",
    'name': "Wales"
  },
  'west_country': {
    'arrive': "Arriving in the West Country by plane, you need a pint after a bumpy landing.",
    'name': "West Country"
  },
  'the_north': {
    'arrive': "You arrive in Manchester to a warm welcome by Morrisey",
    'name': "The North"
  },
  'london': {
    'arrive': "You arrive in London, taking your large security entourage around with you, just in case.",
    'name': "London"
  }
}

information = [
    {'string': "After looking around for a few moments, you spot a pub on the nearest corner. Without hestiation, you cancel your next appointment and head straight in."},
    {'string': "On your way to your next appointment, you receive a wonderful phone call from a republican across the pond. You wonder why a man who talks so much sense can receive so much flak..."},
    {'string': 'Something about this place feels strangely familiar. It would look great from the skies...'},
]

# Store the possible ripostes in the available_ripostes attribute.
# Store the ID of the "vote leave" riposte in the successful_riposte attribute.
rally_openers = [
    {'string': 'What do you think about...?', 'successful_riposte': 0, 'available_ripostes': [0, 1]},
]

ripostes = [
    {'string': 'Vote leave!', 'id': 0},
    {'string': 'Vote remain!', 'id': 1}
]
