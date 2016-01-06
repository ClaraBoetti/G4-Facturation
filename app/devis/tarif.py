from datetime import datetime

#On cherche à retourner le type de tarif (Jour ou Nuit/Dimanche/JoursFériés)
def type_tarif(demande):
    
    #On récupère la date et l'heure de départ
    date = demande['date_debut'].split('-')
    annee_depart = int(date[0])
    mois_depart = int(date[1])
    jour_depart = int(date[2])
    heure_depart = int(demande['heures'])
    minutes_depart = int(demande['minutes'])
    
    #Mise en forme de la date
    date = datetime(
        annee_depart,
        mois_depart,
        jour_depart,
        heure_depart,
        minutes_depart
    )

    #Recherche du tarif: Jour ou Nuit/JourFerie/Dimanche    
    #Initialisation du booléen
    test = False
    
    #On concaténe le mois et le jour de façon a avoir une chaine de la forme 'jour/mois'  
    dateC = str(date.day)+ '/' +str(date.month)
    
    #On vérifie si la date en entrée est un jour ferie
    ferie = dateC in [
        '1/1',
        '1/5',
        '8/5',
        '14/7',
        '15/8',
        '1/11',
        '11/11',
        '25/12'
    ]
    
    #On vérifie si l'heure est de nuit ou un dimanche
    dimanche = date.weekday()
   
    if date.hour > 19:
        test = True
    
    elif date.hour < 8:
        test = True
    
    elif ferie == True or dimanche == 6:
        test = True  
        
    #Test tarif spécial (Nuit/JourFérié/Dimanche)
    if test:
        Type_tarif = 'TarifD'
        
    #Tarif de jour par défaut 
    else:
        Type_tarif = 'TarifC'
    return Type_tarif

    
