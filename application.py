
from reservation import inputs
from reservation import hotels

hotel_chain = hotels.HotelChain()
hotel_chain.load_hotels('config.xml')

input_reader = inputs.TextFileReader()
input_reader.set_input_source('inputs.txt')
customer_request = input_reader.get_next()

while(customer_request):
  print hotel_chain.find_cheapest(customer_request)
  customer_request = input_reader.get_next()

