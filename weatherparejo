# -*- coding: utf-8 -*-
import requests
import json

ciudades = {"1":"Almeria","2":"Cádiz","3":"Córdoba","4":"Granada","5":"Huelva","6":"Jaén","7":"Málaga","8":"Sevilla"}

print """
1. Almería
2. Cádiz
3. Córdoba
4. Granada
5. Huelva
6. Jaén
7. Málaga
8. Sevilla
"""
peti = raw_input("¿De que ciudad quieres conoces el tiempo hoy?: ")
respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudades[peti]})
dicci = json.loads(respuesta.text)
tempe = dicci["main"]["temp"]
tempreal = tempe - 273

print "La temperatura actual es %s es %s grados centígrados" % (ciudades[peticion],tempreal)
