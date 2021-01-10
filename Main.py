import vagrant, os, shutil, wmi
import subprocess
from netmiko import ConnectHandler






class WrongInput(Exception):
    pass
#We schrijven onze eigen exception
    






#Dit is de classe die het programma zal runnen. Deze classe zal gebruik maken van objecten van de classe vagrantBox en zal hier instanties van gaan aanmaken.---------------Class runProgram
class runProgram:
    def reset(self):
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
                    naam = input("geef deze host een naam. \n :")
                    ip = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")
                    domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")
                    #Opvragen van de nodige gegevens aan de gebruiker
                    
                    vb = vagrantBox(naam,domein,ip,"gusztavvargadr/windows-10","windows","../Provisionscipts/win_10_developer.sh",False)
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()

        
            elif subkeuze == 2:
                #voer een extern script uit voor het opstellen van een network engineer box
                try:
                   naam = input("geef deze host een naam. \n :")
                   ip = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")
                   domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")
                   #Opvragen van de nodige gegevens aan de gebruiker
                    
                   vb = vagrantBox(naam,domein,ip,"gusztavvargadr/windows-10","windows","../Provisionscipts/win_10_engineer.sh",False)
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
                    naam = input("geef deze host een naam. \n :")
                    ip = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")
                    domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")
                    #Opvragen van de nodige gegevens aan de gebruiker
                    
                    vb = vagrantBox(naam,domein,ip,"bento/ubuntu-16.04","linux","../Provisionscipts/ubuntu_developer.sh",False)                
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()
            
            elif subkeuze == 2:
                #voer een extern script uit voor het opstellen van een network engineer box
                try:
                    naam = input("geef deze host een naam. \n :")
                    ip = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")
                    domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")
                    #Opvragen van de nodige gegevens aan de gebruiker
                    
                    vb = vagrantBox(naam,domein,ip,"bento/ubuntu-16.04","linux","../Provisionscipts/ubuntu_engineer.sh",False)
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
                    naam = input("geef deze host een naam. \n :")
                    ip = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")
                    domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")
                    #Opvragen van de nodige gegevens aan de gebruiker
                    
                    vb = vagrantBox(naam,domein,ip,"jacqinthebox/windowsserver2016core","windows","../Provisionscipts/winServer_DHCP.sh",False)
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()
         
            elif subkeuze == 2:
                #voer een extern script uit voor het opstellen van een AD + DNS only box
                try:
                    naam = input("geef deze host een naam. \n :")
                    ip = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")
                    domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")
                    #Opvragen van de nodige gegevens aan de gebruiker
                    
                    vb = vagrantBox(naam,domein,ip,"jacqinthebox/windowsserver2016core","windows","../Provisionscipts/winServer_AD_DNS.sh",False)
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()

        
            elif subkeuze == 3:
                #voer een extern script uit voor het opstellen van server met AD + DHCP + DNS box
                try:
                    naam = input("geef deze host een naam. \n :")
                    ip = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")
                    domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")
                    #Opvragen van de nodige gegevens aan de gebruiker
                    
                    vb = vagrantBox(naam,domein,ip,"jacqinthebox/windowsserver2016core","windows","../Provisionscipts/winServer_DHCP_DNS_AD.sh",False)
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
                    naam = input("geef deze host een naam. \n :")
                    ip = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")
                    domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")
                    #Opvragen van de nodige gegevens aan de gebruiker
                    
                    vb = vagrantBox(naam,domein,ip,"higebu/vyos","linux","../Provisionscipts/vyos.sh",False)
                    vb.SetUp()
                    vb.OmgevingAanmaken()
                    vb.VoegToeAanFile()
                except:
                    raise WrongInput()

    

        elif keuze == 5:  #-------------------------------------------------------------------------------------------Keuze 5
            #voer een extern script uit dat een webserver met LAMP installatie aanmaakt

              naam = input("geef deze host een naam. \n :")
              ip = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")
              domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")
              #Opvragen van de nodige gegevens aan de gebruiker

              vb = vagrantBox(naam,domein,ip,"AntonioD/centos7-server","linux","../Provisionscipts/LAMP_Server.sh",True)
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
            myDic = {}
            #Aanmaken dictionary (hierin zullen we alle hosts uit de hostfile.txt in gaan opslaan als vagrantBox objecten met de naam van deze objecten als key)
            try:
               
                with open("HostOmgeving/Hostfile.txt", "r") as file:
                    print("Dit zijn de namen van alle runnende hosts: \n")
                    
                    for line in file:

                        x = line.split(" ")
                        item = vagrantBox(x[0].split(":")[1],x[4].split(":")[1],x[1].split(":")[1],"",x[2].split(":")[1],"",x[6].split(":")[1])
                        #We maken van elk item in de host file een "vagrantBox" object (dit doen we zodat we straks makkelijker de gegevens kunnen opvragen)

                        key = x[0].split(":")[1]
                        #we gaan de naam van de host gebruiken als key in onze dictionary 
                        
                        myDic[key] = item
                        #We steken het aangemaakte object in een lijst.
                        
                        
                for key in myDic:
                    print(key)
                        #print de namen van alle hosts die in de hostfile staan
                        
            except NameError:
                print("de nodige file ontbreekt")

                
    
            host = input("Van welke host wenst u de details te zien? (geef de exacte naam op!)")
            for box in myDic:
                if(box == host):
                    item = myDic[box]
                    if(item.OS == "windows"):
                    #als we vaststellen dat we de gevraagde box gevonden hebben gaan we de waarde van de key gaan koppelen aan een item.
                    #Dus in item zal een vagrantBox object zitten
                        while True:
                            try:
                                comm = wmi.WMI(item.ipAddress, user=["vagrant"], password=["vagrant"])

                                for x in comm.win32_computersystem():print(x.name)
                                print("\n -----")

                                for x in comm.Win32_ComputerSystem(): print('Total memory: ' +str(round(int(x.TotalPhysicalMemory)/(1024*1024*1024),2))+' GB')
                                for x in comm.win32_operatingsystem(): print ('Free memory: '+str(round(int(x.freephysicalmemory)/(1024*1024),2)) +' GB')
                                for x in comm.win32_LogicalDisk():
                                    try:
                                        size=round(int(x.size)/(1024*1024*1024),2)
                                        size2=round(int(x.freespace)/(1024*1024*1024),2)
                                        print('Total diskspace: '+x.caption + ' '+ str(size)+'GB')
                                        print('Free diskspace: ' +x.caption + ' '+ str(size2)+'GB')
                                        
                                    except:
                                        pass
                                try:
                                    subprocess.run(["wmic cpu get loadpercentage"],capture_output=True)
                                except:
                                    print("Er ging iets fout met het subprocesscomando")
