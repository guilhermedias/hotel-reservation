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


class TextFileReader(InputReader):
  """ Parse and process input from text files. """

  def __init__(self):
    self.source_index = -1 # Read position
    self.input_source = []

  def set_input_source(self, input_source):
    with open(input_source, 'r') as s:
      self.source_index = -1
      self.input_source = s.readlines()

  def get_next(self):
    while True:
      self.source_index += 1
      if(self.source_index >= len(self.input_source)):
        # End of input source, return None
        return None
      else:
        try:
          # Instatiate CustomerRequest
          line = self.input_source[self.source_index]
          line = ''.join(line.split())
          split_line = line.split(':')
          customer_type = split_line[0]
          dates = split_line[1].split(',')
          return customer.CustomerRequest(customer_type, dates)

        except:
          # Malformed input line -> skip to the next iteration
          pass

