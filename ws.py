#!/usr/bin/env python3
import urllib.request
import urllib.parse
import http.client
import json

print("Consulta webService de sismos")
try:
    url = "http://api.geonames.org/earthquakesJSON?formatted=true&north=44.1&south=-9.9&east=-22.4&west=55.2&username=davel"
    f = urllib.request.urlopen(url,timeout=30)
    djson = json.loads(f.read())
    print("Fecha: ")
    print(djson['earthquakes'][0]['datetime'])
    print("Coordenadas [lat, long]")
    print(djson['earthquakes'][0]['lat'])
    print(djson['earthquakes'][0]['lng'])
    print("Magnitud")
    print(djson['earthquakes'][0]['magnitude'])
       
except:
    print('Error al consultar datos')
