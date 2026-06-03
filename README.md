# ai-meetup-kit

这是一个用于线下 AI 交流会的轻量 Flask 项目，主题是“普通人如何用 Codex 把想法变成工具”。

项目适合用来做现场演示：从一个普通人的真实想法出发，拆成清楚需求，再让 Codex 按阶段完成页面、内容、检查和迭代。它不依赖外部 API，也不需要 OpenAI API 或 Sora API 才能本地运行。

## 项目用途

- 展示一个线下 AI 交流会的活动首页、议程页、报名页和 Codex 教学页。
- 帮助参与者理解 AI Agent 的工作方式：先说清目标，再拆分任务，再检查结果。
- 作为 Codex 多 Agent 协作的练习项目：Content Agent 负责文案和教学内容，Frontend Agent 可以继续优化页面体验，Backend Agent 可以继续完善报名和数据处理。
- 给不会编程的用户一个可观察的示例：AI 可以协助做工具，但仍然需要人来提出清楚需求和验收结果。

## 本地运行

先安装依赖：

```powershell
py -m pip install -r requirements.txt
```

启动项目：

```powershell
py app.py
```

也可以使用 Flask 命令运行：

```powershell
$env:FLASK_APP = "app.py"
py -m flask run
```

启动后在浏览器打开：

```text
http://127.0.0.1:5000
```

可访问页面：

- 首页：`/`
- 活动议程：`/agenda`
- 我要报名：`/register`
- Codex 教学：`/codex`

## 后续可以如何扩展

- 完善报名流程：增加提交成功页、字段校验、重复报名提示和本地数据查看方式。
- 优化活动页面：加入更清晰的移动端排版、活动时间地点、主讲人信息和常见问题。
- 扩展教学内容：加入更多可复制提示词、现场案例、分阶段任务模板和验收清单。
- 做多 Agent 演示：让 Content Agent 写内容，Frontend Agent 改视觉和交互，Backend Agent 处理报名保存与数据检查。
- 增加本地演示数据：准备几条模拟报名记录，方便线下活动现场展示完整流程。
