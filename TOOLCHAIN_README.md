# Local Verification Toolchain

This project now contains a local verification toolchain for economics theory work.

## Installed Locally

- Python 3.12.10: `.tools/Python312/python.exe`
- Python virtual environment: `.venv/`
- Python packages:
  - `sympy` for symbolic algebra
  - `numpy` and `scipy` for numerical computation and counterexample search
  - `matplotlib` for plots
  - `pandas` for tables/logs
  - `z3-solver` for SMT-style checks
- Lean 4 via elan:
  - `lean`: `.tools/elan/bin/lean.exe`
  - `lake`: `.tools/elan/bin/lake.exe`

## Mathematica

Mathematica 13.0 is installed locally, and `wolframscript` exists at:

```text
C:\Program Files\Wolfram Research\Mathematica\13.0\wolframscript.exe
```

Codex can run `wolframscript` successfully when the command is allowed to run outside the default sandbox. In the default sandbox, WolframScript may fail because it cannot read the user configuration directory:

```text
C:\Users\viplee110\AppData\Roaming\Wolfram\WolframScript
```

When using Mathematica from Codex, approve the `wolframscript` command if prompted. Mathematica is useful for:

- `FullSimplify`
- `Reduce`
- `Resolve`
- symbolic derivatives
- inequality checks under assumptions
- exact parameter-region analysis

## Quick Self-Test

Run:

```powershell
.\verify_toolchain.ps1
```

Direct Mathematica test:

```powershell
& "C:\Program Files\Wolfram Research\Mathematica\13.0\wolframscript.exe" -code "Print[2+2]"
& "C:\Program Files\Wolfram Research\Mathematica\13.0\wolframscript.exe" -code "Print[FullSimplify[D[x^3,x]]]"
```

## Python Command

Use:

```powershell
.\.venv\Scripts\python.exe
```

Example:

```powershell
.\.venv\Scripts\python.exe -c "import sympy as sp; x=sp.symbols('x'); print(sp.diff(x**3, x))"
```

## Lean Command

Use:

```powershell
$env:ELAN_HOME = "$PWD\.tools\elan"
.\.tools\elan\bin\lean.exe --version
.\.tools\elan\bin\lake.exe --version
```

Lean is installed, but Mathlib has not been downloaded yet. Install Mathlib only when needed, because it can be a large dependency.