##                                for x in comm.Win32_Process():
##                                    lijst = print("ID: {0}\nHandleCount: {1}\nProcessName: {2}\n".format(process.ProcessId, process.HandleCount, process.name))
##                                with open(pfile,'w') as file:
##                                    file.write(lijst)
##                                    file.close
##                                with open(pfile,'r') as file:
##                                    for line in range(3):
##                                        file.readlines()
##                                        print(line)
##                                        file.close()
                                        
                            except wmi.x_wmi:
                                continue
                            else:
                                break
                    elif(item.OS == "linux"):
                        try:
                            linux = {
                                'device_type': 'linux',
                                'ip': item.ipAddress,
                                'username': 'vagrant',
                                'password': 'vagrant'
                                }
                            try:
                                net_connect = ConnectHandler(**linux)
                                computername = 'hostname'
                                hddinfo = 'df'    
                                ramused= 'free'
                                cpuinfo= 'lscpu'
                                processen= 'top -b -n 1 | head -n 3'

                                output  = net_connect.send_command(computername)
                                output2 = net_connect.send_command(hddinfo)
                                output3 = net_connect.send_command(ramused)
                                output4 = net_connect.send_command(cpuinfo)
                                output5 = net_connect.send_command(processen)
                              
                               
                                print(output)
                                print(output1)
                                print(output2)
                                print(output3)
                                print(output4)
                                print(output5)
                            except:
                                print("Er is iets fout gelopen tijdens het versturen van de commando's naar de linux machine.")
                        except:
                            print("Er trad een foute op bij het aanmaken van de netmiko connectie object")


        elif keuze == 8:  #-------------------------------------------------------------------------------------------Keuze 8
          myDic = {}
            #Aanmaken dictionary
            #(hierin zullen we alle hosts uit de hostfile.txt in gaan opslaan als vagrantBox objecten met de naam van deze objecten als key)
          try:
               
                with open("HostOmgeving/Hostfile.txt", "r") as file:
                    print("Dit zijn de namen van alle runnende hosts: \n")
                    
                    for line in file:

                        x = line.split(" ")
                        item = vagrantBox(x[0].split(":")[1],x[4].split(":")[1],x[1].split(":")[1],"",x[2].split(":")[1],"",x[6].split(":")[1])
                        #We maken van elk item in de host file een "vagrantBox" object
                        #(dit doen we zodat we straks makkelijker de gegevens kunnen opvragen)

                        key = x[0].split(":")[1]
                        #we gaan de naam van de host gebruiken als key in onze dictionary 
                        
                        myDic[key] = item
                        #We steken het aangemaakte object in een lijst.
                        
                        
                for key in myDic:
                    print(key)
                        #print de namen van alle hosts die in de hostfile staan
                        
          except NameError:
              print("de nodige file ontbreekt")

                

          host = input("welke host wenst u te verwijderen? (geef de exacte naam op!)")

            #code om de aangeduide host te verwijderen


        else:
            #print("uw keuze is niet valid. Run het programma opnieuw als u het nog eens wil proberen")
            raise WrongInput()
        



