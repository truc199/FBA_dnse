param(
  [string]$DocPath,
  [string]$LabelsJson,
  [string]$OutJson,
  [string]$PdfPath
)
$ErrorActionPreference = 'Stop'
$labels = Get-Content -Raw -Encoding UTF8 $LabelsJson | ConvertFrom-Json
$want = @{}
foreach ($h in $labels.heads) { $want[[string]$h[1]] = $true }
foreach ($f in $labels.figs) { $want[[string]$f] = $true }
foreach ($t in $labels.tabs) { $want[[string]$t] = $true }

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
$doc = $null
try {
  $doc = $word.Documents.Open($DocPath, $false, $true)
  $doc.Repaginate()
  $pages = @{}
  $bodyStart = -1; $bodyEnd = -1; $execStart = -1; $tocStart = -1
  $n = $doc.Paragraphs.Count
  for ($i = 1; $i -le $n; $i++) {
    $p = $doc.Paragraphs.Item($i)
    $txt = $p.Range.Text
    if ($txt.Length -gt 220) { continue }
    $t = $txt.TrimEnd([char]13, [char]7, ' ')
    if ($t.Contains("`t")) { continue }
    if ($want.ContainsKey($t) -and -not $pages.ContainsKey($t)) {
      $pages[$t] = $p.Range.Information(3)
      $style = $p.Style.NameLocal
      if ($t -eq '1. Introduction') { $bodyStart = $p.Range.Start }
      if ($t -eq 'Appendices') { $bodyEnd = $p.Range.Start }
      if ($t -eq 'Executive summary') { $execStart = $p.Range.End }
    }
    if ($t -eq 'Table of contents' -and $tocStart -lt 0) { $tocStart = $p.Range.Start }
  }
  $bodyWords = $doc.Range($bodyStart, $bodyEnd).ComputeStatistics(0)
  $execWords = $doc.Range($execStart, $tocStart).ComputeStatistics(0)
  $totalPages = $doc.ComputeStatistics(2)
  $out = [ordered]@{ body_words = $bodyWords; exec_words = $execWords; total_pages = $totalPages; pages = $pages }
  $out | ConvertTo-Json -Depth 4 | Out-File -Encoding utf8 $OutJson
  if ($PdfPath) { $doc.ExportAsFixedFormat($PdfPath, 17) }
  "body_words=$bodyWords exec_words=$execWords pages=$totalPages found=$($pages.Count) of $($want.Count)"
}
finally {
  if ($doc -ne $null) { $doc.Close($false) }
  if ($word.Documents.Count -eq 0) { $word.Quit() }
  [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}
