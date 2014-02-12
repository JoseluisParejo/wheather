# -*- coding: utf-8 -*-
import requests
import json

ciudades = {"1":"Sevilla","2":"Málaga","3":"Cádiz","4":"Córdoba","5":"Huelva","6":"Granada","7":"Jaén","8":"Almería"}

print 
"""
1. Sevilla
2. Málaga
3. Cádiz
4. Córdoba
5. Huelva
6. Granada
7. Jaén
8. Almería
"""
peti = raw_input("¿De que ciudad quieres conoces el tiempo hoy?: ")
respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudades[peti]})
dicci = json.loads(respuesta.text)
tempe = dicci["main"]["temp"] - 273

print "la temperatura actual de",provincias[peti], "es:",tempe, "grados centigrados"
