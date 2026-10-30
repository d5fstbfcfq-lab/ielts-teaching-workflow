# Contributing / 参与贡献

Contributions should improve speaking preparation, material handling, courseware, or workflow reliability. The release distributes instructions, prompts, blank templates, and supporting scripts, rather than finished lessons.

贡献应改善口语备课、材料处理、课件或流程可靠性。本项目发布指令、提示词、空白模板和辅助脚本，不建设成品课程库。

1. Describe the issue, intended behavior, actual environment, reproduction steps, and what you verified.
   说明具体问题、预期行为、实际环境、复现步骤和已验证内容。
2. Edit the canonical skill sources and keep Chinese and English aligned. Do not edit only the generated upload document.
   修改技能主来源，保持中英一致，不仅修改生成的上传文档。
3. For script changes, update meaningful file-behavior checks using temporary synthetic files without course content.
   修改脚本时补充有意义的文件行为检查，使用不含课程内容的临时合成文件。
4. Rebuild and run the checks from the repository root:
   在仓库根目录重新生成并检查：

```sh
python scripts/build_chatgpt.py
python scripts/build_chatgpt.py --check
python -m unittest discover -s tests -v
```

Tests need the optional dependency in `requirements.txt`; the bundle generator uses only the standard library.

测试需要 `requirements.txt` 中的可选依赖，上传文档生成器只使用标准库。

Do not submit completed lessons, question banks, commercial materials, provider handbooks, learner recordings or work, personal data, secrets, private local paths, or proprietary plugin source. Use a minimal structural reproduction for file problems. Do not attach private audit reports to public issues.

不提交已完成课程、题库、商业资料、培训方手册、学生录音或作业、个人数据、密钥、私人路径或专有插件源码。文件问题使用最小结构复现，不把私人报告附在公开 Issue 中。

Check third-party licenses before reusing text or code, preserve required notices, and identify its role. Summarize general methodology in your own words; official material does not become MIT-licensed through a reference link.

复用第三方文字或代码前核对许可，保留必要声明并注明用途。用自己的文字整理通用方法，链接到官方资料不等于将其重新按 MIT 授权。

Contributions use the repository's [MIT license](LICENSE), subject to explicitly identified third-party rights. Preserve capability checks and distinguish mechanical, visual, and teaching evidence.

贡献采用仓库的 [MIT 许可](LICENSE)，明确标识的第三方权利除外。保留工具能力检查，区分机械、视觉及教学证据。
