from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

#add_polygon(polygons,0,0,0,50,0,0,25,25,0)
parse_file( 'script', edges, polygons, transform, screen, color )
#parse_file( 'test', edges, polygons, transform, screen, color )
