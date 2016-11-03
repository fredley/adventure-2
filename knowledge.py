"""

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
