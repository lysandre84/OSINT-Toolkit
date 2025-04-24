#!/usr/bin/env pwsh
<#
=============================================================================================================================================
  /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$   /$$$$$$$$                  /$$ /$$       /$$   /$$    
 /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$|__  $$__/  |__  $$__/                 | $$| $$      |__/  | $$    
| $$  \ $$| $$  \__/  | $$  | $$$$| $$   | $$        | $$  /$$$$$$   /$$$$$$ | $$| $$   /$$ /$$ /$$$$$$  
| $$  | $$|  $$$$$$   | $$  | $$ $$ $$   | $$ /$$$$$$| $$ /$$__  $$ /$$__  $$| $$| $$  /$$/| $$|_  $$_/  
| $$  | $$ \____  $$  | $$  | $$  $$$$   | $$|______/| $$| $$  \ $$| $$  \ $$| $$| $$$$$$/ | $$  | $$    
| $$  | $$ /$$  \ $$  | $$  | $$\\  $$$   | $$        | $$| $$  | $$| $$  | $$| $$| $$_  $$ | $$  | $$ /$$
|  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \\  $$   | $$        | $$|  $$$$$$/|  $$$$$$/| $$| $$ \\  $$| $$  |  $$$$/ 
 \______/  \______/ |______/|__/  \__/   |__/        |__/ \\______/  \______/ |__/|__/  \__/|__/   \___/  
=============================================================================================================================================
.SYNOPSIS
  Collecte des emails publics via Google Search, avec gestion d’erreurs et pagination.
.PARAMETER Domain
  Domaine cible.
.PARAMETER Output
  Fichier CSV de sortie.
#>
param(
    [Parameter(Mandatory)]
    [string]$Domain,
    [string]$Output = "harvester.csv"
)

try {
    $pattern = "\b[A-Za-z0-9._%+-]+@$Domain\b"
    $results = @()
    for ($i=0; $i -lt 5; $i++) {
        $start = $i * 10
        $query = "site:$Domain @email&start=$start"
        $response = Invoke-WebRequest -Uri "https://www.google.com/search?q=$query" -UseBasicParsing
        $matches = $response.Content | Select-String -Pattern $pattern | ForEach-Object { $_.Matches.Value }
        $results += $matches
    }
    $unique = $results | Sort-Object -Unique
    if ($unique) {
        $unique | Export-Csv -Path $Output -NoTypeInformation
        Write-Output "[*] Emails enregistrés dans $Output"
    } else {
        Write-Warning "Aucun email trouvé pour $Domain"
    }
} catch {
    Write-Error "Erreur lors du harvest: $_"
}
