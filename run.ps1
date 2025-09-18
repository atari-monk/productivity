function Get-LogEntries {
    param([string]$Path)
    return Get-Content -Path $Path -Raw
}

function Parse-LogEntries {
    param([string]$Content)
    $pattern = '(?m)^## (.+?) (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) - (\d{2}:\d{2}) (.+?)$'
    $matches = [regex]::Matches($Content, $pattern)
    $entries = @()
    foreach ($match in $matches) {
        $project = $match.Groups[1].Value.Trim()
        $date = [DateTime]$match.Groups[2].Value
        $startTime = [TimeSpan]::Parse($match.Groups[3].Value)
        $endTime = [TimeSpan]::Parse($match.Groups[4].Value)
        $duration = $match.Groups[5].Value.Trim()
        $entries += [PSCustomObject]@{
            Project = $project
            Date = $date
            StartTime = $startTime
            EndTime = $endTime
            Duration = $duration
            FullEntry = $match.Value
        }
    }
    return $entries
}

function Find-TimeConflicts {
    param([array]$Entries)
    $conflicts = @()
    $groupedEntries = $Entries | Group-Object Date
    foreach ($group in $groupedEntries) {
        $dayEntries = $group.Group | Sort-Object StartTime
        for ($i = 0; $i -lt $dayEntries.Count; $i++) {
            for ($j = $i + 1; $j -lt $dayEntries.Count; $j++) {
                $entry1 = $dayEntries[$i]
                $entry2 = $dayEntries[$j]
                if ($entry1.EndTime -gt $entry2.StartTime) {
                    $conflicts += [PSCustomObject]@{
                        Date = $entry1.Date
                        Entry1 = $entry1
                        Entry2 = $entry2
                        OverlapMinutes = [math]::Round(($entry1.EndTime - $entry2.StartTime).TotalMinutes, 2)
                    }
                } else {
                    break
                }
            }
        }
    }
    return $conflicts
}

$logContent = Get-LogEntries -Path "C:/Atari-Monk-Art/productivity/proj-log.md"
$parsedEntries = Parse-LogEntries -Content $logContent
$timeConflicts = Find-TimeConflicts -Entries $parsedEntries

if ($timeConflicts.Count -eq 0) {
    Write-Host "No time conflicts found."
    exit
}

Write-Host "Found $($timeConflicts.Count) time conflict(s):"
foreach ($conflict in $timeConflicts) {
    Write-Host "Conflict on $($conflict.Date.ToString('yyyy-MM-dd')):"
    Write-Host "  $($conflict.Entry1.Project) $($conflict.Entry1.StartTime.ToString('hh\:mm')) - $($conflict.Entry1.EndTime.ToString('hh\:mm'))"
    Write-Host "  $($conflict.Entry2.Project) $($conflict.Entry2.StartTime.ToString('hh\:mm')) - $($conflict.Entry2.EndTime.ToString('hh\:mm'))"
    Write-Host "  Overlap: $($conflict.OverlapMinutes) minutes"
    Write-Host "---"
}