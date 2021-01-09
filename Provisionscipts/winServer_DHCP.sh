Param(
[Parameter(Mandatory=$true, position=0)]
[string]$hostname,
[Parameter(Mandatory=$false, position=1)]
[string]$domainname,
[Parameter(Mandatory=$false, position=2)]
[string]$ipAddress
)

Rename-Computer -NewName $hostname -Restart

#ip instellen om DHCP rol te kunnen installeren
New-NetIPAddress -InterfaceIndex 2 -IPAddress $ipAddress -PrefixLength 24
Install-WindowsFeature DHCP -IncludeManagementTools