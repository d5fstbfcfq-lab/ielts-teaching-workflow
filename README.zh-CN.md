# 雅思口语教学工作流

[English](README.md)

雅思口语教学工作流：备课、材料、课件与质量检查。面向使用 **Codex 或 ChatGPT** 的雅思口语教师，提供中英双语工作流。

这是我用AI以来总结出的第一个工作流，期待大家给出意见或建议。欢迎通过 [Issues](https://github.com/d5fstbfcfq-lab/ielts-teaching-workflow/issues) 或 Pull Request 交流。

根据教师自己的需求和材料，完成课程规划、课次设计、材料整理、课件制作及审查修改。

第一版聚焦**口语**，覆盖备课与课件工作的完整过程，暂不包含听力、阅读和写作教学工作流。

## 可以做什么

| 工作 | 结果 |
|---|---|
| 课程与课次规划 | 学员需求、能力进阶、可观察目标、范围、CELTA 教学方法及目标到练习的一致性 |
| 材料整理 | 来源与版本登记、改编边界、可用输入及缺项 |
| 课件制作 | 可直接使用的逐页提纲；有合适文件工具时制作可编辑 PPTX |
| 审查与修改 | 具体页码、问题依据、修改建议及实际改动的验证 |
| 反馈分析 | 来源与版本、时间定位，区分建议、教师确认、直接观察与分析 |
| 质量检查 | 语言与教学复核、可选 PPTX 机械检查及条件允许时的渲染检查 |
| 接续工作 | 当前成品、已确认决定、遗留问题及下一步 |

仓库只包含指令、提示词、空白模板和可选脚本，**不包含已完成课程、教学 PPT、题库、学生作业、机构材料或私人教学记录**。字体、标题、配图、页数、教学框架与保存方式由具体任务决定。

## 在 ChatGPT 中使用

1. 下载[中英双语工作流文档](chatgpt/IELTS-speaking-workflow.md)。
2. 上传到普通对话，或加入项目的来源，同时提供你有权使用的材料。
3. 在 [START.md](chatgpt/START.md) 复制所需语言的提示词，填写相关信息并说明任务。

上传文档包含工作流、CELTA 指导、口语支架、反馈证据、质量检查、来源边界和空白模板，无需创建自定义 GPT。

当前对话有合适文件工具时，可要求交付真实的可编辑 PPTX；不支持时，应交付完整逐页内容或审查建议，并明确说明未生成或修改 PPTX。只有文本提取能力时，不能验证实际版面或发音。

## 在 Codex 中使用

将完整的 [ielts-speaking-workflow](skills/ielts-speaking-workflow) 文件夹复制到教学工作目录的 `.agents/skills/`，或个人的 `~/.agents/skills/`。已有同名目录时，先比较再决定如何替换。也可请 `$skill-installer` 从本仓库 GitHub 地址安装 `skills/ielts-speaking-workflow`。

然后调用技能并提供需求：

```text
$ielts-speaking-workflow
```

现行发现方式参见 [OpenAI 技能文档](https://learn.chatgpt.com/docs/build-skills)。所需教学参考和空白模板已包含，不依赖其他教学技能或某个专有演示插件。

本地教学材料放在公开仓库之外，或已忽略的 `local/` 目录中。安装技能不代表授权公开使用过程中生成的文件。

## 可选：检查 PPTX

辅助脚本需要 Python 3.10 或更新版本，单纯阅读工作流不需要 Python。创建虚拟环境：

```sh
python3 -m venv .venv
```

macOS/Linux 使用 `source .venv/bin/activate` 激活；Windows PowerShell 使用 `.venv\Scripts\Activate.ps1`。在仓库根目录运行：

```sh
python -m pip install -r requirements.txt
python skills/ielts-speaking-workflow/scripts/audit_pptx.py local/deck.pptx --markdown local/audit.md --json local/audit.json
```

请自行提供 `local/deck.pptx`，报告上级目录须已存在。脚本只读源文件，检查几何、估计文本容纳、显式小字号及备注、隐藏内容和批注，不强制字体、宽高比、标题、图片数量或教学页序。页码采用实际显示顺序。

小字号提示阈值默认为 14 pt，可用 `--min-font-size` 调整，只作初检线索，并非投影标准。默认成功执行返回 0；使用 `--fail-on-error` 时，发现 error 返回 1；输入或输出失败返回 2。局限与渲染检查见[质量指南](skills/ielts-speaking-workflow/references/quality.md)。

## 维护项目

主来源位于 `skills/ielts-speaking-workflow/`，ChatGPT 上传文档由这些文件生成：

```sh
python scripts/build_chatgpt.py
python scripts/build_chatgpt.py --check
python -m unittest discover -s tests -v
```

测试使用无课程实例的临时合成文件。包检查可发现漏打包的参考、失效的本地链接和过期上传文档。GitHub Actions 会在推送及拉取请求时运行这些检查及文件行为测试。参见[贡献规则](CONTRIBUTING.md)和[发布范围](docs/design/open-source-scope.md)。

## 来源与许可

CELTA 指导为独立整理，不是官方培训课程或评估工具。考试事实须核对现行官方来源，AI 反馈不是官方雅思成绩。参见[来源规范](skills/ielts-speaking-workflow/references/sources.md)和[来源说明](ATTRIBUTION.md)。

仓库原创内容采用 [MIT](LICENSE)，允许商用、修改和再分发，并要求保留相应声明。第三方材料和商标仍受各自权利约束。使用工作流不等于公开自己的课程，也不会自动将成果纳入本仓库。本项目独立于雅思权利方、Cambridge English 和 OpenAI，未获其背书。
