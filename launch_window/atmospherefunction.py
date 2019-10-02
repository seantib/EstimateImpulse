#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Two-Body Orbit"""
import astropy.units as u
import numpy as np
from poliastro.bodies import Earth
u.imperial.enable()


"""Python 3.7
   Simpson Aerospace (c) 2019
   Christopher R. Simpson
   christopher.r.simpson@simpsonaerospace.com"""
#------------------------------------------------------------------------------
def atmConditions(h):
    """ATMCONDITIONS Gradient method (lapse rate) to determine P, rho, T @ h
       MIL-STD-210A Assumptions:
       1. Pressure at SSL is same for cold and hot atmospheres (29.92 in Hg)
       2. Constant value of gravity to 100,000 ft (32.174 ft/sec**2)
       (Constant gravity will not be used in this case.)
       3. Constant composition of atmosphere throughout altitude range.
       4. Relative humidity not considered (dry air!)."""
    #g0 = -32.174*(u.ft/(u.s*u.s)) # ft/sec**2
    g = Earth.k/((Earth.R_mean+h)**2)
    deg_R = u.def_unit('deg_R', represents=u.K, format={'latex': r'\degree R'})
#    Rankine = u.def_unit('Rankine',u.deg_F + 459.67)
    T_ssl = (15 + 273.15)*deg_R 
    p_ssl = 14.695332*u.imperial.psi #psi
    rho_ssl = 0.00237*(u.imperial.slug/u.imperial.ft*u.imperial.ft*u.imperial.ft)
    R_air = 1716.5*(u.imperial.ft*u.imperial.lbf/(deg_R*u.imperial.slug))
    
    if(h <= 36089*u.imperial.ft):
        a = -0.003566 * (deg_R/u.imperial.ft) #Rankine per ft
        T = T_ssl + a*(h-0) #Rankine
        p = p_ssl * pow((T/T_ssl),(-g/a*R_air)) #psi
        rho = rho_ssl * pow((T/T_ssl),-((g/(a*R_air))+1))
    
    if(h <=65000*u.imperial.ft):
        a_36089 = -0.003566 * (deg_R/u.imperial.ft) #Rankine per ft
        T_36089 = T_ssl + a_36089*((36089 - 0)*u.imperial.ft) #Rankine
        p_36089 = p_ssl * ((T_36089/T_ssl)**(-g/(a_36089*R_air))) #psi
        rho_36089 = rho_ssl * (T_36089/T_ssl)**(-((g/(a_36089*R_air))+1))
        
        a = 0* (deg_R/u.imperial.ft)
        dh = (h - (36089*u.imperial.ft))
        T = T_36089 + a*dh
        p = p_36089*np.exp((-g/(R_air*T))*dh)
        rho = rho_36089 * np.exp((-g/(R_air*T))*dh)
        
    return T,p,rho,R_air,g
