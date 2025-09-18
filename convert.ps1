# Convert-MarkdownSessions.ps1
# Usage: .\Convert-MarkdownSessions.ps1 -InputFile "input.md" -OutputFile "output.md"

param(
    [string]$InputFile,
    [string]$OutputFile
)

# Read the input file
$content = Get-Content -Path $InputFile

$outputLines = @()
$currentProject = ""

foreach ($line in $content) {
    if ($line.StartsWith("# ")) {
        # This is a project header, store the project name
        $currentProject = $line.TrimStart('#').Trim()
    }
    elseif ($line.StartsWith("## Session ")) {
        # This is a session header, reformat it
        $sessionInfo = $line.TrimStart('#').Trim().Replace("Session ", "")
        $newHeader = "## $currentProject $sessionInfo"
        $outputLines += $newHeader
    }
    elseif ($line.Trim() -eq "" -or $line.StartsWith("- ")) {
        # Keep empty lines and bullet points as they are
        $outputLines += $line
    }
}

# Write to output file
$outputLines | Out-File -FilePath $OutputFile -Encoding UTF8

Write-Host "Conversion complete! Output saved to: $OutputFile"