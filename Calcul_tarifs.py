import pandas as pd
import Calcul_distance as cd
import Type_tarif as Typta

def heures_tariff(demande):
    categorie=demande['categorie']
    if categorie=='particulier':
       
      return  pd.read_csv('data/tarif.csv', encoding='utf8')
    else: 
        
      return pd.read_csv('data/tarif-Pro.csv', encoding='utf8')
      
def suppf(demande):
    categorie=demande['categorie']
    if categorie=='particulier':       
      return  pd.read_csv('data/Supplements.csv', encoding='utf8')
    else:         
      return pd.read_csv('data/Supplements-Pro.csv', encoding='utf8')

def calcul_tarifs(demande):
    supp=suppf(demande)
    heures_tarif =heures_tariff(demande)

#On initialise les prix de départ et les suppléments
    prise_en_charge = supp[supp['Supplements'] == 'Prise_en_charge']
    
#On prend les lignes selon les types de tarifs et on en tire le prix associé
    ligne = heures_tarif[heures_tarif['Type_Tarif'] == Typta.Type_tarif(demande)]
    prix = float(ligne['tarif_par_km'])
    
#On calcule les suppléments
 #On récupère les lignes selon les suppléments et leurs prix
    an= supp[supp['Supplements'] == 'Animal']
    bag = supp[supp['Supplements'] == 'Bagage']
    PerS = supp[supp['Supplements'] == 'PersonneSup']
    Gar = supp[supp['Supplements'] == 'Gare']
    Aer = supp[supp['Supplements'] == 'Aeroport']
    
 #On calcule les suppléments
    supplement = float(demande['bagage']) * float(bag['Prix']) + float(demande['animaux']) * float(an['Prix'])
    if int(demande['nb_passagers']) > 4:
        supplement += (float(demande['nb_passagers'])-4) * float(PerS['Prix'])
    if demande['gare'] == 'True':
        supplement += float(Gar['Prix'])
    if demande['aeroport'] == 'True':
        supplement += float(Aer['Prix'])

  #On concatenne les adresses de départ et d'arrivée
    depart = demande['numero_dep'] + ' ' + demande['adresse_dep'] + ' ' + demande['cp_dep'] + ' ' + demande['ville_dep']
    arrive = demande['numero_arr'] + ' ' + demande['adresse_arr'] + ' ' + demande['cp_arr'] + ' ' + demande['ville_arr']       
#On calcule le prix total
    prixTotal = float(prise_en_charge['Prix']) + prix * cd.recup_distance(cd.distance(depart,arrive)) + supplement
    
    #On vérifie que le prix total soit supérieur au prix minimal
    prixMinimal = float(supp[supp['Supplements'] == 'Tarif_minimum']['Prix'])
    if prixTotal < prixMinimal:
        prixTotal = prixMinimal
        
    #On retourne le prix total
    if demande['gare']== 'True':
        if int(demande['nb_passagers']) > 4:
            a = {
                'Prix_Total' : str(round(prixTotal,2)), 
                'Prise_en_charge' : str(float(prise_en_charge['Prix'])),
                'Nombre_bagage' : str(demande['bagage']),
                'Prix_1_bagage' : str(float(bag['Prix'])),
                'prix_total_bagage' : str(float(demande['bagage']) * float(bag['Prix'])),
                'animal' : str(demande['animaux']),
                'prix_animal' : str(float(an['Prix'])),
                'prix_total_animal' : str(float(demande['animaux']) * float(an['Prix'])),
                'Gare' : str(demande['gare']),
                'Prix_Gare' : str(float(Gar['Prix'])),
                'Nombres_personnes_sup' : str(float(demande['nb_passagers']) - 4 ),
                'Prix_par_personnes_sup' : str(float(PerS['Prix'])),
                'Prix_personnes_sup' : str((float(demande['nb_passagers'])-4) * float(PerS['Prix']))
                 }
        else:
            a = {
                'Prix_Total' : str(round(prixTotal,2)), 
                'Prise_en_charge' : str(float(prise_en_charge['Prix'])),
                'Nombre_bagage' : str(float(demande['bagage'])),
                'Prix_1_bagage' : str(float(bag['Prix'])),
                'prix_total_bagage' : str(float(demande['bagage']) * float(bag['Prix'])),
                'animal' : str(demande['animaux']),
                'prix_animal' : str(float(an['Prix'])),
                'prix_total_animal' : str(float(demande['animaux']) * float(an['Prix'])),
                'Gare' : str(demande['gare']),
                'Prix_Gare' : str(float(Gar['Prix'])),
                'Nombres_personnes_sup' : 0,
                'Prix_par_personnes_sup' : 0,
                'Prix_personnes_sup' : 0
                 }
    else:
        if int(demande['nb_passagers']) > 4:
            a = {
                'Prix_Total' : str(round(prixTotal,2)),
                'Prise_en_charge' : str(float(prise_en_charge['Prix'])),
                'Nombre_bagage' : str(float(demande['bagage'])),
                'Prix_1_bagage' : str(float(bag['Prix'])),
                'prix_total_bagage' : str(float(demande['bagage']) * float(bag['Prix'])),
                'animal' : str(demande['animaux']),
                'prix_animal' : str(float(an['Prix'])),
                'prix_total_animal' : str(float(demande['animaux']) * float(an['Prix'])),
                'Gare' : str(demande['gare']),
                'Prix_Gare' : 0,
                'Nombres_personnes_sup' : str(float(demande['nb_passagers']) - 4 ),
                'Prix_par_personnes_sup' : str(float(PerS['Prix'])),
                'Prix_personnes_sup' : str((float(demande['nb_passagers'])-4) * float(PerS['Prix']))
                 }
        else:
            a = {
                'Prix_Total' : str(round(prixTotal,2)),
                'Prise_en_charge' : str(float(prise_en_charge['Prix'])),
                'Nombre_bagage' : str(float(demande['bagage'])),
                'Prix_1_bagage' : str(float(bag['Prix'])),
                'prix_total_bagage' : str(float(demande['bagage']) * float(bag['Prix'])),
                'animal' : str(demande['animaux']),
                'prix_animal' : str(float(an['Prix'])),
                'prix_total_animal' : str(float(demande['animaux']) * float(an['Prix'])),
                'Gare' : str(demande['gare']),
                'Prix_Gare' : 0,
                'Nombres_personnes_sup' : 0,
                'Prix_par_personnes_sup' : 0,
                'Prix_personnes_sup' : 0
                 }        

    #On retourne le prix total
    return a
    
print("Votre itinéraire devrait vous coûter " + str(calcul_tarifs(Typta.demande))+ "€")

