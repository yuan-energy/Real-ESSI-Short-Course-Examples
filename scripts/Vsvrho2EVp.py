#!/usr/bin/python

from math import sqrt
import sys

if len(sys.argv) < 4 :
	print( " ERROR!! : Require 3 arguments: Vs, v, rho, respectively")
	sys.exit()

Vs = (float)(sys.argv[1])
v = (float)(sys.argv[2])
rho = (float)(sys.argv[3])

print( "Vs  = " + str(Vs) +   " m/s    ")
print( "v   = " + str(v) +   "       ")
print( "rho = " + str(rho) + " kg/m^3")

# G = E / 2. / (1 + v )
G = rho * Vs * Vs
print( "G   = " + str(G)  +  " Pa    ")

# Vs = sqrt(G / rho )
E = 2. * G * (1. + v )
print( "E   = " + str(E/1e6) +  " MPa   ")

M = E * ( 1 - v ) / (1 + v ) / ( 1 - 2 * v )
print( "M   = " + str(M/1e6)  +  " MPa    ")
Vp = sqrt( M  / rho )
print( "Vp  = " + str(Vp) +  " m/s   ")






