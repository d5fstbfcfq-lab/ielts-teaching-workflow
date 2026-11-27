# Quality review / 质量检查

Review content, file structure, visual evidence, and teaching design separately. Record what was actually inspected. A clean script report does not establish teaching effectiveness or PowerPoint rendering quality.

分别复核内容、文件结构、视觉证据和教学设计，并记录实际检查范围。脚本零发现不能证明教学效果或 PowerPoint 渲染质量。

## Match checks to impact / 按影响范围检查

Fully check a new deck or a change to the overall structure, theme, or substantial content. For a local change, inspect affected pages and necessary dependencies, such as a model used in later practice, shared layout, media, or reveal sequence. Expand the scope if those checks reveal a wider problem. A broad but inexpensive mechanical scan may still be useful; it does not require re-rendering every unchanged page.

新课件，或整体结构、主题、大量内容变化时完整检查。局部改动检查受影响页及必要依赖，如后续练习引用的示范、共用版式、媒体或揭示顺序；发现更大问题时再扩大范围。成本较低的整套机械扫描仍可有用，但不代表必须重渲染全部未改页面。

Reuse earlier results only where the source and relevant dependencies remain unchanged. Record pages and presentation states actually inspected, the environment, and exclusions. Stop once the requested outcome is verified and no new concern remains; a sample or historical pass must not be reported as current full validation.

仅在来源及相关依赖未变时复用旧结果。记录实际查看的页码、呈现状态、环境与未覆盖项；满足目标且没有新增疑点后结束。抽样或历史通过不能写成本次完整验收。

## Content and sources / 内容与来源

Check source fidelity, question–answer relevance, natural spoken English, suitability for learners, and the distinction between original and adapted material. Confirm that model responses support the intended language or speaking skill. Treat AI estimates as provisional; do not infer pronunciation from a transcript.

核对来源忠实性、题答相关性、口语自然度、水平适配及原文与改编的区别。示范回答应服务于目标语言或口语能力。AI 估计只作参考，不从转写文本推断发音。

For answer frameworks, models, language banks, or substitution, use [speaking support](speaking-support.md) and inspect the actual material:

涉及回答框架、示范、语言库或替换练习时，按[口语支架](speaking-support.md)检查实际材料：

- Do the model and practice reach the agreed outcome, including after a target change? / 示范与练习是否达到约定目标，目标变更后是否同步？
- Can learners turn the structure and support into the intended response? / 学生能否借助结构与支架形成目标回答？
- Do the question, plan, keywords, English sentences, and examples agree in meaning? / 题干、思路、关键词、英文句子与例子是否对应？
- Does language support cover the information needed, and does the demonstrated substitution still answer the question? / 语言支持是否覆盖所需信息，替换结果是否仍回应题目？
- Does each core point have a coherent short model and focused analysis nearby, retaining any needed complete response without low-value repetition? / 核心点是否有邻近的连贯短示范和聚焦解析，保留必要完整回答并减少低增量重复？

Report the affected page or passage and the broken relationship. Compare recorded delivery only when available; otherwise state that it was not checked. These are content judgements, not new guarantees made by the audit script.

报告受影响页码或段落及具体不一致之处；只有实际取得现场资料后才对照教学示范，否则说明未检查。这些属于内容判断，不是机械脚本新增的保证。

## Mechanical file check / 文件机械检查

When Python and `python-pptx` are available, run the bundled script against the actual PPTX:

具备 Python 和 `python-pptx` 时，对实际 PPTX 运行随附脚本：

```text
python audit_pptx.py <deck.pptx> --json <audit.json> --markdown <audit.md>
```

Resolve the script inside this skill's `scripts` directory; the command above uses its filename for readability. In an uploaded ChatGPT bundle, this is an optional local command, not a claim that the script is present or can execute there.

脚本位于本技能的 `scripts` 目录，上方仅为便于阅读使用文件名。ChatGPT 上传文档中的此命令是可选的本地操作说明，不代表脚本已经上传或能够运行。

The script reads the PPTX and optionally writes reports. It does not alter slides. It checks top-level geometry and overlap, estimates text fit, flags explicitly small text, and reports notes, hidden slides/objects, and comments for audience review. Notes or comments are not automatically defects. It does not enforce fonts, slide titles, images on every slide, aspect ratio, classroom timers, or lesson methods.

脚本读取 PPTX，可选输出报告，不修改幻灯片。它检查顶层几何与重叠、估计文本容纳情况、提示显式小字号，并提示备注、隐藏页或对象、批注以便核对读者边界。这些嵌入内容不自动构成缺陷。脚本不强制字体、标题、逐页配图、宽高比、课堂计时或教学法。

`error` identifies a strong structural signal such as meaningful content wholly outside the canvas. `warning` needs visual investigation. `advisory` provides context. Findings use displayed slide order, including reordered decks. Exit code 0 means the audit ran; `--fail-on-error` changes error findings to exit code 1. Input or output failures return 2.

