# Installation Into a Paper Folder

## Option A - Copy Files

Copy these files and folders into the root of your paper project:

```text
AGENTS.md
ECONOMETRICA_ORCHESTRATOR.md
ECONOMETRICA_PANEL_PROTOCOL.md
ECONOMETRICA_DISCOVERY_WORKFLOW.md
ECONOMETRICA_VERIFICATION_WORKFLOW.md
ECONOMETRICA_AI_HUMAN_WORKFLOW.md
ECONOMETRICA_VERSION_CONTROL.md
FIRST_RUN.md
TOOLCHAIN_README.md
verify_toolchain.ps1
verification_templates/
```

Open the paper folder in Codex Desktop. Start with:

```text
Use the system: first-run setup check
```

Small Chinese command example:

```text
按系统处理：初始化检测
```

Then initialize the current paper project:

```text
Use the system: initialize this paper project
```

Other useful entry commands:

```text
Use the system: continue by the system.
Use the system: quickly screen this idea.
Use the system: run a full literature audit.
Use the system: run a full simulated review.
Use the system: what should I do today?
Use the system: export a short working preview draft.
```

The system will ask explicit human-gate questions when important decisions are
needed; you do not need to know the internal stage names.

## Option B - Git Clone and Copy

Clone the workflow repository somewhere stable, then copy the workflow files into each paper project.

```powershell
git clone https://github.com/viplee110/econ-theorist-ai.git
```

Then copy the files listed in Option A.

## Option C - Git Submodule

Inside a paper project:

```powershell
git submodule add https://github.com/viplee110/econ-theorist-ai.git ai_workflow
```

Then copy or symlink `AGENTS.md` into the paper root. Codex reads `AGENTS.md` most reliably when it is at the project root.

## Toolchain

Run this after copying if you want a computer-level toolchain status report:

```powershell
.\verify_toolchain.ps1 -WriteStatus
```

By default the script looks for shared verification tools under:

```text
C:\Tools\CodexVerification
```

To use another location:

```powershell
$env:CODEX_VERIFICATION_HOME = "D:\Tools\CodexVerification"
.\verify_toolchain.ps1 -WriteStatus
```

or:

```powershell
.\verify_toolchain.ps1 -ToolRoot "D:\Tools\CodexVerification" -WriteStatus
```

If Python, Lean, or Mathematica are unavailable, the workflows still work as prompts and checklists, but mathematical verification will be weaker.

## Folder Portability

The paper project is folder-portable. Copy or sync the whole paper project
folder, open it on another computer, run the local toolchain check there, and
continue from the project artifacts.

Use this command after opening the copied folder:

```text
Use the system: continue by the system.
```

Copy the whole folder, not just the manuscript. Workflow artifacts tell the
assistant what happened and what is confirmed. Computer-level setup still belongs
to each computer: agent IDE login, Python, LaTeX, Lean, Mathematica, Git, and
local tool paths should be checked locally.

## If You Use Git

Generated research files are saved locally in each paper project folder. They are
not automatically uploaded to GitHub. The workflow works locally even if you
never use Git.

Git is optional for running the workflow. For serious projects, Git checkpoints
are recommended because they let you roll back file versions if something goes
wrong. Folder portability preserves project state; Git checkpoints preserve
recoverable file versions.

Git commits are stored in the project folder's hidden `.git/` directory. They
stay local unless you choose to push them to GitHub or another remote.

If you use GitHub as a backup for a paper project, you may choose which generated
research files to track. Durable research records that are often worth tracking
include:

```text
human_decisions.md
project_state.md
contribution_lock.md
field_profile.md
target_journal_profile.md
literature_evidence_ledger.md
model_tournament.md
absorption_tests.md
generality_ledger.md
risk_register.md
revision_tree.md
revision_log.md
version_log.md
```

Files that usually do not need to be tracked include:

```text
active_context.md
toolchain_status.md
preview_drafts/
style_anchor_notes/
style_anchor_matrix.md
style_pass_plan.md
referee_reports/
verification/
formal/
lean/
large local caches
```

These runtime files are ignored in this workflow template so paper-specific
process files do not accidentally enter the public workflow repository. In your
own paper project, you may choose to track selected durable records if you want
GitHub or another remote to back up the research process.
