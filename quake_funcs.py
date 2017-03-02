from urllib.request import urlopen
from json import loads
from datetime import datetime


# GIVEN FUNCTIONS: Use these two as-is and do not change them
def get_json(url):
   """Function to get a JSON dictionary from a website.

   Args:
      url (str): The url from which to get the JSON

   Returns:
      A Python dictionary containing the information from the JSON object
   """
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)


def time_to_str(time):
   """Converts integer seconds since unix epoch to a string.

   Args:
      time (int): Unix time

   Returns:
      A nicely formated time string
   """
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')



class Earthquake:
   """ A class to model and earthquake.

   Attributes:
      place (str): The place the earthquake happened.
      mag (float): The magnitude of the earthquake.
      longitude (float): The longitude of the earthquake.
      latitude (float): The latitude of the earthquake.
      time (int): The time the earthquake took place.
   """

   def __init__(self, place, mag, longitude, latitude, time):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time

   def __eq__(self, other):
      return self.place == other.place and self.mag == other.mag and self.longitude == other.longitude and self.latitude == other.latitude and self.time == other.time



# TODO: Required function - implement me!
def read_quakes_from_file(filename):
   my_file = open(filename, 'r')
   list_of_quakes = []
   for line in my_file:
      string = line.split()
      place = " ".join(string[4:])
      q = Earthquake(place, float(string[0]),float(string[1]), float(string[2]), int(string[3]))
      list_of_quakes.append(q)
   return list_of_quakes





# TODO: Required function - implement me!
def filter_by_mag(quakes, low, high):
   pass


# TODO: Required function - implement me!
def filter_by_place(quakes, word):
   pass


# TODO: Required function for final part - implement me too!
def quake_from_feature(feature):
   pass
