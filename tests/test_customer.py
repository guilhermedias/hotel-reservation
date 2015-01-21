
import unittest
from reservation import customer
 
class TestCustomer(unittest.TestCase):

    # get_weekday_count()
    def test_weekday_count_empty(self):
        request = customer.CustomerRequest("Regular", [])
        self.assertEqual(request.get_weekday_count(), 0)

    def test_weekday_count_0(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(sat)", 
                                                       "17Mar2009(sun)"])
        self.assertEqual(request.get_weekday_count(), 0)

    def test_weekday_count_only_2(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(mon)", 
                                                       "17Mar2009(tues)"])
        self.assertEqual(request.get_weekday_count(), 2)

    def test_weekday_count_full_week(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(mon)", 
                                                       "17Mar2009(tues)",
                                                       "18Mar2009(wed)",
                                                       "19Mar2009(thur)",
                                                       "20Mar2009(fri)",
                                                       "21Mar2009(sat)",
                                                       "22Mar2009(sun)"])
        self.assertEqual(request.get_weekday_count(), 5)

    def test_weekday_count_mixed(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(sat)", 
                                                       "17Mar2009(sun)",
                                                       "18Mar2009(mon)",
                                                       "19Mar2009(tues)"])
        self.assertEqual(request.get_weekday_count(), 2)

    # get_weekend_count()
    def test_weekend_count_empty(self):
        request = customer.CustomerRequest("Regular", [])
        self.assertEqual(request.get_weekend_count(), 0)

    def test_weekend_count_0(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(mon)", 
                                                       "17Mar2009(tues)"])
        self.assertEqual(request.get_weekend_count(), 0)

    def test_weekend_count_only_2(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(sat)", 
                                                       "17Mar2009(sun)"])
        self.assertEqual(request.get_weekend_count(), 2)

    def test_weekend_count_full_week(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(mon)", 
                                                       "17Mar2009(tues)",
                                                       "18Mar2009(wed)",
                                                       "19Mar2009(thur)",
                                                       "20Mar2009(fri)",
                                                       "21Mar2009(sat)",
                                                       "22Mar2009(sun)"])
        self.assertEqual(request.get_weekend_count(), 2)

    def test_weekend_count_mixed(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(sat)", 
                                                       "17Mar2009(sun)",
                                                       "18Mar2009(mon)",
                                                       "19Mar2009(tues)"])
        self.assertEqual(request.get_weekend_count(), 2)

if __name__ == '__main__':
    unittest.main()

