# Sources and attribution / 来源说明

The workflow and helper code were adapted from the maintainers' own teaching-preparation workflow. Private files, institutional rules, personal presentation preferences, and finished teaching outcomes are not distributed. CELTA guidance is an independently written summary of general principles; no provider handbook, training feedback, or official course material is bundled.

工作流和辅助代码来自维护者自己的备课流程，不发布私人文件、机构规则、个人演示偏好或教学成果。CELTA 指导是对通用原则的独立整理，不打包培训方手册、培训反馈或官方课程材料。

- Official IELTS and Cambridge English references appear in the [source guide](skills/ielts-speaking-workflow/references/sources.md). Their content retains its own rights.
  雅思及 Cambridge English 官方入口见[来源规范](skills/ielts-speaking-workflow/references/sources.md)，资料保留各自权利。
- OpenAI's [skill documentation](https://learn.chatgpt.com/docs/build-skills) informs packaging and invocation. No proprietary presentation skill or host runtime is bundled.
  OpenAI 的[技能文档](https://learn.chatgpt.com/docs/build-skills)用于核对打包和调用方式，不包含专有演示技能或宿主运行库。
- The optional [python-pptx](https://github.com/scanny/python-pptx) dependency is separately installed under its [MIT license](https://github.com/scanny/python-pptx/blob/master/LICENSE); its source is not vendored.
  可选依赖 [python-pptx](https://github.com/scanny/python-pptx) 按其 [MIT 许可](https://github.com/scanny/python-pptx/blob/master/LICENSE) 单独安装，未复制源码入仓库。

## Related projects reviewed / 调研过的相关项目

- [IELTS Obsidian Workflow](https://github.com/3Dclaude/IELTS-Obsidian-Workflow-Skill): candidate practice and Obsidian integration; MIT. Reviewed skill blob: `ee8b7817669f00078cd5bd08adc5c6d043e5b718`.
  面向考生练习及 Obsidian 集成，MIT；核对的技能文件版本如上。
- [K-Teacher Skills](https://github.com/pblsketch/k-teacher-skills): teacher preparation and workflow routing; MIT. Reviewed router blob: `ec5e95fbe821f9206349ebe761e4a31df3add98c`.
  面向教师备课与工作流路由，MIT；核对的路由文件版本如上。

These projects informed comparison of audience and boundaries. Their code, instructions, templates, and installers were not copied. Names and trademarks belong to their respective owners; reference does not imply endorsement.

上述项目用于比较受众与边界，未复制其代码、指令、模板或安装脚本。名称和商标归相应权利人，引用不表示背书。
