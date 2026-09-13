# First run

Modified for the original workflow refresh (2026-09-13).

Install the files described in [INSTALL.md](INSTALL.md), open the paper folder,
and describe the research task. You can start from a question, a fixed model,
a theorem, a draft or an existing project.

The agent should identify the immediate uncertainty and perform useful work.
It creates project state only as needed. There is no requirement to populate
profiles, scores, approval forms or empty research files before starting.

If you want a Windows tool check, run:

```powershell
.\verify_toolchain.ps1
```

It detects available capabilities without installing packages. The printed
status distinguishes executable availability from a test actually run.
It does not verify your paper's mathematics. Missing tools limit the affected
operations; they do not block discussion, model development or writing.

Optional saved status:

```powershell
.\verify_toolchain.ps1 -WriteStatus -StatusPath '.\toolchain_status.md'
```

Use [toolchain guidance](TOOLCHAIN_README.md) for non-default locations,
and [migration](docs/MIGRATION.md) when continuing an older paper.
Chat follows your language; notes and manuscripts are English unless requested
otherwise. Existing commands such as "initialize this paper project" and
"continue by the system" remain supported as ordinary task requests.
