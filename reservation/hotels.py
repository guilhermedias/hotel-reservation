
from xml.etree import ElementTree

class Hotel(object):
  """ A single hotel representation. """

  def __init__(self, name, rating, price_table):
    self.name = name
    self.rating = rating
    self._price_table = price_table

  def request_cost(self, customer_request):
    weekday_price = self._price_table[customer_request.customer_type]["weekday"]
    weekend_price = self._price_table[customer_request.customer_type]["weekend"]

    return customer_request.get_weekday_count() * weekday_price + \
           customer_request.get_weekend_count() * weekend_price


class HotelChain(object):
  """ Hotel chain representation. """

  def __init__(self):
    self.hotels = []

  def load_hotels(self, config_file):
    configs = ElementTree.parse(config_file)

    for hotel in configs.getroot().findall("hotel"):
      name =  hotel.attrib["name"]
      rating =  hotel.attrib["rating"]

      price_table = dict()

      for price in hotel.findall("price"):
        customer_type = price.attrib["customer_type"]
        booking_class = price.attrib["booking_class"]

        if customer_type not in price_table:
          price_table[customer_type] = dict()

        price_table[customer_type][booking_class] = float(price.text)

      self.hotels.append(Hotel(name, rating, price_table))

  def find_cheapest_hotel(self, customer_request):
    cheapest_hotel = None
    lowest_cost = -1
    for hotel in self.hotels:
      current_cost = hotel.request_cost(customer_request)
      if(current_cost < lowest_cost or lowest_cost == -1):
        lowest_cost = current_cost
        cheapest_hotel = hotel

      if(current_cost == lowest_cost):
        if(hotel.rating > cheapest_hotel.rating):
          lowest_cost = current_cost
          cheapest_hotel = hotel

    return cheapest_hotel.name

