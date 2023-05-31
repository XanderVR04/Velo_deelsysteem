class Transport():
  def __init__(self, name):
    self.name = name
    self.max_bikes = 20
    self.can_take_multiple_bikes = True
    self.bikes = []


class Transporteur():

  def __init__(self):
    self.lijst = []
    self.index = 1  # start ID

  def toevoegen(self,naam):
    nieuwe_gebruiker = Transport(naam)
    self.lijst.append(nieuwe_gebruiker)  # toevoegen
    self.index += 1  # ga naar volgende ID
