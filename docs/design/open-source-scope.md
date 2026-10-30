# Release scope / 发布范围

## Confirmed outcome / 已确认目标

Provide an IELTS speaking teaching workflow that another teacher can use with their own materials in Codex or ChatGPT, without private project files or machine-specific paths.

提供雅思口语教学工作流，让其他教师在 Codex 或 ChatGPT 中使用自己的材料，无需私人项目文件或特定机器路径。

## First release / 第一版

- Cover course and lesson planning, material organization, PPT creation, review, revision, quality checks, and continuation for speaking.
  覆盖口语课程与课次设计、材料整理、PPT 制作、审查修改、质量检查及续做。
- Provide a self-contained skill plus teacher-readable workflow, prompts, and blank templates.
  同时提供自包含技能及教师可读的工作流、提示词和空白模板。
- Support uploaded documents and copied prompts in ordinary ChatGPT chats and projects; a custom GPT is outside this release.
  ChatGPT 通过上传文档与复制提示词使用，兼顾普通对话和项目；第一版不制作自定义 GPT。
- Publish Chinese and English documentation and use MIT for original repository content.
  公开文档采用中英双语，原创仓库内容采用 MIT。
- Retain independently summarized CELTA-informed principles without imposing one framework.
  保留独立整理的通用 CELTA 原则，不强制单一框架。
- Deliver an editable PPTX when the environment supports file work; otherwise deliver text and state that no file was created or changed.
  环境支持时交付可编辑 PPTX，否则交付文本，并明确未生成或修改文件。

## Exclusions / 排除内容

Do not distribute course examples, completed lessons, teaching outcomes, institutional information, personal habits, original question banks, student data, or private records. Listening, reading, and writing workflows are outside this release. Fonts, every-slide images, fixed titles, slide counts, and approval or saving preferences are not universal requirements.

不发布课程实例、已完成课程、教学成果、机构信息、个人习惯、原始题库、学生数据或私人记录。第一版不覆盖听力、阅读和写作工作流，不把特定字体、逐页配图、固定标题、页数或审批与保存偏好设为统一要求。

## Acceptance / 验收依据

- Teachers can load the skill or upload the bundle without missing private dependencies.
  教师可以加载技能或上传文档，不依赖缺失的私人文件。
- Branches identify inputs, outputs, and review boundaries; review-only work preserves source files.
  各分支明确输入、输出与检查边界，仅审查时保留源文件。
- Both entry points share canonical guidance; the generated document can be checked for drift.
  两种入口共用主来源，可以检查生成文档是否同步。
- The optional audit is read-only, uses displayed slide order, and distinguishes mechanical signals from rendered and teaching evidence.
  可选检查脚本只读文件，使用实际显示页序，区分机械信号与渲染、教学证据。
- The published package contains intended files, valid local references, no private paths or classroom artifacts, and clear MIT and third-party boundaries.
  发布包仅包含预定文件，内部引用有效，无私人路径或课堂成品，并明确 MIT 与第三方权利边界。
