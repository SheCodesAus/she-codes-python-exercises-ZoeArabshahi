#Write a program that takes a distance in kilometers from the user, and output the distance in meters and
#centimeters.

dist=input("How many kilometers? ")
dist_m=float(dist)*1000
dist_cm=float(dist)*100000
print(float(dist),"km","=",float(dist_m),"m")
print(float(dist),"km","=",float(dist_cm),"cm")

