# Project 5 - Earthquakes
#
# Name: Taylor Morris
# Instructor: Brian Jones
# Section: 17


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

   def __str__(self):
      return ("Place: {:s} Mag: {:2.f} Longitude: {:3.f} Latitude: {:3.f} Time: {:d}".format(self.place, self.mag, self.longitude, self.latitude, self.time)) 




def read_quakes_from_file(filename):
   my_file = open(filename, 'r')
   list_of_quakes = []

   for line in my_file:
      string = line.split()
      place = " ".join(string[4:])
      q = Earthquake(place, float(string[0]),float(string[1]), float(string[2]), int(string[3]))
      list_of_quakes.append(q)

   return list_of_quakes




def filter_by_mag(quakes, low, high):
   filtered = []
   for quake in quakes:
      if low <= quake.mag <= high:
         filtered.append(quake)
   return filtered

#print(filter_by_mag([Earthquake("CA", 3.0, 12, 3, 12), Earthquake("Az", 5.0, 2, 4, 20)], 1, 4))


# TODO: Required function - implement me!
def char_upper(char):
   if char.islower():
      return chr(ord(char) - 32)
   else:
      return char

def string_upper(string):
   return "".join([char_upper(c) for c in string])

def filter_by_place(quakes, word):
   filtered = []
   for quake in quakes:
      if string_upper(word) in string_upper(quake.place):
         filtered.append(quake)
   return filtered


# TODO: Required function for final part - implement me too!
def quake_from_feature(feature):
   pass
