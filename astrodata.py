"""This is the backend to my planetarium app. It calculates the location of pre-chosen objects
based on the user's location. The astronomical coordinate system used is alt/az."""

import json
import pandas as pd
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import requests

#opens/reads csv datafile consisting of all mapped celestial objects

astrodata = pd.read_csv("astrodatalabels.csv", header=0, names=["Stars", "Messier", "Solar System"])
print(astrodata)

#user location based on IP address

resp_ip = requests.get('http://ipinfo.io/')
loc_json = resp_ip.json()
loc_data = loc_json['loc'].split(",")
lat = float(loc_data[0])
lon = float(loc_data[1])

#user elevation infromation based on IP address

API_KEY = "AIzaSyDwg1l0kMyhYagjdIikdTF57J5p_YVOsDE"
ELEVATION_URL = "https://maps.googleapis.com/maps/api/elevation/json?locations={},\
   {}&key={}".format(lat, lon, API_KEY)
resp_elevation = requests.get(ELEVATION_URL)
elev_json = resp_elevation.json()
elevation = elev_json["results"][0]["elevation"]
location = EarthLocation(lat=lat*u.deg, lon=lon*u.deg, height=elevation*u.m)

#RA/DEC coordinate calculation for all objects in csv file "astro data"

star_coords = set()
messier_coords = set()
ss_coords = set()
for index, row in astrodata.iterrows():
    star_coords.add(SkyCoord.from_name(row[0]))
    messier_coords.add(SkyCoord.from_name(row[1]))
    #ss_coords.add(SkyCoord.from_name(row[2].lower()))
    #messier_coords += SkyCoord.from_name(row[1])
    #ss_coords += SkyCoord.from_name(row[2])

#alt/az coordinate conversions

#for row in astrodata:
 #   star_coords = SkyCoord.from_name(starsz
  #  messier_coords = SkyCoord.from_name(messier)
   # solar_system_objects_coords = SkyCoord.from_name(solar_system_objects)
#utcoffset = -4*u.hour  # Eastern Daylight Time
#time = Time('2020-4-25 23:37:00') - utcoffset
#m13altaz = m13.transform_to(AltAz(obstime=time,location=toronto))
