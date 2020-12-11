import vagrant,os, shutil





class WrongInput(Exception):
    pass
#We schrijven onze eigen exception
    






#Dit is de classe die het programma zal runnen. Deze classe zal gebruik maken van objecten van de classe vagrantBox en zal hier instanties van gaan aanmaken.---------------Class runProgram
class runProgram:
    def __init__(self):
        try:
            shutil.rmtree("HostOmgeving")
            os.mkdir("HostOmgeving")
        except FileExistsError:
            print("De folder \"HostOmgeving\" werd eerder aangemaakt en is daarom niet opnieuw aangemaakt. \n \n ")
            #Hier maken we de parent folder aan, in deze omgeving zullen alle host boxen aangemaakt worden. (Deze map kan maar 1 keer aangemaakt worden)
            

    
    def run(self):

        opties = {"1":") Windows 10 host" ,"2":") Linux Ubuntu host" ,"3":") Windows Server" ,"4":") Vyos router" ,"5":") Webserver" ,"6":") Volledige Omgeving" ,"7":") Gegevens Opvragen" ,"8":") Verwijder een box"  }
        #We gooien alle 8 de opties in een dictionary (op deze manier hebben we geen 8 print statements nodig)

        print("     W E L K O M")
        for optie in opties:
            print(optie,opties[optie])
        #afprinten van het keuzen menu

            
        keuze = int(input("Uw kan een optie selecteren door het juiste NUMMER in te geven \n"))
        #We vragen de gebruiker welke optie ze willen uitvoeren


        if keuze == 1:  #-------------------------------------------------------------------------------------------Keuze 1
            print("1) Wilt u een Win10 host voor een 'developper' of")
            print("2) voor een 'network engineer'?")
    
            subkeuze = int(input("Geef weer uw keuze op in NUMMER vorm (1 of 2) "))
            if subkeuze == 1:
                #voer een extern script uit voor het opstellen van de developer box
                try:
                    vb = vagrantBox("","","","gusztavvargadr/windows-10","windows","../Provisionscipts/win_10_developer.sh",False)
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()

        
            elif subkeuze == 2:
                #voer een extern script uit voor het opstellen van een network engineer box
                try:
                   vb = vagrantBox("","","","gusztavvargadr/windows-10","windows","../Provisionscipts/win_10_engineer.sh",False)
                   vb.SetUp()
                   vb.OmgevingAanmaken()
                   vb.VoegToeAanFile()
                except:
                    raise WrongInput()
                
        
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
                    vb = vagrantBox("","","","bento/ubuntu-16.04","linux","../Provisionscipts/ubuntu_developer.sh",False)
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()
            
            elif subkeuze == 2:
                #voer een extern script uit voor het opstellen van een network engineer box
                try:
                    vb = vagrantBox("","","","bento/ubuntu-16.04","linux","../Provisionscipts/ubuntu_engineer.sh",False)
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()

                
            else:
                #print("uw keuze is niet valid. Run het programma opnieuw als u het nog eens wil proberen")
                raise WrongInput()
        

        elif keuze == 3:  #-------------------------------------------------------------------------------------------Keuze 3
            print("1) DHCP only box")
            print("2) AD + DNS only box")
            print("3) AD + DHCP + DNS box")

            subkeuze = int(input("Geef weer uw keuze op in NUMMER vorm (1, 2 of 3) "))
            if subkeuze == 1:
                #voer een extern script uit voor het opstellen van een network engineer box
                try:
                    vb = vagrantBox("","","","jacqinthebox/windowsserver2016core","windowsserver","../Provisionscipts/winServer_DHCP.sh",False)
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()
         
            elif subkeuze == 2:
                #voer een extern script uit voor het opstellen van een AD + DNS only box
                try:
                    vb = vagrantBox("","","","jacqinthebox/windowsserver2016core","windowsserver","../Provisionscipts/winServer_AD_DNS.sh",False)
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()

        
            elif subkeuze == 3:
                #voer een extern script uit voor het opstellen van server met AD + DHCP + DNS box
                try:
                    vb = vagrantBox("","","","jacqinthebox/windowsserver2016core","windowsserver","../Provisionscipts/winServer_DHCP_DNS_AD.sh",False)
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()
        
            else:
                #print("uw keuze is niet valid. Run het programma opnieuw als u het nog eens wil proberen")
                raise WrongInput()
        

        elif keuze == 4:  #-------------------------------------------------------------------------------------------Keuze 4
            #voer een extern script uit dat een vyos router aanmaakt?????
                try:
                    vb = vagrantBox("","","","higebu/vyos","linux router","../Provisionscipts/vyos.sh",False)
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()

    

        elif keuze == 5:  #-------------------------------------------------------------------------------------------Keuze 5
            #voer een extern script uit dat een webserver met LAMP installatie aanmaakt
        
              vb = vagrantBox("","","","AntonioD/centos7-server","linuxServer","../Provisionscipts/LAMP_Server.sh",True)
              vb.SetUp()
              vb.OmgevingAanmaken()
              vb.VoegToeAanFile()
      

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


