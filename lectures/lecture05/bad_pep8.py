#!/usr/bin/env python3
import math,sys

def calc_area(radius):return math.pi*radius**2

def calc_volume(my_radius):
    print("Here we are calculating the volume of a sphere with radius", my_radius)
    sphere_volume = 4 / 3 * math.pi * my_radius**3
    return sphere_volume
def main():
    r = float(input("Enter the radius:"))
    area=calc_area(r)
    print("The area is:",area)
    print("The volume is:",
                  calc_volume(r))

if __name__=='__main__':main()
