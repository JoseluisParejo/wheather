# -*- coding utf-8 -*-
import requests
import json

ciudades = {"1":"Sevilla","2":"Malaga","3":"Cadiz","4":"Cordoba","5":"Huelva","6":"Granada","7":"Jaen","8":"Almeria"}

print 
"""
1. Sevilla
2. Malaga
3. Cadiz
4. Cordoba
5. Huelva
6. Granada
7. Jaen
8. Almeria
"""
peti = raw_input("De que ciudad quieres conocer el tiempo hoy?: ")
respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudades[peti]})
dicci = json.loads(respuesta.text)
tempe = dicci["main"]["temp"] 
tempre = tempe - 273

print "la temperatura actual de",ciudades[peti],"es de",tempre,'C'   
