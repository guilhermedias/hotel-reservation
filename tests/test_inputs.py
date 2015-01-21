
import unittest
from reservation import inputs
 
class TestCustomer(unittest.TestCase):

    # valid_input()
    def test_valid_input_empty(self):
        input_line = ""
        self.assertFalse(inputs.TextFileReader.valid_input(input_line))

    def test_valid_input_no_dates(self):
        input_line = "Regular: "
        self.assertFalse(inputs.TextFileReader.valid_input(input_line))

    def test_valid_input_incomplete_date(self):
        input_line = "Regular: 16Mar2009(mon), 17Mar2009, 18Mar2009(wed)"
        self.assertFalse(inputs.TextFileReader.valid_input(input_line))

    def test_valid_input_no_spacing(self):
        input_line = "Regular:16Mar2009(mon),17Mar2009(tues),18Mar2009(wed)"
        self.assertTrue(inputs.TextFileReader.valid_input(input_line))

    def test_valid_input_extra_spacing(self):
        input_line = "Regular: 16Mar2009(mon)  , 17Mar2009(tues),  18Mar2009(wed)"
        self.assertTrue(inputs.TextFileReader.valid_input(input_line))

    def test_valid_input_trailing_comma(self):
        input_line = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed),"
        self.assertTrue(inputs.TextFileReader.valid_input(input_line))

    def test_valid_input_trailing_spaces(self):
        input_line = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)   "
        self.assertTrue(inputs.TextFileReader.valid_input(input_line))

    def test_valid_input_leading_spaces(self):
        input_line = "   Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        self.assertTrue(inputs.TextFileReader.valid_input(input_line))

    def test_valid_input_regular(self):
        input_line = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        self.assertTrue(inputs.TextFileReader.valid_input(input_line))

if __name__ == '__main__':
    unittest.main()

