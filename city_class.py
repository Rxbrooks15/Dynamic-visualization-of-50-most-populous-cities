#Name: Raine.B
#Course: CS1
#Instructor: Vasanta
#Date: 11/02/2021
#Purpose: Create a city class that transfers text of given cities to an output file that
#is edited by the city class

class City:
    #constructor that initializes the 6 initial vars for the city object
    def __init__(self, ccode, cname, cregion, cpop, clat, clong):
        self.ccode = ccode  #string
        self.cname = cname  #string
        self.cregion = cregion  #string
        self.cpop = cpop    #integer
        self.clat = clat    #float
        self.clong = clong  #float


    def __str__(self):      #returns the country name, population, latitude and longitude
        return self.cname + "," + str(self.cpop) + "," + str(self.clat) + "," + str(self.clong)

