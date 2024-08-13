#Name: Raine.B
#Course: CS1
#Instructor: Vasanta
#Date: 11/08/2021
#Purpose: draws world map and produce 50 dots cities from largest pop to smallest

from sort_cities import *
from cs1lib import *

image = load_image("world.png")

WIDTH = 720
HEIGHT = 360

count = 0
drawn_cities = []

def main_draw_func():#main draw fucntion draws the 50 cities on the map
    draw_image(image, 0, 0)
    draw_cities(50)

#draws city dots one by one till it is less than or equal to value given
def draw_cities(num):

    global count
    if len(drawn_cities) <= num:
       drawn_cities.append(clist[count])
       count += 1

    for cities in drawn_cities:     #locates cities in drawn_cities and draws circles depending on the lat and long location

        lat_scale = WIDTH//2+ (WIDTH*cities.clong/180)//2
        long_scale = HEIGHT//2 - (HEIGHT *cities.clat//90)//2

        set_fill_color(0, 1, 0.8 )
        draw_circle(lat_scale, long_scale, 5)


start_graphics(main_draw_func, width=WIDTH, height=HEIGHT, framerate=10)

