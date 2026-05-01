$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Python = Join-Path $Root ".venv\Scripts\python.exe"
$ElanHome = Join-Path $Root ".tools\elan"
$Lean = Join-Path $ElanHome "bin\lean.exe"
$Lake = Join-Path $ElanHome "bin\lake.exe"
$WolframScript = "C:\Program Files\Wolfram Research\Mathematica\13.0\wolframscript.exe"

Write-Host "== Python scientific stack =="
& $Python -c "import sympy as sp, numpy as np, scipy, pandas as pd, z3; x=sp.symbols('x'); print('python_ok'); print('d/dx x^3 =', sp.diff(x**3,x)); print('numpy_sum =', np.array([1,2,3]).sum()); print('scipy =', scipy.__version__); print('pandas =', pd.__version__); print('z3_symbol =', z3.Int('n'))"

Write-Host "`n== Lean toolchain =="
$env:ELAN_HOME = $ElanHome
& $Lean --version
& $Lake --version

Write-Host "`n== Wolfram / Mathematica =="
if (Test-Path $WolframScript) {
  & $WolframScript -code 'Print[$Version]'
  if ($LASTEXITCODE -ne 0) {
    Write-Host "WolframScript was found, but the kernel did not run successfully. Check Mathematica licensing."
  }
} else {
  Write-Host "WolframScript not found at expected path."
}

