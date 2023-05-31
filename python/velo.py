from medewerker import Transporteur
from gebruiker import Gebruikers
from fietsen import Fietsen, Fiets
from station import Stations
from faker import Faker

fake = Faker()

class Velo():
    """ Een container-klasse voor alle andere klassen """
    def __init__(self):
        self.gebruikers = Gebruikers()
        self.stations = Stations()
        self.transporter = Transporteur()
        self.bikes = Fietsen()
        self.initialiseer_gebruikers()
        self.initialiseer_stations()
        self.initialiseer_bikes()
    
    def initialiseer_gebruikers(self):
        for i in range(1, 501):
          naam = fake.name()
          self.gebruikers.toevoegen(naam)
        for i in range(1, 11):
          naam = fake.name()
          self.transporter.toevoegen(naam)

    def initialiseer_stations(self):
       self.stations.extract_from_geojson('velo.geojson')
    
    def initialiseer_bikes(self):
       for i in range(1, 4001):
        self.bikes.add_bike(Fiets())  
    
    def terminal_interface_weergeven(self):
        keuze_string = "Maak een keuze:\n1: Toon Station\n2: Kies Station\n3: Neem Fiets\n4: Plaats Fiets\n5: Website Generen\n0: Data opslaan en toepassing verlaten\nJouw keuze: "
        getal = int(input(keuze_string))
        while getal != 0:
            if getal == 1: #Toon Stations
              print(self.Stations.stations())
            elif getal == 2: #Kies Station
              print(getal)
            elif getal == 3: #Neem Fiets
              getal = int(input(keuze_string))
            elif getal == 4: #Plaats Fiets
              getal = int(input(keuze_string))

            elif getal == 5: #Website Generen
              print(getal)

        getal = int(input(keuze_string)) 