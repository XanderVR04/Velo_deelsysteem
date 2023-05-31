from slot import Slot
import json

class Station:
    def __init__(self, naam, straatnaam):
        self.Naam = naam
        self.Straatnaam = straatnaam
        self.empty_list = []



class Stations:
    def __init__(self):
        self.stations = []

  
    @staticmethod
    def extract_from_geojson(file_path):
      stations = []
      with open(file_path) as file:
            data = json.load(file)
            for feature in data['features']:
                naam = feature['properties']['Naam']
                straatnaam = feature['properties']['Straatnaam']
                aantal_plaatsen = feature['properties']['Aantal_plaatsen']

                slots = [Slot() for _ in range(aantal_plaatsen)]

                slots_data = {slot.id: slot.value for slot in slots}
          
                station = Station(naam, straatnaam)
                station.empty_list = slots_data

                stations.append(station)
            return Stations