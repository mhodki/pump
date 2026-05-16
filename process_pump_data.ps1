$patterns = @(
    "CENTRIFUGAL PUMP",
    "AXIAL FLOW PUMP",
    "MIXED FLOW PUMP",
    "PISTON PUMP",
    "GEAR PUMP",
    "LOBE PUMP",
    "PERISTALTIC PUMP",
    "PROGRESSING CAVITY PUMP",
    "DIAPHRAGM PUMP",
    "METERING PUMP",
    "PROPELLER PUMP",
    "SCREW PUMP",
    "PUMP IMPELLER",
    "PUMP VOLUTE",
    "PUMP CASING",
    "PUMP BEARING",
    "PUMP BASE",
    "PUMP WITH END SUCTION",
    "PUMP WITH SIDE SUCTION",
    "ROTARY POSITIVE DISPLACEMENT PUMP",
    "POSITIVE DISPLACEMENT PUMP",
    "PUMP WITH SPECIFIED FEATURES",
    "PUMP WITH SPECIFIED MOTION",
    "RECIPROCATING PUMP",
    "PUMP CYLINDER",
    "PUMP PISTON",
    "PUMP SHAFT",
    "PUMP WITH SINGLE STAGE"
)

$inputFile = 'c:\Users\00040628\LocalData\GitHub\pump\input.csv'
$outputFile = 'c:\Users\00040628\LocalData\GitHub\pump\pump_class_mappings.txt'

# Read the CSV file
$data = Import-Csv -Path $inputFile

# Create regex pattern for matching
$patternString = '(' + (($patterns | ForEach-Object { [regex]::Escape($_) }) -join '|') + ')'

# Filter and extract matching rows
$output = @()
$data | Where-Object {
    $_.UniqueName -match $patternString
} | ForEach-Object {
    $output += "$($_.URI)|$($_.UniqueNumber)|$($_.UniqueName)|$($_.TextDefinition)"
}

# Save to output file
$output | Set-Content -Path $outputFile

# Report
Write-Output "Total matches: $($output.Count)"
Write-Output "Results saved to: $outputFile"
