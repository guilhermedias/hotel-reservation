
from reservation import inputs
from reservation import hotels

hotel_chain = hotels.HotelChain()
hotel_chain.load_hotels('config.xml')

input_reader = inputs.TextFileReader()
input_reader.set_input_source('inputs.txt')
customer_request = input_reader.get_next()

while(customer_request):
  input_line = customer_request.original_input
  hotel_name = hotel_chain.find_cheapest_hotel(customer_request) 
  print "INPUT: " + input_line
  print "OUTPUT: " + hotel_name + '\n'
  customer_request = input_reader.get_next()

