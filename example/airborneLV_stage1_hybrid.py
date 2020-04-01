#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""estimate first stage performance"""
#libraries
import numpy as np
#from CEA.ceaexec.CEAfunctions import engine, writefile, runcea, readcea

"""Python 3.7
   Simpson Aerospace (c) 2020
   Christopher R. Simpson: christopher.r.simpson@simpsonaerospace.com"""
#------------------------------------------------------------------------------
#Non-dimensionalized ---> X=x/r(0,0), Tau=t/tburn, R=r(x,t)/r(0,0)
#J(x,t) = (mdotox(0) + mdotf(x,t))/mdotox(0)
#Lambda(x,t) = (mdotox(t) - mdotf(0))/mdotox(0)
 


#Step 1
    #Specify r(x=0,t=0), Lport, tburn, a, n, and m
n=0.62
m=0.015
a=9.27e-5; #m^(2.39=(2n+m+1))kg^(-0.62=-n)sec^(-0.38=n-1)
r0    = 0.0508; #m, r(x=0,t=0)
Lport = 1.143;#m, length of port
tburn = 100;  #sec, length of burn
rhof = 920.0; #kg/m3
mdotox0 = 50*(np.power(100,2))/1000;#kg/m^2-sec

#Step 2 
    #Make grid of X and Tau
imax = 2000;
jmax = 2000;
X = [(i/imax)*(Lport/r0) for i in range(imax)];
Tau = [(j/jmax) for j in range(jmax)];

    #Calculate CR and CJ
CR = (a*tburn* np.power(mdotox0,n))/(np.power(r0,(2*n + m + 1)));
CJ = (a*rhof*mdotox0**(n - 1))/(r0**(2*n + m - 2));

#Step 3 Create tables defining the initial port geometry and mdotox flow rate
    #If initial port radius not constant, specify R(X,0)
#R = [r0/r0 for i in range(imax)]
    #If oxidizer flow not constant, specify Lambda(Tau)
Lambda = [(mdotox0 - mdotox0) for j in range(jmax)];

#Step 4 Define initial radius values and mass flow functions
R=[[1 for j in range(jmax)] for i in range(imax)];
J = R;

#Step 5 Update the R and J tables over length of port and for length of burn
dTau = 1/jmax;
dX = (1/imax)*(Lport/r0);

for i in range(1,imax - 1):
    for j in range(jmax - 1):
        drdt = np.power(((J[i][j] + Lambda[j])/(np.pi*R[i][j]**2)),n);
        R[i][j + 1] = R[i][j] + (dTau * (CR/X[i]**m) * drdt)
        J[i + 1][j] = J[i][j] + (dX * ((CJ * 2 * np.pi * R[i][j])/(X[i]**m)) * drdt)
