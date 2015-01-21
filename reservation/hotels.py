
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
    """ Load hotels information from configuration XML file. """

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

    """ Find the most affordable choice in the hotel chain. """
    cheapest_hotel = None

    for hotel in self.hotels:
      cheapest_hotel = HotelChain.compare_hotels(cheapest_hotel, hotel, customer_request)

    return cheapest_hotel.name

  @classmethod
  def compare_hotels(cls, hotel_a, hotel_b, customer_request):
    if hotel_a == None:
      return hotel_b

    if hotel_b == None:
      return hotel_a

    cost_a = hotel_a.request_cost(customer_request)
    cost_b = hotel_b.request_cost(customer_request)

    selected_hotel = None

    if cost_a < cost_b:
      selected_hotel = hotel_a
    elif cost_b < cost_a:
      selected_hotel = hotel_b
    elif hotel_a.rating > hotel_b.rating:
      selected_hotel = hotel_a
    else:
      selected_hotel = hotel_b

    return selected_hotel

