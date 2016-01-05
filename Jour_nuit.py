# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 09:25:59 2016

@author: riwan
"""

from datetime import datetime
#cette fonction retourne un booléen qui indique si il y a une augmentattion du prix a cause des criteres jour férié,nuit,dimanche pour une date en entrée 
def tarifPlus(debut):
    #initialisation du booléen
    test=False
    #on concaténe le mois et le jour de façon a avoir une chaine de la forme 'jour/mois'  
    datef=str(debut.day)+'/'+str(debut.month)
    #on vérifie si la date en entrée est un jour ferie
    ferie=datef  in ['1/1','1/5','8/5','14/7','15/8','1/11','11/11','25/12']
    #on vérifie si la date en entrée est un dimanche
    dimanche=debut.weekday()
    if debut.hour > 19:
        test = True
    elif debut.hour <8:
        test=True
    elif ferie ==True or dimanche==6:
        test = True
    return test
       
date=datetime(2016, 12, 25, 9, 0)    
tarifPlus(date)
