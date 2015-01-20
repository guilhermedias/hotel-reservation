class CustomerRequest:
  """A customer's request data"""
  def __init__(self, customer_type, dates):
    self.customer_type = customer_type
    self.dates = dates

  def is_rewards(self):
    if(self.customer_type == "Rewards"):
      return True
    else:
      return False


