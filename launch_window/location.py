#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import astropy.units as u
from astropy.coordinates import EarthLocation
class location:
    """Incorporate Earth location effect on the flight of the rocket."""
    def __init__(self, longitude, latitude, height=0.0, ellipsoid='WGS84'):
        loc_hh = EarthLocation.from_geodetic(longitude, latitude, height, ellipsoid)

        #GET THE VELOCITY?
        #From EarthLocation.get_gcrs(self, obstime)?
        #Seems too complicated.

        #Velocity of Earth at equator
        Veq = 464.5 *(u.m/u.s)
        #Earth inertial velocity addition to launch
        Vgs_lat = Veq*np.cos(np.deg2rad(latitude))

        return loc_hh, Vgs_lat
        #return super().__init__(*args, **kwargs)


