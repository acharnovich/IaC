# Place this file in a jenkins pipeline for users to restart a Windows service without logging into the server
powershell -Command "Start-Process PowerShell -Verb RunAs"
$computerName = $($env:Hosts)
$serviceName = "Automation Anywhere Bot Agent"
echo $computerName
# Stop the service on the remote computer
Invoke-Command -ComputerName $computerName -ScriptBlock {
    param($serviceName)
    Stop-Service -Name $serviceName
} -ArgumentList $serviceName

# Wait for the service to stop
while((Get-Service -ComputerName $computerName -Name $serviceName).Status -ne "Stopped"){
    Write-Host "Waiting for service to stop..."
    Start-Sleep -Seconds 1
}

# Start the service on the remote computer
Invoke-Command -ComputerName $computerName -ScriptBlock {
    param($serviceName)
    Start-Service -Name $serviceName
} -ArgumentList $serviceName

# Wait for the service to start
while((Get-Service -ComputerName $computerName -Name $serviceName).Status -ne "Running"){
    Write-Host "Waiting for service to start..."
    Start-Sleep -Seconds 1
}

Write-Host "Service on $computerName has been restarted."
