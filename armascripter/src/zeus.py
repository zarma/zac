# -*- coding: utf-8 -*-
# V0.9
# script made by Z
#

import sys

class variablesobjet:
    def __init__(self):
        self.efface()
    def efface(self):
        self.vehicule=""
        self.azimut=""
        self.text=""
        self.markers=[]
        self.placement="0"
        self.special="NONE"
        self.skill=0
        self.armor=1
        self.position=[]
        self.speed=""
        self.formation=""
        self.type=""
        self.behaviour=""
        self.combat=""
        self.description=""
        self.expActiv=""
        self.expDesactiv=""
        self.combatMode=""
        self.rectangular=""
        self.interruptable=""
        self.activationBy="\"NONE\""
        self.timeoutMin=0
        self.timeoutMid=0
        self.timeoutMax=0
        self.completitionRadius=0
        self.a=50
        self.b=50
        self.repeating="0"
        self.age=""
        self.angle="0"
        self.expCond='"This"'
        self.id=""
        

def ecrire(f,p): 
    f.write ("// =============================//\n")
    f.write ("// script generated by zeus \n")
    f.write ("// a Z tool\n")
    f.write ("// z_arma@hotmail.com\n")
    f.write ("// =============================//\n")
    f.write ("\n")
#    print p
    for i in p:
        f.write(i + "\n")
                
def formatter(lignes):
    liste=[]
    niveau=0 # gestion des niveaux d'accolades 
    for lig in lignes: 
        ligne = lig.strip()  
        mots = ligne.split('=',1) ## Séparation variable / valeur
#        print "mots=", mots    
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
        if p in ("Waypoints"):
            result=True
        if p in ("Sensors"):
            result=True 
        if p in ("Markers"):
            result=True     
                       
    return result


def scriptsqf(p):
#====== intitialisation des variables ==========================================    
    classe=""
    objetOk=False
    isgroup=False
    groupnumber =0
    groupname=""
    grouplist = []  # liste des unités du groupe en cours de traitement
    grouplistp = [] # liste des unités du groupe précédemment traité
    resteagrouper=0
    taillegroupe=0
    v = variablesobjet()    
    n=0
    lescript = []
    finobjet=False
    niveaus=niveauc=0 # niveau de l'objet selectionné et niveau courrant
#===============================================================================    
#    print "scriptsqf(p) \n" + str(p)
    for i in p:
#        print i
        if i[0] == "{": niveauc = i[1]
        
        if selection(str(i[-1])):
            classe = str(i[-1])
            niveaus = niveauc + 1 # stockage du niveau de l'accolade suivante
        if str(i[-1]) == "Groups" and niveauc == 2:
            isgroup=True   
        if isgroup and niveauc==2 and i[0] == "};":
            isgroup=False

        if v.position:
            objetOk=True
           
        chaine ="class"
        if chaine == i[0]:
            if "Item" in i[1]:
                print "Item ----",i[1]
                if objetOk:
                    finobjet=True
        chaine = "};"    # fin de classe
#        print "classe,id", classe, v.id,niveauc,niveaus
        if chaine in i > -1:
            niveauc = i[1]
            if niveauc == niveaus:
                finobjet=True
            if niveauc < niveaus:
                niveaus=0 # nous sommes à la fin d'une classe selectionnée
                
        chaine ="id"
        if chaine == i[0]:
           v.id = i[1]
           
        chaine ="items"
        if chaine == i[0]:
            if classe=="Vehicles" and isgroup and niveauc==4:
                groupnumber +=1
                groupname = "grp"+  str(groupnumber)
                taillegroupe=resteagrouper=int(i[1].rstrip(";"))
