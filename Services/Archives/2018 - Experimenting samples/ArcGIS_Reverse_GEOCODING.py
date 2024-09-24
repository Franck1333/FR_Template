# coding: utf-8

# In[2]:


#---------------------------------------------------------------------------
#---ArcGIS API---

#AIDES: https://notebooks.esri.com/user/8uWENFEcO3tFj41KxMulwiGrG/tree
#AIDES: https://developers.arcgis.com/labs/python/search-for-an-address/
#AIDES: https://developers.arcgis.com/rest/services-reference/geographic-coordinate-systems.htm
#AIDES: https://developers.arcgis.com/python/guide/reverse-geocoding/
#AIDES ISSUE : https://github.com/jupyter/jupyter/issues/270

#-----------------------------------------------------------------
#The following code in a cell to import the ArcGIS API for Python
#Ce qui suit permet d'importer le contenue de l'API ArcGIS pour Python
from arcgis.gis import *
from arcgis.geocoding import geocode, reverse_geocode
from arcgis.geometry import Point
#-----------------------------------------------------------------

dev_gis = GIS()  #Log into ArcGIS Online as an anonymous user

#Construct a Point geometry object for the following latitude and longitude
location = {'Y':47.2224326667,'X':-0.729606666667,
            'spatialReference':{
            'wkid':4231}
           }
unknown_pt = Point(location)

#Reverse geocode the Point to get the address
address = reverse_geocode(location=unknown_pt)

print (address)

#---ArcGIS API---
#---------------------------------------------------------------------------

