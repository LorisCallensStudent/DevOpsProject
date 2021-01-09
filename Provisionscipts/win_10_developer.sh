scoop bucket add github-gh https://github.com/cli/scoop-gh.git
scoop install gh
powershell

Rename-Computer -NewName computerNaam -DomainCredential domain -Restart
$Path = $env:TEMP; $Installer = "Git-2.30.0-64-bit.exe"; Invoke-WebRequest "https://github.com/git-for-windows/git/releases/download/v2.30.0.windows.1/Git-2.30.0-64-bit.exe" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
$Path = $env:TEMP; $Installer = "SafariSetup.exe"; Invoke-WebRequest "https://www.techspot.com/downloads/downloadnow/4184/?evp=9e858002577f4aed6ccc88b9f6d63112&file=1" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
$Path = $env:TEMP; $Installer = "Firefox Installer"; Invoke-WebRequest "https://www.mozilla.org/nl/firefox/download/thanks/" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
$Path = $env:TEMP; $Installer = "chrome_installer.exe"; Invoke-WebRequest "http://dl.google.com/chrome/install/375.126/chrome_installer.exe" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
$Path = $env:TEMP; $Installer = "npp.7.9.2.Installer.exe"; Invoke-WebRequest "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9.2/npp.7.9.2.Installer.exe" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer

