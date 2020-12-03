import vagrant,os






class WrongInput(Exception):
    pass
#We schrijven onze eigen exception
    


opties = {"1":") Windows 10 host" ,"2":") Linux Ubuntu host" ,"3":") Windows Server" ,"4":") Vyos router" ,"5":") Webserver" ,"6":") Volledige Omgeving" ,"7":") Gegevens Opvragen" ,"8":") Verwijder een box"  }
#We gooien alle 8 de opties in een dictionary (op deze manier hebben we geen 8 print statements nodig)




def runProgramma():
    print("     W E L K O M")
    for optie in opties:
        print(optie,opties[optie])

    keuze = int(input("Uw kan een optie selecteren door het juiste NUMMER in te geven \n"))
    #We vragen de gebruiker welke optie ze willen uitvoeren


    if keuze == 1:  #-------------------------------------------------------------------------------------------Keuze 1
        print("1) Wilt u een Win10 host voor een 'developper' of")
        print("2) voor een 'network engineer'?")
    
        subkeuze = int(input("Geef weer uw keuze op in NUMMER vorm (1 of 2) "))
        if subkeuze == 1:
            #voer een extern script uit voor het opstellen van de developer box
            try:
                stream = open("Win_10_Developer.py")# SCRIPT
                script = stream.read()
                exec(script)
            except NameError:
                print("de nodige file ontbreekt")

        
        elif subkeuze == 2:
            #voer een extern script uit voor het opstellen van een network engineer box
            try:
                stream = open("Win_10_Engineer.py")# SCRIPT
                script = stream.read()
                exec(script)
            except NameError:
                print("de nodige file ontbreekt")
                
        
        else:
            #print("uw keuze is niet valid. Run het programma opnieuw als u het nog eens wil proberen")
            raise WrongInput("U hebt de verkeerd input opgegeven, de input die u opgaf is niet geldig")




    elif keuze == 2: #-------------------------------------------------------------------------------------------Keuze 2
        print("1) Wilt u een Linux host voor een 'developper' of")
        print("2) voor een 'network engineer'?")
    
        subkeuze = int(input("Geef weer uw keuze op in NUMMER vorm (1 of 2) "))
        if subkeuze == 1:
            #voer een extern script uit voor het opstellen van de developer box
            try:
                stream = open("test.py") #SCRIPT
                script = stream.read()
                exec(script)
            except NameError:
                print("de nodige file ontbreekt")
        
        elif subkeuze == 2:
            #voer een extern script uit voor het opstellen van een network engineer box
            try:
                stream = open("test.py") #SCRIPT
                script = stream.read()
                exec(script)
            except NameError:
                print("de nodige file ontbreekt")

                
        else:
            #print("uw keuze is niet valid. Run het programma opnieuw als u het nog eens wil proberen")
            raise WrongInput()
        

    elif keuze == 3:  #-------------------------------------------------------------------------------------------Keuze 3
        print("1) DHCP only box")
        print("2) AD + DNS only box")
        print("3) AD + DHCP + DNS box")

        subkeuze = int(input("Geef weer uw keuze op in NUMMER vorm (1, 2 of 3) "))
        if subkeuze == 1:
            #voer een extern script uit voor het opstellen van de DHCP only box
           try:
                stream = open("Win_10_Server_DHCP.py")# SCRIPT
                script = stream.read()
                exec(script)
            except NameError:
                print("de nodige file ontbreekt")

         
        elif subkeuze == 2:
            #voer een extern script uit voor het opstellen van een AD + DNS only box
            try:
                stream = open("Win_10_Server_AD_DNS.py") #SCRIPT
                script = stream.read()
                exec(script)
            except NameError:
                print("de nodige file ontbreekt")

        
        elif subkeuze == 3:
            #voer een extern script uit voor het opstellen van server met AD + DHCP + DNS box
            try:
                stream = open("Win_10_Server_AD_DNS_DHCP.py") #SCRIPT
                script = stream.read()
                exec(script)
            except NameError:
                print("de nodige file ontbreekt")
        
        else:
            #print("uw keuze is niet valid. Run het programma opnieuw als u het nog eens wil proberen")
            raise WrongInput()
        

    elif keuze == 4:  #-------------------------------------------------------------------------------------------Keuze 4
        #voer een extern script uit dat een vyos router aanmaakt?????
            try:
                stream = open("test.py") #SCRIPT
                script = stream.read()
                exec(script)
            except NameError:
                print("de nodige file ontbreekt")

    

    elif keuze == 5:  #-------------------------------------------------------------------------------------------Keuze 5
        #voer een extern script uit dat een webserver met LAMP installatie aanmaakt
            try:
                stream = open("test.py") #SCRIPT
                script = stream.read()
                exec(script)
            except NameError:
                print("de nodige file ontbreekt")
                

    elif keuze == 6:  #-------------------------------------------------------------------------------------------Keuze 6
        #voer een extern script uit dat de volledige configuratie opsteld
            try:
                stream = open("test.py") #SCRIPT
                script = stream.read()
                exec(script)
            except NameError:
                print("de nodige file ontbreekt")


                
    elif keuze == 7:  #-------------------------------------------------------------------------------------------Keuze 7
        #Print alle hosts?????????
    
        host = input("Van welke host wenst u de details te zien? (geef de exacte naam op!)")
   


    elif keuze == 8:  #-------------------------------------------------------------------------------------------Keuze 8
        #Print alle hosts??????

        host = input("welke host wenst u te verwijderen? (geef de exacte naam op!)")

        #code om de aangeduide host te verwijderen


    else:
        #print("uw keuze is niet valid. Run het programma opnieuw als u het nog eens wil proberen")
        raise WrongInput()


try:
    os.mkdir("HostOmgeving")
except FileExistsError:
    print("De folder \"HostOmgeving\" werd eerder aangemaakt en is daarom niet opnieuw aangemaakt. \n \n ")
#Hier maken we de parent folder aan, in deze omgeving zullen alle host boxen aangemaakt worden. (Deze map kan maar 1 keer aangemaakt worden)

try:
    runProgramma()
except WrongInput:
    print("Je hebt de verkeerde input in gegeven, je kan enkel een nummer ingeven dit gekoppeld is aan een mogelijke optie...")
    herstarten = int(input("wilt u het programma herstarten? \n 1) JA \n 2) NEE \n"))
    if herstarten == 1:
        print("\n \n \n \n")
        #wat plaats maken dat het nieuwe programma duidelijk kan runnen
        
        runProgramma()
    else:
        print("end")
#We voeren de function 'runProgramma' uit en vangen eventuele fouten/exceptions die gegooid werden op en printen een algemene fout boodschap



