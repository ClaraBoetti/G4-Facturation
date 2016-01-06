from app.devis import calculer




demande = {
     'minutes': '40',
     'commentaire': '',
     'heures': '08',
     'cp_arr': '31400',
     'numero_dep': '2',
     'categorie': 'particulier',
     'ville_dep': 'Toulouse',
     'adresse_dep': 'Impasse André Marfaing',
     'ville_arr': 'Toulouse',
     'nb_passagers': '1',
     'cp_dep': '31400',
     'numero_arr': '2',
     'adresse_arr': 'Impasse André Marfaing',
     'date_debut': '2016-01-06',
     'paiement': 'especes',
     'bagage':'0',
     'animaux':'0',
     'gare':'False',
     'aeroport':'False'
 }
 
 
print(str(calculer.tarifs(demande)))