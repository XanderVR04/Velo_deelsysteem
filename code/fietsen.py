class Fiets:
  bike_count = 0
  
  def __init__(self, log=None):
    self.bike_count += 1
    self.id = Fiets.bike_count
    self.log = log

  def __str__(self):
    return f"{self.id} : {self.log}"


class Fietsen:

  def __init__(self):
    self.storage = {}
    self.index = 1

  def add_bike(self):
    self.index += 1
    self.storage.update({Fiets.id: Fiets()})


