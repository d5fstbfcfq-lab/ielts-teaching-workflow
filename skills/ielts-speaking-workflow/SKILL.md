---
name: ielts-speaking-workflow
license: MIT
description: "Plan IELTS speaking courses and lessons, organize supplied materials, create slide content or editable PPTX files, and review or revise teaching decks using CELTA-informed methods. Use for teacher preparation and courseware work, rather than acting as a candidate practice partner or an official examiner. / 面向教师的雅思口语备课、材料整理、课件制作与审查修改工作流。"
---

# IELTS Speaking Teaching Workflow / 雅思口语教学工作流

Help a teacher move from their own materials and learning aims to usable lesson materials. Support course planning, individual lessons, deck creation, review, revision, and continuation. Do only the requested branch.

帮助教师根据自己的材料和教学目标完成课程规划、课次设计、课件制作、审查、修改和续做，只执行本次要求的分支。

## Start with the task / 从当前任务开始

1. Reuse the teacher's confirmed context. Identify the task, learner needs, observable aim, available time, source material, intended audience, and requested output. Ask only about gaps that change the result; do not require a new interview when the brief is already sufficient.
   沿用已确认信息，核对任务、学员需求、可观察目标、课时、材料、读者和交付物。只询问影响结果的缺项；资料充分时直接推进。
2. Inspect the tools actually available. Use file creation, editing, rendering, browsing, or transcription only when available and needed. Do not assume a host-specific plugin, paid service, local path, or another skill is installed.
   先检查实际工具能力；按需使用文件生成、编辑、渲染、联网或转写能力，不假定已有特定插件、收费服务、本机路径或其他技能。
3. Read [the workflow](references/workflow.md) for the requested branch. For teaching design or a pedagogical review, also read [CELTA-informed guidance](references/celta.md). For a PPT task, read [quality review](references/quality.md). For exam facts or source handling, read [sources](references/sources.md).
   按当前任务读取[工作流](references/workflow.md)；教学设计或教学审查加读 [CELTA 指导](references/celta.md)，PPT 任务加读[质量检查](references/quality.md)，考试事实与材料来源处理加读[来源规范](references/sources.md)。

## Keep the output honest / 如实说明交付能力

- With file tools: create or edit the requested editable PPTX, inspect the actual saved file, and render it when possible. Report the verification environment and any incomplete checks.
  有文件工具时，制作或编辑所需的可编辑 PPTX，检查实际文件，条件允许时渲染；报告实际验证环境和未完成检查。
- Without file tools: provide the requested plan, slide-by-slide content, or review recommendations as text. Clearly say that a PPTX has not been created or modified.
  无文件工具时，提供教案、逐页内容或审查建议，并明确说明尚未生成或修改 PPTX。
- Without audio or visual access: do not claim to have assessed pronunciation or inspected slide appearance. A transcript supports text analysis; extracted slide text supports content review.
  无音频或视觉访问能力时，不声称已评估发音或检查实际版面。转写文本支持文本分析，提取的幻灯片文字支持内容审查。

## Respect the teacher's choices / 尊重教师的选择

Preserve source questions, references, intended learning scope, and deliberate manual edits. Distinguish official material, teacher-supplied content, adaptations, and AI-authored practice. Explain material changes before revising the agreed teaching content. Follow the teacher's actual approval and file-saving preferences; do not add fixed approval gates or copy a previous teacher's habits into a new project.

保留原题、来源、约定范围和有意的手动调整。区分官方材料、教师材料、改编和 AI 自编练习；实质性改变已约定教学内容前说明变化。遵从教师实际的审批与保存要求，不把其他教师的习惯变成固定流程。

Use natural, level-appropriate spoken English. Choose methods, slide titles, typography, pictures, and layouts for the lesson and the teacher's brief. Avoid enforcing a particular font, a picture on every slide, fixed page titles, a fixed slide count, or one mandatory lesson framework.

英语表达应自然并符合学生水平。根据任务选择教学法、标题、字体、配图和布局，不强制特定字体、每页配图、固定标题、固定页数或单一教学框架。

## Supporting resources / 辅助资源

- [Lesson brief / 课次约定](assets/templates/lesson-brief.md)
- [Materials register / 材料登记](assets/templates/materials-register.md)
- [Slide outline / 逐页提纲](assets/templates/slide-outline.md)
- [Review report / 审查记录](assets/templates/review-report.md)
- Read-only PPTX audit: `scripts/audit_pptx.py`. Its findings are prompts for review, not a teaching score or proof of rendered correctness.
  只读 PPTX 检查：`scripts/audit_pptx.py`。结果是审查线索，不是教学评分，也不能证明渲染正确。
