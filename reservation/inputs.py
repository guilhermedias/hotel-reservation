
import re
from abc import ABCMeta
from abc import abstractmethod
from reservation import customer


class InputReader(object):
  """ Abstract base class for input handlers. """

  __metaclass__ = ABCMeta

  @abstractmethod
  def set_input_source(self, input_source):
    """ Set the input source for specific object. """
    pass

  @abstractmethod
  def get_next(self):
    """ Return the next CustomerRequest in the input
        source. Return None when the source is done.
    """
    pass

  @classmethod
  def valid_input(cls, input_line):
    """ Checks the integrity of an input line. """
    # Input line pattern
    pattern = re.compile(
          "\s*(\w+):(\s*\w+\(\w+\)\s*,)*(\s*\w+\(\w+\)\s*,?\s*\Z)")

    if(pattern.match(input_line)):
      return True
    else:
      return False


class TextFileReader(InputReader):
  """ Parse and process input from text files. """

  def __init__(self):
    self._source_index = 0 # Read position
    self._input_source = []

  def set_input_source(self, input_source):
    with open(input_source, 'r') as s:
      self._source_index = 0
      self._input_source = s.readlines()

  def get_next(self):
    next_request = None
    valid_input = False

    # Iterate over the input source until it finds
    # valid input line or the input source is over
    while not valid_input and self._source_index < len(self._input_source):
      input_line = self._input_source[self._source_index]
      if(TextFileReader.valid_input(input_line)):
        customer_type = input_line.split(':')[0]
        booking_dates = re.findall("\w+\(\w+\)", input_line)
        next_request = customer.CustomerRequest(customer_type, booking_dates)
        valid_input = True

      self._source_index += 1

    return next_request

