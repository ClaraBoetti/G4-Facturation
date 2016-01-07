from app.devis import calculer




demande = {
     'minutes': '40',
     'commentaire': '',
     'heures': '14',
     'cp_arr': '',
     'numero_dep': '2',
     'categorie': 'particulier',
     'ville_dep': 'Toulouse',
     'adresse_dep': 'Impasse André Marfaing',
     'ville_arr': 'Agen',
     'nb_passagers': '1',
     'cp_dep': '31400',
     'numero_arr': '',
     'adresse_arr': '',
     'date_debut': '2016-01-08',
     'paiement': 'especes',
     'bagage':'0',
     'animaux':'0',
     'gare':'False',
     'aeroport':'False',
     'A-R':'True',
     'heure_retour':'12',
     'minute_retour':'00'
}
 
 
print(str(calculer.tarifs(demande)))