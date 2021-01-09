Param(
[Parameter(Mandatory=$true, position=0)]
[string]$hostname,
[Parameter(Mandatory=$false, position=1)]
[string]$domainname
)

Rename-Computer -NewName $hostname -Restart

Install-windowsfeature -name AD-Domain-Services -IncludeManagementTools
Install-ADDSForest -DomainName $domainname
Install-WindowsFeature DNS -IncludeManagementTools

#ip instellen om DHCP rol te kunnen installeren
New-NetIPAddress -InterfaceIndex 2 -IPAddress $ipAddress -PrefixLength 24
Install-WindowsFeature DHCP -IncludeManagementTools