`error` 表示内容完全落在画布外等较强结构信号，`warning` 需要视觉判断，`advisory` 提供检查信息。页码按实际显示顺序计算，包括重排课件。退出码 0 表示检查成功执行；`--fail-on-error` 会在发现 error 时返回 1，输入或输出失败返回 2。

Text fit and overlap are estimates. Theme-inherited fonts, rotated text, nested group geometry, table cell geometry, transparency, animation, pronunciation, and pedagogy require other evidence. Do not turn every bounding-box intersection into a confirmed collision.

文本容纳与重叠只作估计。主题继承字号、旋转文字、组合内几何、表格单元格几何、透明度、动画、发音和教学效果需要其他依据，不把所有边框相交都判为遮挡。

## Visual review / 视觉复核

For a full review, render the deck, inspect its contact sheet, and view every page at a useful size. For a local review, render and inspect affected pages and dependencies. Check clipping, line wrapping, missing glyphs, font substitution, contrast, z-order, image crop, hierarchy, page numbering, and consistency. Recheck corrections and disclose pages not seen.

完整检查时渲染整套课件，查看缩略图并逐页放大；局部检查时渲染并查看受影响页及依赖。核对截断、换行、缺字、字体替换、对比、层次、裁切、层级、页码及一致性；修复后复核，并说明未查看页面。

Use [slide design and presentation](slide-presentation.md) to check diagram meaning, editability, readable connectors, and proximity of analysis to the matching model language. Check teaching usefulness and visual hierarchy, not picture counts. A static preview may show only one display state.

按[页面设计与呈现](slide-presentation.md)检查图示意义、可编辑性、连线可读性及解析与示范的对应距离。判断教学用途与视觉层级，不统计图片凑数；静态预览可能只显示一种呈现状态。

If only text extraction is available, label the work a content review. Do not claim visual approval. Report the actual rendering environment; a third-party preview is distinct from testing in the intended classroom software.

只有文字提取能力时，标为内容审查，不宣称视觉通过。说明实际渲染环境，区分第三方预览与目标课堂软件验证。

## PowerPoint playback / PowerPoint 实际放映

Within the impact scope, verify planned full-display and staged pages in the target PowerPoint slide show, following [the presentation checks](slide-presentation.md). Inspect entry, initial screen, each click group, final content, and returning to the page. Check answer timing, retained support, missing objects, obstruction, and triggers; include diagrams and special media where used.

按影响范围，在目标 PowerPoint 实际放映中验证完整呈现及分步页，遵循[呈现检查](slide-presentation.md)。核对页面进入、首屏、每个单击意义组、最终内容及返回该页的表现，检查答案时机、支架保留、漏显、遮挡及触发，并覆盖涉及的图示和特殊媒体。

Record software/version when known, pages, states, and actual results. PNG/PDF output, XML animation tags, or a successful audit are insufficient to pass this check. Without target PowerPoint access, report native playback as unverified and supply a concise handoff checklist; do not label the deck fully validated. For text-only work, record the plan as awaiting file implementation and playback.

记录实际软件及已知版本、页码、状态与结果。PNG/PDF、XML 动画标签或脚本成功均不足以判定此项通过。无法访问目标 PowerPoint 时，将原生放映记为未验证，提供简短交接检查项，不宣称课件完整验收；纯文本工作标为待文件实现与放映。

## Teaching review / 教学复核

Check the link between aims, input, examples, practice, and feedback. Examine learner workload and speaking opportunities within the available time. Use the agreed audience boundary: preserve necessary student instructions and keep private records out of student-facing material. Do not add fixed stages or remove useful feedback just to satisfy a framework.

核对目标、输入、示范、练习和反馈的关系，判断课时内的负担与表达机会。遵从约定的读者边界，保留必要学生指令，避免公开私密记录。不为套框架强加阶段，也不机械删除有用反馈。

## Actionable findings / 可执行问题记录

For each finding, state the displayed page number, evidence, consequence, recommended change, and confidence or verification limit. Distinguish a defect from a stylistic preference. For a proposed reordering, explain the learning dependency. A review report should identify its source file/version and whether any edits were performed.

每项问题写明实际页码、依据、影响、修改建议及把握或验证限制。区分缺陷与风格偏好；重排建议应解释学习依赖。报告注明源文件或版本，以及是否实际修改。

When findings come from earlier reviews or recordings, apply [feedback evidence](feedback-evidence.md). Keep the original version/location and distinguish reviewer advice from directly verified facts and the current recommendation.

问题来自早期审查或录音录像时，按[反馈证据](feedback-evidence.md)保留原版本与定位，区分评课者建议、直接核实事实及本次建议。

Before delivery, verify that the saved artifact opens and that the review describes that same artifact. Report incomplete checks rather than inventing a passing score.

交付前确认保存文件能打开，报告对应同一成品；如实说明未完成检查，不编造通过分数。
