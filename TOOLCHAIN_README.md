# Optional verification tools

Modified for the original workflow refresh (2026-09-13).

Tool choice follows the claim. Python, symbolic algebra, finite-game searches,
Lean and Mathematica can support different checks; none is required for every
research activity. LaTeX compiles manuscripts and Git preserves versions.

## Windows capability check

```powershell
.\verify_toolchain.ps1
.\verify_toolchain.ps1 -ToolRoot 'D:\Tools\CodexVerification'
.\verify_toolchain.ps1 -ConfigPath '.\local-tool-config.json'
.\verify_toolchain.ps1 -WriteStatus -StatusPath '.\toolchain_status.md'
```

Default shared root: `C:\Tools\CodexVerification`, overridden by `-ToolRoot`,
`CODEX_VERIFICATION_HOME`, or a config `toolRoot`. Explicit/configured paths are
preferred to PATH lookup. A config may contain:

```json
{
  "toolRoot": "D:\\Tools\\CodexVerification",
  "pythonPath": "D:\\Python\\python.exe",
  "leanPath": "D:\\Tools\\elan\\bin\\lean.exe",
  "lakePath": "D:\\Tools\\elan\\bin\\lake.exe",
  "elanHome": "D:\\Tools\\elan",
  "wolframScriptPath": "D:\\Wolfram\\wolframscript.exe"
}
```

Without `-ConfigPath`, the script reads an existing
`$HOME/.econ-theorist-ai/config.json` if available; it does not create it.
`-WriteStatus` defaults to `toolchain_status.md` beside the script, and
`-StatusPath` overrides that destination. Status writing creates no global
configuration. Review an existing status file before replacing it.

The script installs nothing and does not persist PATH or environment changes.
It reports protocol presence/revision, executable/version checks, discoverable
Python packages and the result of an explicitly requested smoke test. An executable found on PATH
has not necessarily run successfully. A version/import/arithmetic check has not
validated a research claim. Package discovery does not establish that importing
a package or using it will succeed. Lean, Lake and LaTeX are located without
launching them; a Lean launcher can otherwise trigger toolchain setup.

Use `-RunSmokeTests` to request the optional Wolfram `Print[2+2]` check. It may
launch a licensed kernel. Its result concerns that arithmetic operation only;
the script does not compile the Lean example or validate a paper.

## Use capabilities selectively

- If the optional templates/examples were copied, use Python 3.8 or later;
  the scripts and maintainer checks need only the standard library.
  Optional `sympy`, `numpy`, `scipy`, `pandas`,
  `matplotlib` and `z3-solver` support project-specific checks.
- For symbolic algebra, record assumptions and inspect exceptional cases.
  Numeric searches should include relevant boundaries and failure cases; a
  search that finds no counterexample does not prove a theorem.
- The optional Lean template is a compiler smoke test. Substantial Lean work may
  need a separate Mathlib project and suitable versions; configure those only
  when the claim warrants formalization. Record the exact theorem checked.
- Mathematica is optional and machine-specific. Use a configured executable
  and an available license; do not assume the maintainer's installation exists.
- Keep large toolchains and caches outside paper folders when practical. Keep
  source, proofs, environments needed for reproduction and exact outputs with
  the paper or in a documented reproducible location.

See [Verification](ECONOMETRICA_VERIFICATION_WORKFLOW.md) for evidence standards.
