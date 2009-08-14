# -*- coding: utf-8 -*-
#
# script made by Z
#

def ecrire(p): 
    fsortie.write ("// =============================//\n")
    fsortie.write ("// script generated by zeus \n")
    fsortie.write ("// a Z tool\n")
    fsortie.write ("// z_arma@hotmail.com\n")
    fsortie.write ("// =============================//\n")
    fsortie.write ("\n")
#    print p
    for i in p:
        fsortie.write(i + "\n")
                
def formatter(lignes):
    liste=[]
    niveau=0 # gestion des niveaux d'accolades 
    for lig in lignes: 
        ligne = lig.strip()  
        mots = ligne.split('=') ## Séparation variable / valeur    
        if len(mots)==2:
            liste.append(mots)
        else:
            mots = ligne.split(" ")
#            print mots
            if mots[0] == "class":
                liste.append(mots)
            if mots[0] == "{":
                niveau += 1
                liste.append([mots[0],niveau])
            if mots[0] == "};":            
                liste.append([mots[0],niveau])
                niveau -= 1
    return liste 
           
def selection(p):
    result = False 
    if p:
        if p in ("Vehicles"):
            result=True
    return result
def scriptsqf(p):
    lescript = []
    finobjet=False
    niveaus=niveauc=0 # niveau de l'objet selectionné et niveau courrant
    markers , placement , special, skill, armor = "[]","0","NONE",0,1
    print "scriptsqf(p) \n" + str(p)
    for i in p:
        if i[0] == "{": niveauc = i[1]
        if selection(str(i[-1])):
            niveaus = niveauc + 1 # stockage du niveau de l'accolade suivante
            print i, "OK"
        chaine = "vehicle"
        if chaine in i > -1:
            print i[1]
            letype = i[1].rstrip(";")
        chaine = "azimut"
        if chaine in i > -1:
            azimut = i[1].rstrip(";")
        chaine = "position[]"
        if chaine in i > -1:
            laposition = i[1].rstrip(";").rstrip("};") + ",0"
            liste = laposition.split(",")
            liste.pop(1)
            laposition = str(liste).lstrip("[").rstrip("]").replace("'", "")
        chaine = "skill"
        if chaine in i > -1:
            skill = i[1]
        chaine = "health"
        if chaine in i > -1:
            armor = i[1]
        chaine = "type"
        if chaine in i > -1:
            type = i[1]
        chaine = "combatMode"
        if chaine in i > -1:
            combatMode = i[1]
        chaine = "formation"
        if chaine in i > -1:
            formation = i[1]
        chaine = "speed"
        if chaine in i > -1:
            speed = i[1]
        chaine = "combat"
        if chaine in i > -1:
            combat = i[1]
        chaine = "};"
        if chaine in i > -1:
            niveauc = i[1]
            if niveauc == niveaus:
                finobjet=True
            if niveauc < niveaus:
                niveaus=0 # nous sommes à la fin d'une classe
        
        if finobjet:
            lescript.append("")
            result = "_pos = [" + laposition + "]"
            lescript.append(result)
            result = "_veh = createVehicle [" + letype + ", _pos," + markers + "," + placement + "," + special+"];"
            lescript.append(result)
            if azimut:
                result = "_veh setDir " + azimut + ";"
                lescript.append(result)
            result = "_veh setPos _pos;"
            lescript.append(result)
            print "skill " , skill
            result = "_veh setSkill " + str(skill) 
            lescript.append(result)
            if armor != 1:
                result = "_veh setVehicleArmor " + str(armor) 
                lescript.append(result)
            lescript.append("")
            
            markers , placement , special, skill, armor = "[]","0","NONE",0,1
            finobjet=False

            
    return lescript

print "DEBUT"         

fmission = open ("F:\zas\mission.sqm","r")
fsortie = open ("F:\zas\script.sqf","w")

#for i in formatter(fmission.readlines()):
#    print i
liste1 = formatter(fmission.readlines())
lescript = scriptsqf(liste1)
#for i in scriptsqf(liste1):
#    print i

ecrire(lescript)

fmission.close
fsortie.close

print "FIN"
