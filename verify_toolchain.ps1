param(
  [string]$ToolRoot = $env:CODEX_VERIFICATION_HOME,
  [string]$ConfigPath = "",
  [switch]$WriteStatus,
  [string]$StatusPath = "",
  [switch]$RunSmokeTests
)

# Modified for the original workflow refresh (2026-09-13).
# Capability diagnostics only. No installation or persistent environment changes.
$ErrorActionPreference = "Stop"
$WorkflowRoot = $PSScriptRoot
$Config = $null
if (-not $ConfigPath) {
  $ConfigPath = Join-Path (Join-Path $HOME ".econ-theorist-ai") "config.json"
  $ExplicitConfig = $false
} else {
  $ExplicitConfig = $true
}
if (Test-Path -LiteralPath $ConfigPath -PathType Leaf) {
  try {
    $ConfigText = Get-Content -Raw -Encoding UTF8 -LiteralPath $ConfigPath
    if (-not $ConfigText -or -not $ConfigText.TrimStart().StartsWith("{")) {
      throw "Expected a JSON object."
    }
    $Config = $ConfigText | ConvertFrom-Json
    if ($null -eq $Config -or $Config -isnot [pscustomobject]) {
      throw "Expected a JSON object."
    }
  } catch {
    Write-Error "Cannot read tool configuration '$ConfigPath': $_"
    exit 1
  }
} elseif ($ExplicitConfig) {
  Write-Error "Tool configuration does not exist: $ConfigPath"
  exit 1
}
if (-not $ToolRoot -and $Config -and $Config.toolRoot) {
  $ToolRoot = [string]$Config.toolRoot
}
if (-not $ToolRoot) { $ToolRoot = "C:\Tools\CodexVerification" }

function Find-Tool($Configured, $Candidates, $Names) {
  # An explicit path must not silently fall back to a different installation.
  if ($Configured) {
    if (Test-Path -LiteralPath $Configured -PathType Leaf) { return [string]$Configured }
    return $null
  }
  foreach ($Candidate in $Candidates) {
    if ($Candidate -and (Test-Path -LiteralPath $Candidate -PathType Leaf)) { return $Candidate }
  }
  foreach ($Name in $Names) {
    $Command = Get-Command $Name -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($Command) { return $Command.Source }
  }
  return $null
}

function Invoke-Probe($Executable, $Arguments) {
  try {
    $ProbeOutput = & $Executable @Arguments 2>&1
    return @{ Success = ($LASTEXITCODE -eq 0); Output = ($ProbeOutput -join "`n") }
  } catch {
    return @{ Success = $false; Output = [string]$_ }
  }
}

$Status = [ordered]@{}
$Required = @(
  "AGENTS.md", "ECONOMETRICA_ORCHESTRATOR.md", "ECONOMETRICA_DISCOVERY_WORKFLOW.md",
  "ECONOMETRICA_VERIFICATION_WORKFLOW.md", "ECONOMETRICA_AI_HUMAN_WORKFLOW.md",
  "ECONOMETRICA_PANEL_PROTOCOL.md", "ECONOMETRICA_VERSION_CONTROL.md"
)
$Missing = @($Required | Where-Object { -not (Test-Path -LiteralPath (Join-Path $WorkflowRoot $_) -PathType Leaf) })
$WrongRevision = @($Required | Where-Object {
  $ProtocolPath = Join-Path $WorkflowRoot $_
  (Test-Path -LiteralPath $ProtocolPath -PathType Leaf) -and
    -not (Select-String -LiteralPath $ProtocolPath -Pattern '^Workflow revision: 2026-09$' -Quiet)
})
$WorkflowOK = $Missing.Count -eq 0 -and $WrongRevision.Count -eq 0
$Status["Workflow files"] = if ($WorkflowOK) { "Present, revision 2026-09" } else {
  "Incomplete or mixed revisions; missing: $($Missing -join ', '); wrong revision: $($WrongRevision -join ', ')"
}

