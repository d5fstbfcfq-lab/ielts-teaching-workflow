#!/usr/bin/env python3
"""Build/check the bilingual ChatGPT upload document from the skill's sources."""

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/ielts-speaking-workflow"
OUTPUT = ROOT / "chatgpt/IELTS-speaking-workflow.md"
PARTS = ["SKILL.md", "references/workflow.md", "references/celta.md", "references/quality.md",
         "references/sources.md", "assets/templates/lesson-brief.md", "assets/templates/materials-register.md",
         "assets/templates/slide-outline.md", "assets/templates/review-report.md", "LICENSE"]


def build() -> str:
    sections = [
        "# IELTS Speaking Workflow — ChatGPT upload / 雅思口语工作流上传文档\n\n"
        "Generated from the public skill. Edit the source files and rebuild. / 本文件由公开技能生成，请修改源文件后重新生成。\n\n"
        "Use this as task guidance when the teacher asks. All workflow references and blank templates are included below; "
        "do not request local repository paths to read them. The optional Python audit script is not embedded. "
        "Use actual available tools; without file tools provide text and state that no PPTX was created. "
        "Follow the teacher's requested output language. No completed lesson examples are included.\n\n"
        "教师请求时，将本文作为任务指导。下方已包含全部工作流参考与空白模板，无需索要仓库本机路径。"
        "可选 Python 检查脚本未嵌入。只使用实际可用工具；无文件工具时交付文本，并说明未生成 PPTX。"
        "按教师要求选择输出语言。本文不含已完成的课程实例。"
    ]
    for filename in PARTS:
        text = (SKILL / filename).read_text(encoding="utf-8")
        if filename == "SKILL.md":
            text = re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S)
        if filename == "LICENSE":
            text = "# License / 许可证\n\n" + text
        # Relative file links are not usable inside a single uploaded document.
        text = re.sub(r"\[([^\]]+)\]\((?!https?://|#)[^)]+\)", r"\1", text)
        sections.append(text.strip())
    return "\n\n---\n\n".join(sections) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the generated document is stale")
    args = parser.parse_args()
    expected = build()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != expected:
            parser.exit(1, "ChatGPT document is stale. Run python scripts/build_chatgpt.py\n")
        print("ChatGPT document is current / ChatGPT 文档已同步")
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(expected, encoding="utf-8")
        print(OUTPUT.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
