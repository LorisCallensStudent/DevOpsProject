import vagrant,os
#Script voor de windows server met AD & DNS



def SetUp():
    global computerNaam
    computerNaam = input("geef deze host een naam. \n :")

    global ipAddress
    ipAddress = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")

    global domein
    domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")

    #We vragen de userInput op en dit slaan we op in globale variabelen
    #We werken hier met globale variabelen omdat we dit script remote uitvoeren. Als je een script via "exec()" uitvoerd kan je enkel op deze manier werken


    os.chdir("HostOmgeving")
    #We positioneren ons in de correcte map waar we de host willen aanmaken
    
    try:
        os.mkdir(computerNaam)
    except FileExistsError:
        print("De folder ", computerNaam , " werd eerder aangemaakt en is daarom niet opnieuw aangemaakt. \n \n ")
    #We maken de map aan waarin we de box zullen plaatsten en geven deze map dezelfde naam als de box. Als deze naam als bestaat gooien we een exception!

        
    os.chdir(computerNaam)
    







def OmgevingAanmaken():

    v=vagrant.Vagrant()
    v.init("jacqinthebox/windowsserver2016core")
    #naam van de windows developer box
    vagrantInit = "\t config.vm.box = \"jacqinthebox/windowsserver2016core\" \n"
    #naam van de windows box!


    with open("Vagrantfile","w") as vagrantFile:
        vagrantFile.write("Vagrant.configure(\"2\") do |config| \n")
        vagrantFile.write(vagrantInit)
         #begin vagrant file
     
        networkLine = "\t config.vm.network \"private_network\", ip: \"" +str(ipAddress)+"\" \n"
        print(networkLine)
        x = str(networkLine)
        print(x)
        vagrantFile.write(x)
         #Hier voegen we het ip toe aan de vagrant file

        setComputerName = "\t config.vm.host_name =\""+computerNaam+"\" \n"
        vagrantFile.write(setComputerName)
         #Stelt de hostname van de computer in

        vagrantFile.write('config.vm.provision "shell", path: "../Provisionscipts/winServer_AD_DNS.sh" \n')
         
     

         #hoe stel ik het domein van de pc in????????????????????????????????????????????????????????????????????????????????????????

        vagrantFile.write("\t config.vm.provider \"virtualbox\" do |vb| \n")
        vagrantFile.write("\t \t vb.memory = \"2048\" \n")
        vagrantFile.write("\t \t vb.cpus = 2 \n")
        vagrantFile.write("\t \t vb.gui = true \n")
        vagrantFile.write("\t end \n")
         #hardware instellingen van vagrant file

        vagrantFile.write("end \n")

     
         #afsluiten van de vagrant file



    #v.up()

        
def VoegToeAanFile():
    with open("..\Hostfile.txt", "a") as file:
                file.write("\n Computernaam:"+str(computerNaam+" IP:"+ipAddress+" OS:Windows Boxnaam:"+computerNaam))
    #We voegen als laatste de aangemaakte box toe aan het host bestand (txt)



SetUp()
OmgevingAanmaken()
VoegToeAanFile()
