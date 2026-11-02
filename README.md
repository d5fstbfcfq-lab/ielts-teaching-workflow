# IELTS Speaking Teaching Workflow

[简体中文](README.zh-CN.md)

Bilingual IELTS speaking teaching workflow for Codex and ChatGPT: planning, materials, slides, review and quality checks.

This is the first workflow I've put together since I started using AI. Feedback and suggestions are welcome through [Issues](https://github.com/d5fstbfcfq-lab/ielts-teaching-workflow/issues) or a pull request.

Use your own brief and materials to plan courses and lessons, organize sources, create slides, and review or revise teaching decks.

The first release focuses on **speaking** and covers the full preparation and courseware process. Listening, reading, and writing teaching workflows are outside this release.

## What it covers

| Work | Result |
|---|---|
| Course and lesson planning | Learner needs, progression, observable outcomes, scope, CELTA-informed methods, and aim-to-practice alignment |
| Material organization | Source/version register, adaptation boundaries, usable input, and gaps |
| Slide creation | A usable slide outline; an editable PPTX when the host has suitable file tools |
| Review and revision | Displayed page numbers, evidence, recommendations, and verified changes |
| Feedback analysis | Source/version and time references; separate advice, teacher decisions, observations, and analysis |
| Quality checks | Language and teaching review, optional mechanical PPTX checks, and rendered inspection when available |
| Continuation | Current artifact, decisions, unresolved items, and next step |

The repository contains instructions, prompts, blank templates, and an optional audit script. It contains **no completed lessons, teaching decks, question banks, student work, institutional material, or private teaching records**. Fonts, titles, images, page counts, frameworks, and saving preferences are chosen for each task.

## ChatGPT quick start

1. Download [the bilingual workflow document](chatgpt/IELTS-speaking-workflow.md).
2. Upload it to a regular chat or add it to a project's sources, alongside materials you are entitled to use.
3. Copy the English or Chinese prompt from [START.md](chatgpt/START.md), fill the relevant fields, and describe your task.

The upload document includes the workflow, CELTA-informed guidance, speaking support, feedback evidence, quality criteria, source boundaries, and blank templates. No custom GPT is required.

When the chat has suitable file tools, request the actual editable PPTX. Otherwise it should provide complete slide content or review recommendations and state that no PPTX was created or changed. Text extraction alone cannot verify slide appearance or pronunciation.

## Codex quick start

Copy the complete [ielts-speaking-workflow](skills/ielts-speaking-workflow) folder into `.agents/skills/` in your teaching workspace, or `~/.agents/skills/` for personal use. Compare any existing same-name folder before replacing it. You can also ask `$skill-installer` to install `skills/ielts-speaking-workflow` from this repository's GitHub URL.

Invoke the skill and provide your brief:

```text
$ielts-speaking-workflow
```

See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills) for current discovery behavior. All teaching references and blank templates are included; another teaching skill or proprietary presentation plugin is not required.

Keep local teaching materials outside the public checkout or under the ignored `local/` directory. Installing the skill does not authorize publishing files created with it.

## Optional PPTX audit

Helper scripts require Python 3.10 or newer; reading the workflow does not require Python. Create a virtual environment:

```sh
python3 -m venv .venv
```

Activate it with `source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\Activate.ps1` in Windows PowerShell. From the repository root:

```sh
python -m pip install -r requirements.txt
python skills/ielts-speaking-workflow/scripts/audit_pptx.py local/deck.pptx --markdown local/audit.md --json local/audit.json
```

Supply your own `local/deck.pptx`; report parent directories must exist. The audit reads the source without changing it. It flags geometry, estimated text fit, explicitly small text, and embedded notes/hidden content/comments. It imposes no font, aspect ratio, title, picture-count, or lesson-sequence rule. Findings use displayed page order.

The small-text advisory threshold defaults to 14 pt; change it with `--min-font-size`. This is a heuristic, not a projection standard. A successful audit returns 0; `--fail-on-error` returns 1 for error findings. Invalid input/output returns 2. See [quality review](skills/ielts-speaking-workflow/references/quality.md) for limitations and rendered checks.

## Maintain the package

The canonical sources are in `skills/ielts-speaking-workflow/`. Rebuild the ChatGPT upload document from them:

```sh
python scripts/build_chatgpt.py
python scripts/build_chatgpt.py --check
python -m unittest discover -s tests -v
```

Tests use temporary synthetic files containing no course examples. Package checks detect missing bundled references, broken local links, and stale uploads. GitHub Actions runs these and the file-behavior tests on pushes and pull requests. See [contributing](CONTRIBUTING.md) and [release scope](docs/design/open-source-scope.md).

## Sources and license

CELTA-informed guidance is an independent summary, not an official training course or assessment instrument. Verify exam claims against current official sources; AI feedback is not an official IELTS score. See [sources](skills/ielts-speaking-workflow/references/sources.md) and [attribution](ATTRIBUTION.md).

Original repository content uses [MIT](LICENSE), permitting commercial use, modification, and redistribution with the required notice. Third-party materials and trademarks retain their own rights. Using the workflow does not automatically publish your lessons or make them part of this repository. The project is independent and is not endorsed by IELTS owners, Cambridge English, or OpenAI.
