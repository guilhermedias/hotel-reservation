from reservation import inputs
from reservation import hotels

hotel_chain = hotels.HotelChain()
hotel_chain.load_hotels('hotels.csv')

input_parser = inputs.TextFileReader()
input_parser.set_input_source('inputs.txt')
input_object = input_parser.get_next()

while(input_object):
  print hotel_chain.find_cheapest(input_object)
  input_object = input_parser.get_next()

