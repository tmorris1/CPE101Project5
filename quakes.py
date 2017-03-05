# Project 5 - Earthquakes
#
# Name: Taylor Morris
# Instructor: Brian Jones
# Section 17

from quake_funcs import *
from operator import attrgetter


def printing(quakes):
   print("Earthquakes:\n------------")

   for quake in quakes:
      print("({:.2f}) {:>40} {:s} at ({:8.3f}, {:8.3f})".format(quake.mag, quake.place, 
                                 time_to_str(quake.time), quake.longitude, quake.latitude))
   print()

def write_to_file(quakes, quakes_file):
   out_file = open(quakes_file, 'w')
   for quake in quakes:
      out_file.write("{:f} {:f} {:f} {:d} {:s}\n".format(quake.mag, quake.longitude, quake.latitude, quake.time, quake.place))

   

def  main():
   option = ""
   quakes = read_quakes_from_file("quakes.txt")
   printing(quakes)


   while option != "q" and option != "Q":
      option = input("Options:\n  (s)ort\n  (f)ilter\n  (n)ew quakes\n  (q)uit\n\nChoice: ")

      if option == "s" or option == "S":
         sort_by = input("Sort by (m)agnitude, (t)ime, (l)ongtide, or l(a)titude? ")

         if sort_by == "m" or sort_by == "M":
            quakes.sort(key=attrgetter('mag'), reverse=True)
            print()
            printing(quakes) 
         elif sort_by == "t" or sort_by == "T":
            quakes.sort(key=attrgetter("time"), reverse=True)
            print()
            printing(quakes)
         elif sort_by == "l" or sort_by == "L":
            quakes.sort(key=attrgetter("longitude"))
            print()
            printing(quakes)
         elif sort_by == "a" or sort_by == "A":
            quakes.sort(key=attrgetter("latitude"))
            print()
            printing(quakes)

      elif option == "f" or option == "F":
         filter_by = input("Filter by (m)agnitude or (p)lace? ")

         if filter_by == "m" or filter_by == "M":
            lower = float(input("Lower bound: "))
            upper = float(input("Upper bound: "))
            filtered = filter_by_mag(quakes, lower, upper)
            print()
            printing(filtered)

         elif filter_by == "p" or filter_by == "P":
            string = input("Search for what string? ")
            filtered = filter_by_place(quakes, string)
            print()
            printing(filtered)

      elif option == "n" or option == "N":
         quakes_dict = get_json("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson")
         found = False
         for feature in quakes_dict["features"]:
            if quake_from_feature(feature) not in quakes:
               quakes.append(quake_from_feature(feature))
               found = True

         if found == True:
            print("New quakes found!!!")
         print()
         printing(quakes) 

      elif option == "q" or option == "Q":
         write_to_file(quakes, "saved_quakes.txt")
   
            
  


               



if __name__ == "__main__":
   main()