#                print "items", i[1],groupnumber,resteagrouper
 
        chaine = "side"
        if chaine == i[0]:
            side = i[1].rstrip(";").strip('"')         
        chaine = "vehicle"
        if chaine == i[0]:
            v.vehicule = i[1].rstrip(";")
            print v.vehicule
        chaine = "azimut"
        if chaine == i[0]:
            v.azimut = i[1].rstrip(";")
        chaine = "position[]"
        if chaine == i[0]: # ajout troisième dimension
            print "i position" , i
            v.position = i[1].rstrip(";").lstrip("{;").rstrip("};") 
            liste = v.position.split(",")
            t= liste.pop(1)
            liste.append(t)
            v.position = str(liste).lstrip("[").rstrip("]").replace("'", "")           
        chaine = "skill"
        if chaine == i[0]:
            v.skill = i[1]
        chaine = "health"
        if chaine == i[0]:
            v.armor = i[1]
        chaine = "placement"
        if chaine == i[0]:
            v.placement = i[1].rstrip(";")           
        chaine = "completitionRadius"
        if chaine == i[0]:
            v.completitionRadius = i[1]
        chaine = "type"
        if chaine == i[0]:
            v.type = i[1].rstrip(";")
        chaine = "combatMode"
        if chaine == i[0]:
            v.combatMode = i[1]
        chaine = "formation"
        if chaine == i[0]:
            v.formation = i[1]
        chaine = "speed"
        if chaine == i[0]:
            v.speed = i[1]
        chaine = "combat"
        if chaine == i[0]:
            v.combat = i[1]
        chaine ="description"
        if chaine == i[0]:
	       v.description = i[1]
        chaine ="timeoutMin"
        if chaine == i[0]:
	       v.timeoutMin = i[1].rstrip(";")
        chaine ="timeoutMid"
        if chaine == i[0]:
           v.timeoutMid = i[1].rstrip(";")
        chaine ="timeoutMax"
        if chaine == i[0]:
           v.timeoutMax = i[1].rstrip(";")                   
        chaine = "a"
        if chaine == i[0]:
            v.a = i[1].rstrip(";")
        chaine = "b"
        if chaine == i[0]:
            v.b = i[1].rstrip(";")
        chaine ="angle"
        if chaine == i[0]:
	       v.angle = i[1].rstrip(";")
        chaine ="rectangular"
        if chaine == i[0]:
	       v.rectangular = i[1].rstrip(";")        
        chaine ="activationBy"
        if chaine == i[0]:
	       v.activationBy = i[1].rstrip(";")
        chaine ="activationType"
        if chaine == i[0]:
	       v.activationType = i[1].rstrip(";")
        chaine ="repeating"
        if chaine == i[0]:
	       v.repeating = i[1].rstrip(";")
        chaine ="interruptable"
        if chaine == i[0]:
	       v.interruptable = i[1].rstrip(";")
        chaine ="age"
        if chaine == i[0]:
	       v.age = i[1]
        chaine ="text"
        if chaine == i[0]:
	       v.text = i[1].rstrip(";")
        chaine ="name"
        if chaine == i[0]:
	       v.name = i[1]
        chaine ="expCond"
        if chaine == i[0]:
           v.expCond = i[1].rstrip(";")         
        chaine ="expActiv"
        if chaine == i[0]:            
            v.expActiv = i[1].rstrip(";").replace("\"\"","'")
        chaine ="expDesactiv"
        if chaine == i[0]:
	       v.expDesactiv = i[1].rstrip(";").replace("\"\"","'")
        chaine ="track"
        if chaine == i[0]:
	       v.track = i[1]
           
 
        
 
        
        if finobjet and objetOk:
