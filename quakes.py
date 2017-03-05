# Project 5 - Earthquakes
#
# Name: Taylor Morris
# Instructor: Brian Jones
# Section 17

from quake_funcs import *
from operator import attrgetter


def printing(quakes):
   print("\nEarthquakes:\n------------")

   for quake in quakes:
      print("({:.2f}) {:>40} {:s} ({:8.3f}, {:8.3f})".format(quake.mag, quake.place, 
                                 time_to_str(quake.time), quake.longitude, quake.latitude))
   print()
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
            printing(quakes) 
         elif sort_by == "t" or sort_by == "T":
            quakes.sort(key=attrgetter("time"), reverse=True)
            printing(quakes)
         elif sort_by == "l" or sort_by == "L":
            quakes.sort(key=attrgetter("longitude"))
            printing(quakes)
         elif sort_by == "a" or sort_by == "A":
            quakes.sort(key=attrgetter("latitude"))
            printing(quakes)

      elif option == "f" or option == "F":
         filter_by = input("Filter by (m)agnitude or (p)lace? ")

         if filter_by == "m" or filter_by == "M":
            lower = float(input("Lower bound: "))
            upper = float(input("Upper bound: "))
            filtered = filter_by_mag(quakes, lower, upper)
            printing(filtered)

         elif filter_by == "p" or filter_by == "P":
            string = input("Search for what string? ")
            filtered = filter_by_place(quakes, string)
            printing(filtered)

               



if __name__ == "__main__":
   main()