$ElanRoot = if ($Config -and $Config.elanHome) { [string]$Config.elanHome } else { Join-Path $ToolRoot 'elan' }
$ToolSpecs = @(
  @{ Name = 'Git'; Config = 'gitPath'; Candidates = @(); Commands = @('git') },
  @{ Name = 'LaTeX'; Config = 'latexPath'; Candidates = @(); Commands = @('latexmk', 'pdflatex', 'xelatex', 'tectonic') },
  @{ Name = 'Python'; Config = 'pythonPath'; Candidates = @((Join-Path $ToolRoot 'Python312\python.exe')); Commands = @('python', 'py') },
  @{ Name = 'Lean'; Config = 'leanPath'; Candidates = @((Join-Path $ElanRoot 'bin\lean.exe')); Commands = @('lean') },
  @{ Name = 'Lake'; Config = 'lakePath'; Candidates = @((Join-Path $ElanRoot 'bin\lake.exe')); Commands = @('lake') },
  @{ Name = 'WolframScript'; Config = 'wolframScriptPath'; Candidates = @(); Commands = @('wolframscript') }
)
$Executables = @{}
foreach ($Spec in $ToolSpecs) {
  $Configured = if ($Config) { $Config.($Spec.Config) } else { $null }
  $Executable = Find-Tool $Configured $Spec.Candidates $Spec.Commands
  $Executables[$Spec.Name] = $Executable
  if (-not $Executable) {
    $Status[$Spec.Name] = if ($Configured) { "Configured path missing ($Configured)" } else { "Not found" }
    continue
  }
  # Do not launch license-dependent kernels or Lean installation shims by default.
  if ($Spec.Name -in @('WolframScript', 'LaTeX', 'Lean', 'Lake')) {
    $Status[$Spec.Name] = "Executable found; execution not checked ($Executable)"
  } else {
    $Probe = Invoke-Probe $Executable @('--version')
    $Status[$Spec.Name] = if ($Probe.Success) { "Version check passed ($Executable)" } else { "Version check failed ($Executable)" }
  }
}

if ($Executables['Python']) {
  $PackageCode = "import importlib.util; names=['sympy','numpy','scipy','pandas','matplotlib','z3']; print(', '.join(n+':'+('found' if importlib.util.find_spec(n) else 'missing') for n in names))"
  $Packages = Invoke-Probe $Executables['Python'] @('-c', $PackageCode)
  $Status['Optional Python packages'] = if ($Packages.Success) { $Packages.Output } else { 'Package discovery failed' }
}
if ($RunSmokeTests -and $Executables['WolframScript']) {
  $Smoke = Invoke-Probe $Executables['WolframScript'] @('-code', 'Print[2+2]')
  $Status['Wolfram arithmetic smoke test'] = if ($Smoke.Success -and $Smoke.Output.Trim() -eq '4') {
    'Passed (2+2 only)'
  } else { 'Failed or license unavailable' }
}

$Lines = @('# Toolchain capability status', '', "Checked: $(Get-Date -Format o)", "Tool root: $ToolRoot", '')
foreach ($Key in $Status.Keys) { $Lines += "${Key}: $($Status[$Key])" }
$Lines += @('', 'These checks establish capability only, not theorem or paper correctness.',
  'Missing tools limit the corresponding operation. Continue research that does not require it.')
$Lines | ForEach-Object { Write-Output $_ }
if ($WriteStatus) {
  if (-not $StatusPath) { $StatusPath = Join-Path $WorkflowRoot 'toolchain_status.md' }
  # The caller chooses the destination; never create a global configuration tree.
  Set-Content -LiteralPath $StatusPath -Value $Lines -Encoding UTF8
  Write-Output "Saved status: $([IO.Path]::GetFullPath($StatusPath))"
}
if (-not $WorkflowOK) { exit 1 }
exit 0