#Deze classe zal gebruikt worden om vagrant boxen aan te maken!-----------------------------------------------------------------------------------------------------------Class vagrantBOX
class vagrantBox:
    def __init__(self, computerNaam,domein,ipAddress,cloudBox,OS,provisionScript,portForwarding):
        self.computerNaam =  input("geef deze host een naam. \n :")
        self.domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")
        self.ipAddress = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")
        self.cloudBox = cloudBox
        self.OS = OS
        self.provisionScript = provisionScript
        self.portForwarding=portForwarding
        
    def SetUp(self):
        os.chdir("HostOmgeving")
        #We positioneren ons in de correcte map waar we de host willen aanmaken
    
        try:
            os.mkdir(self.computerNaam)
        except FileExistsError:
            print("De folder ", self.computerNaam , " werd eerder aangemaakt en is daarom niet opnieuw aangemaakt. \n \n ")
            herstarten = int(input("wilt u het programma herstarten? \n 1) JA \n 2) NEE \n"))
            if herstarten == 1:
                print("\n \n \n \n")
                #wat plaats maken dat het nieuwe programma duidelijk kan runnen
        
                herstart = runProgramma()
                herstart.run()
        #We maken de map aan waarin we de box zullen plaatsten en geven deze map dezelfde naam als de box. Als deze naam als bestaat gooien we een exception en vragen we of 
                # ze het programma opnieuw wil runnen!

        
        os.chdir(self.computerNaam)
    

    def OmgevingAanmaken(self):

        v=vagrant.Vagrant()
        v.init(self.cloudBox)
        #naam van de windows developer box
        vagrantInit = "\t config.vm.box = \""+self.cloudBox+"\" \n"
        #naam van de windows box!


        with open("Vagrantfile","w") as vagrantFile:
            vagrantFile.write("Vagrant.configure(\"2\") do |config| \n")
            vagrantFile.write(vagrantInit)
             #begin vagrant file
     
            networkLine = "\t config.vm.network \"private_network\", ip: \"" +str(self.ipAddress)+"\" \n"
            print(networkLine)
            x = str(networkLine)
            print(x)
            vagrantFile.write(x)
             #Hier voegen we het ip toe aan de vagrant file

            setComputerName = "\t config.vm.host_name =\""+self.computerNaam+"\" \n"
            vagrantFile.write(setComputerName)
             #Stelt de hostname van de computer in

            vagrantFile.write("config.vm.provision \"shell\", path: \""+self.provisionScript+"\" \n")
      

            vagrantFile.write("\t config.vm.provider \"virtualbox\" do |vb| \n")
            vagrantFile.write("\t \t vb.memory = \"2048\" \n")
            vagrantFile.write("\t \t vb.cpus = 2 \n")
            vagrantFile.write("\t \t vb.gui = true \n")
            vagrantFile.write("\t end \n")
            #hardware instellingen van vagrant file

            vagrantFile.write("end \n")

     
            #afsluiten van de vagrant file



        #v.up()

        
    def VoegToeAanFile(self):
        with open("..\Hostfile.txt", "a") as file:
                    file.write("\n Computernaam:"+str(self.computerNaam+" IP:"+self.ipAddress+" OS:"+self.OS+" Boxnaam:"+self.computerNaam))
        #We voegen als laatste de aangemaakte box toe aan het host bestand (txt)





try:
    rp = runProgram()
    rp.run()
    
except WrongInput:
    print("Je hebt de verkeerde input in gegeven, je kan enkel een nummer ingeven dit gekoppeld is aan een mogelijke  else")
    herstarten = int(input("wilt u het programma herstarten? \n 1) JA \n 2) NEE \n"))
    if herstarten == 1:
        print("\n \n \n \n")
        #wat plaats maken dat het nieuwe programma duidelijk kan runnen
        herstart = runProgram()
        herstart.run()
    else:
        print("end")

#We voeren de function 'runProgramma' uit en vangen eventuele fouten/exceptions die gegooid werden op en printen een algemene fout boodschap