#            print "classe,id", classe, v.id
            n += 1
            lescript.append("")
            lescript.append("// id " + v.id)
            if classe == "Vehicles":
                
                objname = "_veh" + str(n)
                if v.text:
                    objname=v.text.strip("\"")
                                    
                result = "_pos = [" + v.position + "];"
                lescript.append(result)
                print "taillegroupe ", taillegroupe
                if taillegroupe: 
                    grouplist += [objname]
                    if taillegroupe == resteagrouper:
                        result = groupname + " = createGroup (" + side + ");"
                        lescript.append(result)                        
                    resteagrouper-=1
                    result = objname  + " = " + groupname +" createUnit [" + v.vehicule + ", _pos," + str(v.markers) + "," + str(v.placement) + ",\"" + str(v.special) +"\"];"
                    lescript.append(result) 
                else:
                    result = objname  + " = createVehicle [" + v.vehicule + ", _pos," + str(v.markers) + "," + str(v.placement) + ",\"" + str(v.special) +"\"];"
                    lescript.append(result)
                
                if v.azimut:
                    result = objname + " setDir " + v.azimut + ";"
                    lescript.append(result)
                    
                result = objname + " setPos _pos;"
                lescript.append(result)
                                
                result = objname + " setSkill " + str(v.skill) 
                lescript.append(result)
                
                if v.armor != 1:
                    result = objname + " setVehicleArmor " + str(v.armor) 
                    lescript.append(result)
                    
     
                
                if len(grouplist)>1 and resteagrouper==0:
                    lescript.append("")
                    print "grouplist", grouplist
                    
                    result = str(grouplist).replace("'", "") + " join " + groupname +";"
                    lescript.append(result)

                if niveauc==4:
                    grouplistp=grouplist
                    grouplist=[]
                    taillegroupe=0
                    
                lescript.append("")              
                
                
                
            if classe == "Waypoints":
                objname = "_wp" + str(n)               
                result = "_pos = [" + v.position + "];"
                lescript.append(result)
                result = "_radius = " + v.placement + ";"
                lescript.append(result)
                result = objname + " = " + groupname +" addWaypoint [_pos,_radius];"
                lescript.append(result)
                    
                if v.formation:
                    result = objname + " setWaypointFormation " + v.formation;
                    lescript.append(result)
                    
                if  not v.type:
                    v.type = "\"MOVE\"";
                    
                result = objname + " setwaypointtype " + v.type + ";"
                lescript.append(result)
                
                   
                    
                if v.speed:
                    result = objname + " setWaypointSpeed " + v.speed
                    lescript.append(result)
                    
                if v.combat:
                    result = objname + " setWaypointBehaviour " + v.combat
                    lescript.append(result)
                    
                if v.combatMode:
                    result = groupname + " setCombatMode " + v.combatMode
                    lescript.append(result)
                
                if v.completitionRadius:
                    result = objname + " setWaypointCompletionRadius " + v.completitionRadius
                    lescript.append(result)

                if v.description:
                    result = objname + " setWaypointDescription " + v.description
                    lescript.append(result)                    
                
                if v.expActiv:
                    condition = '"true"'
                    print v.expActiv
                    result = objname + " setWaypointStatements [" + condition + ", " + v.expActiv + "];" 
                    lescript.append(result)    
            
                if v.timeoutMin or v.timeoutMid or v.timeoutMax:
                    result = objname + " setWaypointTimeout ["+ str(v.timeoutMin) +","+ str(v.timeoutMid) +","+ str(v.timeoutMax) + "];" 
                    lescript.append(result)
                    
            if classe == "Sensors":
                objname = "_t" + str(n) 
                result = "_pos = [" + v.position + "];"
                lescript.append(result)

                result = objname + " = createTrigger[\"EmptyDetector\",_pos];"
                lescript.append(result)
                
                if v.repeating == "1": tf = "true" 
                else: tf="False"
#                if activationType=="":activationType='"PRESENT"'
#                result = "_t" + str(n) + " setTriggerActivation [" + activationBy + ", " + activationType + ", " + tf + "];"
#                lescript.append(result)
                
                if v.rectangular: tf="True"
                else: tf="False"
                result = objname + " setTriggerArea [" + str(v.a) + "," + str(v.b) + "," + v.angle + "," + tf + "];" 
                lescript.append(result)
                
                if v.expActiv or v.expDesactiv or v.expCond:
                    print "v.expActiv" , v.expActiv
                    if not v.expDesactiv: v.expDesactiv = '""'
                    if not v.expActiv: v.expActiv = '""'
                    result = objname + " setTriggerStatements [" + v.expCond +","+  v.expActiv +","+ v.expDesactiv + "];" 
                    lescript.append(result)
                if v.repeating: tf="True"
                else: tf="False"
                if not v.type:
                    v.type = "\"PRESENT\""
                result = objname + " setTriggerActivation [" + v.activationBy + "," + v.type + "," + tf + "];"
                lescript.append(result) 
                print "time ", v.timeoutMin, v.timeoutMid, v.timeoutMax
                if v.interruptable == "1": tf = "true" 
                else: tf="False"
                if v.timeoutMin or v.timeoutMid or v.timeoutMax:
                    result = objname + " setTriggerTimeout ["+ str(v.timeoutMin) +","+ str(v.timeoutMid) +","+ str(v.timeoutMax) + "," +tf + "];" 
                    lescript.append(result)                
                
                if v.text:
                    result = objname + " setTriggerText " + v.text  
                    lescript.append(result)
            objetOk=False           
            finobjet=False
            
            v = variablesobjet()

            
    return lescript

def main():
    args = sys.argv[1:]
    print "DEBUT", args     
    if "mission.sqm" in args[0]: 
        fmission = open (str(args[0]),"r")
        chaine = str(args[0].rstrip("mission.sqm")) + "zeusscript.sqf"    
        
        fsortie = open (chaine,"w")
         
        #for i in formatter(fmission.readlines()):
        #    print i
        liste1 = formatter(fmission.readlines())
        lescript = scriptsqf(liste1)
        #for i in scriptsqf(liste1):
        #    print i
        
        ecrire(fsortie,lescript)
        
        fmission.close
        fsortie.close
        print "FIN"

if __name__ == '__main__':
    main()


