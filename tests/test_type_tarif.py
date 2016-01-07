# -*- coding: utf-8 -*-
from app.devis import Type_tarif as Typta
#Type tarif normal
def test_type_tarif():
    demande = {
         'minutes': '40',
         'commentaire': '',
         'heures': '08',
         'cp_arr': '',
         'numero_dep': '10',
         'categorie': 'particulier',
         'ville_dep': 'Toulouse',
         'adresse_dep': 'Rue Elvire',
         'ville_arr': 'Toulouse',
         'nb_passagers': '3',
         'cp_dep': '31400',
         'numero_arr': '17',
         'adresse_arr': 'Rue Elvire',
         'date_debut': '2016-01-08',
         'paiement': 'especes',
         'bagage':'0',
         'animaux':'0',
         'gare':'False',
         'aeroport':'False',
    }
    assert Typta.type_tarif(demande) == 'TarifC'

#Type tarif de nuit
    demande = {
         'minutes': '40',
         'commentaire': '',
         'heures': '06',
         'cp_arr': '',
         'numero_dep': '10',
         'categorie': 'particulier',
         'ville_dep': 'Toulouse',
         'adresse_dep': 'Rue Elvire',
         'ville_arr': 'Toulouse',
         'nb_passagers': '3',
         'cp_dep': '31400',
         'numero_arr': '17',
         'adresse_arr': 'Rue Elvire',
         'date_debut': '2016-01-08',
         'paiement': 'especes',
         'bagage':'0',
         'animaux':'0',
         'gare':'False',
         'aeroport':'False',
    }
    assert Typta.type_tarif(demande) == 'TarifD'
    
#Type tarif de nuit pour jours feries
    demande = {
         'minutes': '40',
         'commentaire': '',
         'heures': '08',
         'cp_arr': '',
         'numero_dep': '10',
         'categorie': 'particulier',
         'ville_dep': 'Toulouse',
         'adresse_dep': 'Rue Elvire',
         'ville_arr': 'Toulouse',
         'nb_passagers': '3',
         'cp_dep': '31400',
         'numero_arr': '17',
         'adresse_arr': 'Rue Elvire',
         'date_debut': '2017-01-01',
         'paiement': 'especes',
         'bagage':'0',
         'animaux':'0',
         'gare':'False',
         'aeroport':'False',
    }
    assert Typta.type_tarif(demande) == 'TarifD'
    
#Type tarif de nuit pour dimanches
    demande = {
         'minutes': '40',
         'commentaire': '',
         'heures': '08',
         'cp_arr': '',
         'numero_dep': '10',
         'categorie': 'particulier',
         'ville_dep': 'Toulouse',
         'adresse_dep': 'Rue Elvire',
         'ville_arr': 'Toulouse',
         'nb_passagers': '3',
         'cp_dep': '31400',
         'numero_arr': '17',
         'adresse_arr': 'Rue Elvire',
         'date_debut': '2016-01-10',
         'paiement': 'especes',
         'bagage':'0',
         'animaux':'0',
         'gare':'False',
         'aeroport':'False',
    }
    assert Typta.type_tarif(demande) == 'TarifD'