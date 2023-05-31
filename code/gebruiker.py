class Gebruiker():
    def __init__(self, name):
        self.name = name
        self.max_bikes = 1
        self.can_take_multiple_bikes = False
        self.bikes = []

    def add_bike(self, bike):
        self.bikes.append(bike)

    def remove_bike(self, bike_id):
        for bike in self.bikes:
            if bike.id == bike_id:
                self.bikes.remove(bike)
                break


class Gebruikers():
    def __init__(self):
        self.lijst = []
        self.index = 1 # start ID

    def toevoegen(self, naam):
        nieuwe_gebruiker = Gebruiker(naam)
        self.lijst.append(nieuwe_gebruiker) # toevoegen
        self.index += 1	# ga naar volgende ID
