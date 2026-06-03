# aimeetup-kit

这是一个线下“普通人 AI 交流会”的最小 Flask 项目骨架。活动目标是帮助普通人理解并使用 Codex，把自己的想法逐步变成一个可运行的小工具。

当前版本只包含基础页面和路由，方便后续 Backend Agent、Frontend Agent、Content Agent 并行继续开发。

## 安装依赖

```powershell
py -m pip install -r requirements.txt
```

## 本地运行

```powershell
py app.py
```

也可以使用 Flask 命令运行：

```powershell
$env:FLASK_APP = "app.py"
py -m flask run
```

## 访问地址

启动后在浏览器打开：

```text
http://127.0.0.1:5000
```

可访问页面：

- 首页：`/`
- 活动议程：`/agenda`
- 我要报名：`/register`
- Codex 教学：`/codex`

## 后续开发建议

- Backend Agent：补充报名 POST、数据校验、保存到 `data/registrations.json`。
- Frontend Agent：优化响应式页面、视觉层级和移动端体验。
- Content Agent：完善活动文案、议程说明、Codex 教学内容和报名提示。