#Deze classe zal gebruikt worden om vagrant boxen aan te maken!-----------------------------------------------------------------------------------------------------------Class vagrantBOX
class vagrantBox:
    def __init__(self, computerNaam,domein,ipAddress,cloudBox,OS,provisionScript,portForwarding):
        self.computerNaam = computerNaam 
        self.domein = domein
        self.ipAddress = ipAddress
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

            vagrantFile.write("config.vm.provision \"shell\", path: \""+self.provisionScript+"\" \n" ", args => [self.computernaam, self.domein, self.ipAddress , Vagrant, Vagrant]")
      

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
                    file.write("Computernaam:"+str(self.computerNaam+" IP:"+self.ipAddress+" OS:"+self.OS+" Boxnaam:"+self.computerNaam+ " domein:"+self.domein+
                                                   " cloudBoxNaam:"+self.cloudBox+" portforwarding:"+(str(self.portForwarding))+"\n"))
        #We voegen als laatste de aangemaakte box toe aan het host bestand (txt)

        os.chdir("..")
        os.chdir("..")
        #we positioneren ons terug in de main folder (zelfde folder waar het main.py script staat)
        #we doen dit zodat alles "klaarstaat" voor als we de code opnieuw willen uitvoeren
        #print(os.getcwd()) zou tonen dat me terug in de main folder staan




#---------------------Het programma begint hier en zal beginnen met de code 1 maal uit te voeren------------------------------------------------------------------------------------------
try:
    rp = runProgram()
    rp.reset()
    rp.run()

 #Onderstaande 4 lijnen zullen vragen of het programma nogmaals uitgevoerd moet worden   
    output = input("rerun program? (1 => YES 2=> NO)")
    while output == "1":

        rp.run()
        output = input("rerun program? (1 => YES 2=> NO)")
        
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



