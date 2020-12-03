import vagrant,os
#Script voor de windows 10 developer host

computerNaam = input("geef deze host een naam. \n :")

ipAddress = input("geef deze host een IPv4 address. In de vorm van x.x.x.x (x zijn enkel gehele getallen) \n :")

domein = input("geef deze host een domein naam mee (dit is optioneel) \n :")








os.chdir("HostOmgeving")
#we positioneren ons in de HostOmgeving file

try:
    os.mkdir(computerNaam)
except FileExistsError:
    print("De folder ", computerNaam , " werd eerder aangemaakt en is daarom niet opnieuw aangemaakt. \n \n ")
#Hier maken we de parent folder aan, in deze omgeving zullen alle host boxen aangemaakt worden. (Deze map kan maar 1 keer aangemaakt worden)


def OmgevingAanmaken():
    os.chdir(computerNaam)
    v=vagrant.Vagrant()

    v.init("gusztavvargadr/windows-10")
    #naam van de windows developer box
    vagrantInit = "\t config.vm.box = \"gusztavvargadr/windows-10\" \n"
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
         #Stelt de hostname van de computer is

        vagrantFile.write('  config.vm.provision "shell", path: "../Provisionscipts/win_10_engineer.sh"\n')
         #Pad aanpassen + sh script schrijven 
     

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


def VoegToeAanHostFile():
   
    #pad aanpassen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    with open("../HostOmgeving/Hostfile.txt", "a") as file:
            file.write("\n Computernaam:"+str(computerNaam+" IP:"+ipAddress+" OS:windows10 Boxnaam:"+computerNaam))

VoegToeAanHostFile()

