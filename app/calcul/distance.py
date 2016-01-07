# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:53:40 2016
Last Update on Wed 6 12:00:00 2016
@author: Groupe 6
Last Update author : Groupe 6
Objectif : Calculer les distances et le temps entre deux points en fonction
du traffic
"""


# -*- coding: utf-8 -*-
#Librairies
from app.outils import utile
import json

class Parcours:
    ''' Classe définissant un parcours :
    - départ : coordonnées du lieu de départ {"lat"= valeur , "lon" = valeur} (Dictionnaire de donnée)
    - arrive : coordonnées du lieu d'arrivée {"lat"= valeur , "lon" = valeur} (Dictionnaire de donnée)
    - heure_debut : heure du départ
    - distance : distance en km
    - temps : durée du trajet en minutes
    '''
    ''' !! Penser à rendre la clef secrete pour l'application finale '''
    
    def __init__(self,depart, arrivee, heure_debut, date_format = "%Y-%m-%d %H:%M:%S"):
        self.depart = depart
        self.arrivee = arrivee
        self.heure_debut = heure_debut
        
        base = 'https://maps.googleapis.com/maps/api/directions/json?'
        origine = 'origin=' + str(depart["lat"]) + "," + str(depart["lon"])
        destination = '&destination=' + str(arrivee["lat"]) + "," + str(arrivee["lon"])
        departure_time = '&departure_time=' + str(round(utile.convert_date(heure_debut,date_format)))
        fin_url = '&traffic_model=best_guess&mode=driving&language=fr-FR&key=AIzaSyCQnaoaMu6GVo3AwRzN62l0onao2TPN_u0'
    
        '''Ajouter l'heure de depart à l'url'''
        url = base + origine + destination + departure_time + fin_url
        reponse = utile.requete_http(url)
        data_response = json.loads(reponse)

        self.distance=  round(data_response['routes'][0]['legs'][0]['distance']['value'] / 1000,2)
        self.temps= round(data_response['routes'][0]['legs'][0]['duration_in_traffic']['value'] / 60,2)