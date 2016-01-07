from app.devis import calculer




demande = {
     'minutes': '00',
     'commentaire': '',
     'heures': '10',
     'cp_arr': '',
     'numero_dep': '',
     'categorie': 'particulier',
     'ville_dep': 'Blagnac',
     'adresse_dep': '',
     'ville_arr': 'Ramonville',
     'nb_passagers': '1',
     'cp_dep': '',
     'numero_arr': '',
     'adresse_arr': '',
     'date_debut': '2016-01-10',
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