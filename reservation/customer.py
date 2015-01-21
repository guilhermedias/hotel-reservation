
class CustomerRequest(object):
  """ Customer's request data. """

  def __init__(self, customer_type, request_dates, original_input):
    self.customer_type = customer_type

    self._request_dates = request_dates
    self._weekday_count = 0
    self._weekend_count = 0

    self._update_days_count()

    self.original_input = original_input


  def get_request_dates(self):
    return self._request_dates

  def set_request_dates(self, request_dates):
    self._request_dates = request_dates
    self._update_days_count()

  def get_weekday_count(self):
    return self._weekday_count

  def get_weekend_count(self):
    return self._weekend_count


  # Protected methods

  def _update_days_count(self):
    self._weekday_count = 0
    self._weekend_count = 0

    for date in self._request_dates:
      if "sat" in date or "sun" in date:
        self._weekend_count += 1
      else:
        self._weekday_count += 1

