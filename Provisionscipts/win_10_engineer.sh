scoop bucket add github-gh https://github.com/cli/scoop-gh.git
scoop install gh
powershell

Rename-Computer -NewName computerNaam -DomainCredential domain -Restart
$Path = $env:TEMP; $Installer = "putty-64bit-0.74-installer.msi"; Invoke-WebRequest "https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.74-installer.msi" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
$Path = $env:TEMP; $Installer = "Tftpd64-4.64-setup.exe"; Invoke-WebRequest "https://bitbucket.org/phjounin/tftpd64/downloads/Tftpd64-4.64-setup.exe" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
$Path = $env:TEMP; $Installer = "Firefox Installer"; Invoke-WebRequest "https://www.mozilla.org/nl/firefox/download/thanks/" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
