# Purpose of the program - Calculate the Delta-V requirements for a specific altitude
from math import sqrt

def calcDeltaV():
    'Estimate the DeltaV required for a specific Altitude'
    mu = 3.986004e14 #m^3/s^2
    Rearth = 6378137 #m


    altitude = input("Enter desired altitude (m): ")
    altitude = float(altitude)

    EnergyEnd = -mu/(Rearth+altitude)

    Vlaunch = sqrt(2 * (EnergyEnd + mu/Rearth))

    DeltaV = Vlaunch + altitude/1000 + altitude/2000

    return DeltaV




#Notes: Assume 1m/s per 1km for Drag, 0.5m/s per 1km for gravity