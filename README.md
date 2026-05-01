# Econometrica AI Research System

A local Codex workflow system for economics papers targeting Econometrica-level research quality.

The system is designed for human-AI collaboration across the full research lifecycle:

- topic discovery
- tractable model generation
- first-pass derivation
- mathematical verification
- contribution kill tests
- manuscript development
- simulated Econometrica review
- referee-guided revision
- automatic version-control checkpoints

## Files

- `AGENTS.md`: project-level instructions automatically read by Codex.
- `ECONOMETRICA_ORCHESTRATOR.md`: single entry point that routes natural-language requests to the right workflow.
- `ECONOMETRICA_DISCOVERY_WORKFLOW.md`: topic search, model generation, derivation, early kill tests.
- `ECONOMETRICA_VERIFICATION_WORKFLOW.md`: symbolic checks, numerical counterexample search, proof audit, Lean/Python/Mathematica usage.
- `ECONOMETRICA_AI_HUMAN_WORKFLOW.md`: manuscript development, contribution lock, simulated review, revision loop, final readiness.
- `ECONOMETRICA_VERSION_CONTROL.md`: git checkpointing, diffs, branches, commits, rollback safety.
- `TOOLCHAIN_README.md`: local verification toolchain instructions.
- `verify_toolchain.ps1`: quick local toolchain self-test.
- `verification_templates/`: starter templates for counterexample search and Lean lemmas.

## Recommended Use

Copy these files into the root directory of a paper project:

```text
AGENTS.md
ECONOMETRICA_ORCHESTRATOR.md
ECONOMETRICA_DISCOVERY_WORKFLOW.md
ECONOMETRICA_VERIFICATION_WORKFLOW.md
ECONOMETRICA_AI_HUMAN_WORKFLOW.md
ECONOMETRICA_VERSION_CONTROL.md
TOOLCHAIN_README.md
verify_toolchain.ps1
verification_templates/
```

Then open the paper folder in Codex Desktop and use short natural-language commands:

```text
按系统处理：我想讨论一个新的课题，领域大概是平台搜索和广告。
```

```text
按系统处理：这个 idea 是否有 Econometrica 潜力？
```

```text
按系统处理：帮我生成 tractable model，并尝试推导主结论。
```

```text
按系统处理：严格验证 Proposition 1，必要时用 Python、Mathematica 和 Lean。
```

```text
按系统处理：运行一轮 Econometrica 模拟审稿。
```

```text
按系统处理：根据最新审稿意见修改论文。
```

```text
按系统继续。
```

## Design Philosophy

The system does not assume that repeated AI revision converges to Econometrica acceptance. It is designed to expose non-convergence early:

- weak contribution
- non-novel idea
- overly tailored assumptions
- unverified theorem
- hidden proof gap
- poor literature positioning
- manuscript polish without real economic bite

AI should expand the search space, generate and test models, simulate adversarial feedback, maintain logs, and automate mechanical checks. The human should own taste, contribution, assumptions, novelty, target journal, and final go/no-go decisions.

## Local Toolchain

The workflow can use:

- Python with `sympy`, `numpy`, `scipy`, `pandas`, `matplotlib`, `z3-solver`
- Mathematica via `wolframscript`
- Lean 4 / Lake
- Git
- LaTeX

Tool installation is intentionally not committed to this repo. Do not commit `.venv/`, `.tools/`, downloaded installers, caches, or paper-specific outputs.

## GitHub Installation Pattern

For a future paper project, you can either:

1. Copy this repository's workflow files into the paper root.
2. Add this repository as a git submodule and copy/symlink the workflow files.
3. Turn this repository into a Codex skill or plugin later if you want a more formal reusable interface.

The simplest and most robust method is copying the files into each paper root so Codex sees `AGENTS.md` directly.

