# Used to estimate the impulse required for a Delta-V Given
from math import exp, log, sqrt
from Algorithms.Trajectory.DeltaVCalc import calcDeltaV
from CEA.ceaexec.CEAfunctions import engine,writefile,runcea,readcea
import subprocess

DV = calcDeltaV()#m/s

AresEngine = engine('300','psi','27.2','CH4','O2(L)','2.0',OxTemp='90.17')

writefile(AresEngine)
runcea()
readcea()

To = float(input("Enter Chamber Temperature: ")) #Estimated from NASA CEA Program - Enter the most leftmost value
Cf = float(input("Cf value: ")) #Cf value - Estimated from NASA CEA Program - Enter the rightmost value
isp = float(input("Enter Specific Impulse: "))/9.81 #s - Enter the rightmost value
gam = float(input("Enter Specified Gamma: ")) #Specific Heat Ratio - Estimated from NASA CEA Program - Enter the Leftmost value
Cp = float(input("Enter Specific Heat Cp: "))*1000 #Specific Heat Constant Pressure - Estimated from NASA CEA Program - Enter the leftmost value



mfull = 553.2922 #kg - Estimated Rocket weight (fueled)
TWR = 1.3 #Thrust to Weight Ratio

R = Cp*(gam-1)/gam #Specific Gas Constant
MR = 1/exp(DV/isp/9.81) #Mass Fraction

gp1 = gam + 1
gm1 = gam - 1

tburn = (1 - MR) * (TWR*9.81/Cf * sqrt(gam/R/To) * (2/gp1)**(gp1/2/gm1))**(-1) # Burn Time
T = mfull*9.81*TWR #Liftoff Thrust Required

print(f'\n\n\nExpected Delta V required: {DV} m/s')
print(f'Expected Mass Fraction is: {MR} ')
print(f'Expected Burn time is: {tburn} seconds')

print(f'Expected Thrust (Liftoff) is: {T/1000} kN')
print(f'Expected impulse is: {tburn*T} Ns')

