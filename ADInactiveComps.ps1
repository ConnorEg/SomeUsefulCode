#this program will find computers that have not been active in quite some time in the Active Directory

$TotalDaysInactive = 60
$TimeVar = (Get-Date).Adddays(-($TotalDaysInactive))
Get-ADComputer -Filter {LastLogonTimeStamp -lt $TimeVar} -ResultPageSize 1600 -resultSetSize $null -Properties Name, OS, AbrevAccName, UniqueName