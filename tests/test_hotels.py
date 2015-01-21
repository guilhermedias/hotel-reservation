
import unittest
from reservation import hotels
from reservation import customer
 
class TestHotels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
      price_table_a= {"Regular" : {"weekday" : 90, "weekend" : 60},
                      "Rewards" : {"weekday" : 75, "weekend" : 55},
                      "Special" : {"weekday" : 55, "weekend" : 35}}

      cls._hotel_a = hotels.Hotel("Overlook", 4, price_table_a)

      price_table_b= {"Regular" : {"weekday" : 100, "weekend" : 80},
                      "Rewards" : {"weekday" : 65, "weekend" : 45},
                      "Special" : {"weekday" : 45, "weekend" : 40}}

      cls._hotel_b = hotels.Hotel("California", 5, price_table_b)

      cls._hotel_chain = hotels.HotelChain()
      cls._hotel_chain.add_hotel(cls._hotel_a)
      cls._hotel_chain.add_hotel(cls._hotel_b)

      
    # request_cost()
    def test_request_cost_empty(self):
        request = customer.CustomerRequest("Regular", [], "")
        self.assertEqual(self._hotel_a.request_cost(request), 0)

    def test_request_cost_regular_weekday_2(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(mon)", 
                                                       "17Mar2009(tues)"], "")
        self.assertEqual(self._hotel_a.request_cost(request), 180)

    def test_request_cost_special_weekday_2(self):
        request = customer.CustomerRequest("Special", ["16Mar2009(mon)", 
                                                       "17Mar2009(tues)"], "")
        self.assertEqual(self._hotel_a.request_cost(request), 110)

    def test_request_cost_regular_weekend_2(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(sat)", 
                                                       "17Mar2009(sun)"], "")
        self.assertEqual(self._hotel_a.request_cost(request), 120)

    def test_request_cost_special_weekend_2(self):
        request = customer.CustomerRequest("Special", ["16Mar2009(sat)", 
                                                       "17Mar2009(sun)"], "")
        self.assertEqual(self._hotel_a.request_cost(request), 70)

    def test_request_cost_regular_mixed(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(sat)", 
                                                       "17Mar2009(sun)",
                                                       "18Mar2009(mon)",
                                                       "19Mar2009(tues)"], "")
        self.assertEqual(self._hotel_a.request_cost(request), 300)

    def test_request_cost_special_mixed(self):
        request = customer.CustomerRequest("Special", ["16Mar2009(sat)", 
                                                       "17Mar2009(sun)",
                                                       "18Mar2009(mon)",
                                                       "19Mar2009(tues)"], "")
        self.assertEqual(self._hotel_a.request_cost(request), 180)

    # compare_hotels()
    def test_compare_hotels_none_a_none_b(self):
        request = customer.CustomerRequest("Regular", [], "")
        self.assertIsNone(hotels.HotelChain.compare_hotels(None, None, request))

    def test_compare_hotels_a_none_b(self):
        request = customer.CustomerRequest("Regular", [], "")
        self.assertEqual(hotels.HotelChain.compare_hotels(
                                  self._hotel_a, None, request), self._hotel_a)

    def test_compare_hotels_none_a_b(self):
        request = customer.CustomerRequest("Regular", [], "")
        self.assertEqual(hotels.HotelChain.compare_hotels(
                                  None, self._hotel_b, request), self._hotel_b)

    def test_compare_hotels_draw(self):
        request = customer.CustomerRequest("Regular", [], "")
        self.assertEqual(hotels.HotelChain.compare_hotels(
                          self._hotel_a, self._hotel_b, request), self._hotel_b)

    def test_compare_hotels_regular(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(fri)", 
                                                       "17Mar2009(sat)",
                                                       "18Mar2009(sun)"], "")
        self.assertEqual(hotels.HotelChain.compare_hotels(
                          self._hotel_a, self._hotel_b, request), self._hotel_a)

    def test_compare_hotels_rewards(self):
        request = customer.CustomerRequest("Rewards", ["16Mar2009(fri)", 
                                                       "17Mar2009(sat)",
                                                       "18Mar2009(sun)"], "")
        self.assertEqual(hotels.HotelChain.compare_hotels(
                          self._hotel_a, self._hotel_b, request), self._hotel_b)

    def test_compare_hotels_special(self):
        request = customer.CustomerRequest("Special", ["16Mar2009(fri)", 
                                                       "17Mar2009(sat)",
                                                       "18Mar2009(sun)"], "")
        self.assertEqual(hotels.HotelChain.compare_hotels(
                          self._hotel_a, self._hotel_b, request), self._hotel_b)

    # find_cheapest_hotel()
    def test_find_cheapest_hotel_empty(self):
        request = customer.CustomerRequest("Regular", [], "")
        self.assertEqual(self._hotel_chain.find_cheapest_hotel(request), self._hotel_b.name)

    def test_find_cheapest_hotel_regular(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(fri)", 
                                                       "17Mar2009(sat)",
                                                       "18Mar2009(sun)"], "")
        self.assertEqual(self._hotel_chain.find_cheapest_hotel(request), self._hotel_a.name)

    def test_find_cheapest_hotel_rewards(self):
        request = customer.CustomerRequest("Rewards", ["16Mar2009(fri)", 
                                                       "17Mar2009(sat)",
                                                       "18Mar2009(sun)"], "")
        self.assertEqual(self._hotel_chain.find_cheapest_hotel(request), self._hotel_b.name)

    def test_find_cheapest_hotel_special(self):
        request = customer.CustomerRequest("Special", ["16Mar2009(fri)", 
                                                       "17Mar2009(sat)",
                                                       "18Mar2009(sun)"], "")
        self.assertEqual(self._hotel_chain.find_cheapest_hotel(request), self._hotel_b.name)

    def test_find_cheapest_hotel_exception(self):
        request = customer.CustomerRequest("Undefined", ["16Mar2009(fri)"], "")
        with self.assertRaises(KeyError):
          self._hotel_chain.find_cheapest_hotel(request)

if __name__ == '__main__':
    unittest.main()

