scoop bucket add github-gh https://github.com/cli/scoop-gh.git
scoop install gh
powershell
$Path = $env:TEMP; $Installer = "chrome_installer.exe"; Invoke-WebRequest "http://dl.google.com/chrome/install/375.126/chrome_installer.exe" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
sudo apt-get update
sudo apt-get install -y git
sudo apt-get install -y firefox
sudo apt-get install -y wget #dit dient om de googlechrome browser te kunnen installeren in ubuntu
wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
sudo apt-get install snapd snapd-xdg-open #dit dient om de snap add te gebruiken voor het installeren van notepad
sudo snap install notepad-plus-plus
sudo apt-get install -y wine #dit dient om de safari browser te kunnen installeren in de ubuntu
mkdir -p ~/build/safari
cd ~/build/safari
wget "http://appldnld.apple.com/Safari5/041-5487.20120509.INU8B/SafariSetup.exe"
wine SafariSetup.exe

sudo hostnamectl set-hostname ubuntudevelopper




