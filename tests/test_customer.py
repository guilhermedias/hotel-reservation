
import unittest
from reservation import customer
 
class TestCustomer(unittest.TestCase):
 
    def setUp(self):
        pass

    def tearDown(self):
        pass
 
    def test_weekday_1(self):
        request = customer.CustomerRequest("Regular", ["16Mar2009(mon)", 
                                                       "17Mar2009(tue)",
                                                       "18Mar2009(wed)"])

        self.assertEqual(request.get_weekday_count(), 3)

if __name__ == '__main__':
    unittest.main()

