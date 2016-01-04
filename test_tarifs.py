import pandas as pd

heures_tarif = pd.read_csv('C:/Users/Bruno/Desktop/TaxiSID/tarif.csv', encoding='utf8')
supp = pd.read_csv('C:/Users/Bruno/Desktop/TaxiSID/Supplements.csv', encoding='utf8')

def calcul_tarifs(km, type_tarif, bagage, animal, personneSup, charge_gare):
    
#On initialise les prix de départ et les suppléments
    prise_en_charge = supp[supp['Supplements'] == 'Prise_en_charge']
    
#On prend les lignes selon les types de tarifs et on en tire le prix associé
    ligne = heures_tarif[heures_tarif['Type_Tarif'] == type_tarif]
    prix = float(ligne['tarif_par_km'])
    
#On calcule les suppléments
 #On récupère les lignes selon les suppléments et leurs prix
    bag = supp[supp['Supplements'] == 'Bagage']
    PerS = supp[supp['Supplements'] == 'PersonneSup']
    Gar = supp[supp['Supplements'] == 'Gare']
    
 #On calcule les suppléments
    supplement = bagage * float(bag['Prix']) + animal * 1
    if personneSup > 4:
        supplement += (personneSup-4) * float(PerS['Prix'])
    if charge_gare == True:
        supplement += float(Gar['Prix'])
        
#On retourne le prix total
    return float(prise_en_charge['Prix']) + prix * km + supplement
    
print("Votre itinéraire devrait vous coûter " + str(calcul_tarifs(1, 'TarifC',0,0,6,False)) + "€")


