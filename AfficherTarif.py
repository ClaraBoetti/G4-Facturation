# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:07:32 2016

@author: AntoineP
"""

import pandas as pd

tarifs = pd.read_csv('tarif.csv')
supplements = pd.read_csv('supplements.csv')

tarifUtilisé = tarifs['tarif_par_km'][0]
def afficherTarif (typeTarif, km, nbBagages,nbPersonneSup, boolGare, nbAnimaux) : 
    typeTarif = tarifs[tarifs['Type_Tarif']==typeTarif]
    prixPriseEnCharge = supplements['Prix'][4]
    prixBagages = nbBagages * supplements['Prix'][0]
    prixPersonneSup = nbPersonneSup * supplements['Prix'][1]
    if boolGare:
        prixGare = supplements['Prix'][3]
    else :
        prixGare = 0
    prixAnimaux = nbAnimaux * supplements['Prix'][2]
    prix = typeTarif['tarif_par_km'] * km + prixPriseEnCharge + prixBagages + prixPersonneSup + prixGare + prixAnimaux
    return (prix)

print(afficherTarif('TarifC',0,2,2,1,3))
    

    