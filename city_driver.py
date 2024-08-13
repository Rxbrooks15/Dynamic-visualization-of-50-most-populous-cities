#Name: Raine.B
#Course: CS1
#Instructor: Vasanta
#Date: 11/02/2021
#Purpose:tore the information about each city
# into its own City object within a list, and write out each object (converted to a string) to a file.

from city_class import City
#file reads the text in input
file = open("input", "r")
cities_out = open("cities_out", "w")

#new list where the city list will be placed
mlist = []

for line in file:
    x = line.strip("\n")    #places code in one line
    y = x.split(",")    #removes commas
    if len(y) == 6:#if the elemetns in the list are6 then end the elements into mlist
        z = City(y[0], y[1], y[2], y[3], y[4], y[5])
        mlist.append(z)

for line in mlist:
    cities_out.write(line.__str__() + "\n")

file.close()
cities_out.close()
