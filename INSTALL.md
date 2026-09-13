# Install into a paper folder

Modified for the original workflow refresh (2026-09-13).

Use a downloaded repository or a local clone:

```powershell
git clone https://github.com/viplee110/econ-theorist-ai.git
```

Copy these seven protocol files and `docs/MIGRATION.md` into the paper
folder, preserving the `docs/` subdirectory so the migration link works:

```text
AGENTS.md
ECONOMETRICA_ORCHESTRATOR.md
ECONOMETRICA_DISCOVERY_WORKFLOW.md
ECONOMETRICA_VERIFICATION_WORKFLOW.md
ECONOMETRICA_AI_HUMAN_WORKFLOW.md
ECONOMETRICA_PANEL_PROTOCOL.md
ECONOMETRICA_VERSION_CONTROL.md
docs/MIGRATION.md
```

Also copy `INSTALL.md`, `FIRST_RUN.md`, `TOOLCHAIN_README.md`, `verify_toolchain.ps1`,
`LICENSE` and `NOTICE` to keep the help links and optional setup check available.
`verification_templates/` is optional. If you want the worked examples, copy
`examples/` and `evals/` together to preserve their links. Maintainer checks run
from the full repository, not a minimal paper installation. The repository README,
design notes and tests need not be loaded into a paper session.

If the paper already has an `AGENTS.md` or customized workflow instructions,
merge them after reviewing the diff. Do not overwrite research-specific
constraints or copy the workflow repository's `.gitignore` over the paper's.
Follow [migration](docs/MIGRATION.md) for an older project.

Open the paper folder in your agent environment and ask for the research task.
For example: "Help me develop this mechanism" or "按系统继续". The root
`AGENTS.md` is the entry point; if your environment does not load it, explicitly
ask the agent to read it. The seven protocol files must all say `Workflow revision: 2026-09`.

For an optional setup check on Windows:

```powershell
.\verify_toolchain.ps1
```

The default check displays capability status. To save it, choose a path:

```powershell
.\verify_toolchain.ps1 -WriteStatus -StatusPath '.\toolchain_status.md'
```

See [toolchain configuration](TOOLCHAIN_README.md) for custom executables.
For another computer, copy the paper together with evidence and decision records,
then check any tools needed there. Local files are not automatically published.
