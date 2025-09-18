function ConvertTo-ChronologicalRecords {
    param (
        [string]$SourcePath,
        [string]$DestinationPath
    )
    $content = Get-Content -Path $SourcePath -Raw
    $pattern = '(?s)(## .*?)(?=## |\Z)'
    $matches = [regex]::Matches($content, $pattern)
    $records = @()
    foreach ($match in $matches) {
        $record = $match.Groups[1].Value.Trim()
        if (-not [string]::IsNullOrWhiteSpace($record)) {
            $dateMatch = [regex]::Match($record, '\d{4}-\d{2}-\d{2}')
            if ($dateMatch.Success) {
                $date = [DateTime]$dateMatch.Value
                $records += [PSCustomObject]@{
                    Date = $date
                    Content = $record
                }
            }
        }
    }
    $sortedRecords = $records | Sort-Object Date
    $sortedContent = ($sortedRecords.Content) -join "`n`n"
    Set-Content -Path $DestinationPath -Value $sortedContent.Trim() -NoNewline
}

$sourcePath = "C:/Atari-Monk-Art/productivity/proj-log.md"
$destinationPath = "C:/Atari-Monk-Art/productivity/proj-log-chronological.md"
ConvertTo-ChronologicalRecords -SourcePath $sourcePath -DestinationPath $destinationPath