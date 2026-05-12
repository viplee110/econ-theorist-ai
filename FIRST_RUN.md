# First-Run Setup

This workflow is designed so an economist can start research work before every
technical tool is configured.

The core research workflow is always available:

- idea discovery
- literature and field profiling
- target journal profiling
- model tournaments
- theorem candidate search
- simulated review
- style calibration
- revision planning

Python, Lean, Mathematica, LaTeX, and Git strengthen verification and project
management. They are useful, but they are not required before the first research
conversation.

## Start In 5 Minutes

1. Download the repository as a ZIP file or clone it with Git.
2. Copy the workflow files into the root folder of your paper project.
3. Open that paper project folder in Codex Desktop or another agent IDE.
4. Ask for a setup check:

```text
Use the system: first-run setup check
```

Small Chinese command example:

```text
按系统处理：初始化检测
```

5. Then initialize the paper project:

```text
Use the system: initialize this paper project
```

## What The Setup Check Does

The setup check detects whether this computer can use:

- Git
- LaTeX
- Python and common scientific packages
- Lean and Lake
- Mathematica / WolframScript

It does not automatically install large tools. It does not change your Windows
PATH or system environment variables. It reports what is available and what is
missing, then explains which workflow abilities are affected.

## Computer Status Versus Paper Status

Toolchain status is computer-level state. By default, `verify_toolchain.ps1
-WriteStatus` writes it to:

```text
C:\Users\<user>\.econ-theorist-ai\toolchain_status.md
```

Paper status is project-level state. Each paper project can have its own:

```text
project_state.md
active_context.md
field_profile.md
target_journal_profile.md
human_decisions.md
```

When you start a second paper, the computer-level toolchain check usually does
not need to be repeated. The new paper still needs its own project
initialization.

## Custom Tool Locations

The default shared verification tool root on Windows is:

```text
C:\Tools\CodexVerification
```

You can use a different location with:

```powershell
$env:CODEX_VERIFICATION_HOME = "D:\Tools\CodexVerification"
.\verify_toolchain.ps1 -WriteStatus
```

For a persistent local preference, create:

```text
C:\Users\<user>\.econ-theorist-ai\config.json
```

Example:

```json
{
  "toolRoot": "D:\\Tools\\CodexVerification",
  "pythonPath": "D:\\Tools\\CodexVerification\\Python312\\python.exe",
  "elanHome": "D:\\Tools\\CodexVerification\\elan",
  "wolframScriptPath": "C:\\Program Files\\Wolfram Research\\Mathematica\\13.0\\wolframscript.exe"
}
```

## If Tools Are Missing

Missing tools do not stop the research workflow.

- Missing Python weakens symbolic checks, numerical examples, and counterexample
  search.
- Missing `z3-solver` weakens SMT-style finite checks.
- Missing Lean affects optional formal verification of compact lemmas.
- Missing Mathematica affects optional symbolic simplification.
- Missing LaTeX affects local manuscript compilation.
- Missing Git affects version-control checkpoints.

The system should explain these limits and continue with the parts of the
research workflow that are available.

## Language Policy

This is an English research system with multilingual command understanding.

You can talk to the assistant in Chinese or English. The assistant should answer
chat messages in the user's language when convenient. Research-facing outputs
remain English by default:

- workflow artifacts
- field and target journal profiles
- human decision logs
- referee reports
- theorem and proof notes
- revision logs
- manuscripts

Chinese is allowed in chat and in a small command trigger list only. Do not write
Chinese into research artifacts unless the user explicitly asks for a separate
Chinese explanatory note outside the manuscript workflow.
