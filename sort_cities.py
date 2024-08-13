#Name: Raine.B
#Course: CS1
#Instructor: Vasanta
#Date: 11/09/2021
#Purpose: Sorts city population, latitude and alpha

from quicksort import sort

from city_class import City

file = open("input", "r")

cities_alpha = open("cities_alpha.txt", "w")
cities_pop = open("cities_population.txt", "w")
cities_lat = open("cities_latitude.txt", "w")

clist = []

for line in file:#Reads every line in the file

    s = line.strip("\n")
    v = s.split(",")

    if len(v) == 6:

        x = City(v[0], v[1], v[2], int(v[3]), float(v[4]), float(v[5]))

        clist.append(x)

def alpha_sort(city1,city2):    #sorts the list of cities alphabetically.

    return (city1.cname.lower() <= city2.cname.lower())

sort(clist,alpha_sort)

for line in clist:  #writes new list of cities in cities_alpha
    cities_alpha.write(str(line) + "\n")


def lat_sort(city1,city2):  #sorts in order of latitudes

    return (float(city1.clat) <= float(city2.clat))

sort(clist,lat_sort)
for line in clist:  #writes new list of latitudes in cities_lat
    cities_lat.write(str(line) + "\n")

def pop_sort(city1,city2):  #sorts cities by population

    return ((int(city1.cpop) >= int(city2.cpop)))

sort(clist, pop_sort)

for line in clist:  #writes city populations from largest to smallest
    cities_pop.write(str(line) + "\n")

#closes the files
file.close()
cities_alpha.close()
cities_pop.close()
cities_lat.close()

