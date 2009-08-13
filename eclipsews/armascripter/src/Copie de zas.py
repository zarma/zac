#
# script made by Z
#

def ecrire(): 
    fsortie.write ("titi")
    

def lireconfig():
    config = []
    fconfig.readlines
    for line in fconfig:
            config.append(line.strip()) ,
    print "param extraits " + str(config)
    return config
def liremission(config):
    selection = []
    fmission.readlines
    for line in fmission:
        for chaine in config:            
            if line.find(chaine) > -1:
                selection.append(line.strip()),
    return selection

def affine(selection):
    top=False
    liste=[]
    for i in selection:
        chaine = str("text=")
        if i.find(chaine) > -1:
           top=True
           liste.append(i)
        if i.find("vehicle") > -1:
            if top:
                liste.append(i)
        if i.find("azimut") > -1:
            if top:
                liste.append(i)
        if i.find("position[]") > -1:
            if top:
                liste.append(i)
                top=False                
    return liste

def scriptsqf(p):
    for i in p:
        chaine = "vehicle="
        if i.find(chaine) > -1:
            letype = str(i).lstrip(chaine).rstrip(";")
        chaine = "position[]="
        if i.find(chaine) > -1:
          #  laposition = str(i).lstrip(chaine).rstrip(";").replace("{", "[").replace("}", "]")
            laposition = i.lstrip(chaine).rstrip(";").replace("{", "[").replace("}", "]")
            liste = laposition.split(",")
          #  print laposition
            print liste.pop(1)
            laposition = str(liste)
           
        chaine = "azimut="
        if i.find(chaine) > -1:
            azimut = str(i).lstrip(chaine).rstrip(";")
    result = "_pos = " + laposition + ";"
    print result
    result = "_veh = " + letype + " createVehicle _pos;"
    print result
    result = "_veh setDir " + azimut + ";"
    print result
    result = "_veh setPos _pos;"
    print result
    
                
fsortie = open ("F:\zas\script.txt","w")
fconfig = open ("F:\zas\config.txt","r")
fmission = open ("F:\zas\mission.sqm","r")


config = lireconfig()

selection = liremission(config)
selection.reverse()
laliste = affine(selection)
lescript = scriptsqf(laliste)
print laliste
ecrire()

fmission.close
fconfig.close
fsortie.close
print "demarrage"

