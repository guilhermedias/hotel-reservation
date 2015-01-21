
import sys
from reservation import inputs
from reservation import hotels

input_file = None

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " <input_file>"
  quit()
else:
  input_file = sys.argv[1]
  
hotel_chain = hotels.HotelChain()
hotel_chain.load_hotels('config.xml')

input_reader = inputs.TextFileReader()
input_reader.set_input_source(input_file)
customer_request = input_reader.get_next()

while customer_request:
  input_line = customer_request.original_input
  hotel_name = hotel_chain.find_cheapest_hotel(customer_request) 
  print "INPUT: " + input_line
  print "OUTPUT: " + hotel_name + '\n'
  customer_request = input_reader.get_next()

