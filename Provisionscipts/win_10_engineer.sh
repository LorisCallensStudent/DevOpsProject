scoop bucket add github-gh https://github.com/cli/scoop-gh.git
scoop install gh
powershell
Param(
[Parameter(Mandatory=$true, position=0)]
[string]$hostname,
[Parameter(Mandatory=$false, position=1)]
[string]$domainname,
[Parameter(Mandatory=$false, position=3)]
[string]$gebruiker,
[Parameter(Mandatory=$false, position=4)]
[string]$wachtwoord
)



$joinCred = New-Object pscredential -ArgumentList ([pscustomobject]@{
    UserName = $gebruiker
    Password = (ConvertTo-SecureString -String $wachtwoord -AsPlainText -Force)[0]
})
Add-Computer -Domain $domainname -Options UnsecuredJoin,PasswordPass -Credential $joinCred
Rename-Computer -NewName $hostname -Restart

$Path = $env:TEMP; $Installer = "putty-64bit-0.74-installer.msi"; Invoke-WebRequest "https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.74-installer.msi" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
$Path = $env:TEMP; $Installer = "Tftpd64-4.64-setup.exe"; Invoke-WebRequest "https://bitbucket.org/phjounin/tftpd64/downloads/Tftpd64-4.64-setup.exe" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
$Path = $env:TEMP; $Installer = "Firefox Installer.exe"; Invoke-WebRequest "https://www.mozilla.org/nl/firefox/download/thanks/" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer

