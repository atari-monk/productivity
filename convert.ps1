# Convert duration-only entries to start/end time format and save to different file
function Convert-DurationToTime {
    param(
        [string]$InputFilePath,
        [string]$OutputFilePath
    )
    
    # Read the content from input file
    $content = Get-Content -Path $InputFilePath -Raw
    
    # Pattern to match duration-only sessions
    $pattern = '## Session (\d{4}-\d{2}-\d{2}) (\d{1,2})h (\d{1,2})m'
    
    $matches = [regex]::Matches($content, $pattern)
    Write-Host "Found $($matches.Count) duration-only entries to convert..."
    
    foreach ($match in $matches) {
        $date = $match.Groups[1].Value
        $hours = [int]$match.Groups[2].Value
        $minutes = [int]$match.Groups[3].Value
        
        # Generate random start time between 9 AM and 5 PM (9:00 - 17:00)
        $random = Get-Random -Minimum 0 -Maximum 480 # 8 hours in minutes
        $startHour = 9 + [math]::Floor($random / 60)
        $startMinute = $random % 60
        
        $startTimeFormatted = "{0:00}:{1:00}" -f $startHour, $startMinute
        
        # Calculate end time
        $totalMinutes = $hours * 60 + $minutes
        $endTotalMinutes = $startHour * 60 + $startMinute + $totalMinutes
        $endHour = [math]::Floor($endTotalMinutes / 60)
        $endMinute = $endTotalMinutes % 60
        
        $endTimeFormatted = "{0:00}:{1:00}" -f $endHour, $endMinute
        
        # Format the replacement string
        $replacement = "## Session $date ${startTimeFormatted} - ${endTimeFormatted} ${hours}h ${minutes}m"
        
        # Replace in content
        $content = $content -replace [regex]::Escape($match.Value), $replacement
    }
    
    # Save the modified content to output file
    Set-Content -Path $OutputFilePath -Value $content -NoNewline
    Write-Host "Conversion complete! Output saved to: $OutputFilePath"
    Write-Host "Converted $($matches.Count) duration-only entries"
}

# Usage example:
Convert-DurationToTime -InputFilePath "C:\Atari-Monk-Art\productivity\proj-log.md" -OutputFilePath "C:\Atari-Monk-Art\productivity\proj-log-converted.md"