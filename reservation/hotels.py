
class Hotel:
  """ A single hotel representation. """

  def __init__(self, name,
                      weekday_regular, weekday_rewards,
                      weekend_regular, weekend_rewards, rating):
    self.name = name
    self.weekday_regular = float(weekday_regular)
    self.weekday_rewards = float(weekday_rewards)
    self.weekend_regular = float(weekend_regular)
    self.weekend_rewards = float(weekend_rewards)
    self.rating = float(rating)


  def request_cost(self, customer_request):
    total_cost = 0
    if(customer_request.is_rewards()):
      total_cost = customer_request.get_weekday_count() * self.weekday_rewards + \
                   customer_request.get_weekend_count() * self.weekend_rewards
    else:
      total_cost = customer_request.get_weekday_count() * self.weekday_regular + \
                   customer_request.get_weekend_count() * self.weekend_regular

    return total_cost


class HotelChain:
  """ Hotel chain representation. """

  def __init__(self):
    self.hotels = []

  def load_hotels(self, hotels_file):
    """Load hotels information from the given CSV file"""
    # Parses the CSV file and creates the Hotel objects
    with open(hotels_file, 'r') as h_file:
      for line in h_file:
        h_values = line.split(',')
        hotel = Hotel(h_values[0], # Hotel name
                      h_values[1], h_values[2], # Weekday rates for regular and rewards customers
                      h_values[3], h_values[4], # Weekend rates for regular and rewards customers
                      h_values[5]) # Hotel rating

        self.hotels.append(hotel)

  def find_cheapest(self, customer_request):
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

