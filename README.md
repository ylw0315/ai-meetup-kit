# ai-meetup-kit

这是一个线下“普通人 AI 交流会”活动网站，用来演示如何使用 Codex 和多 Agent 协作，把一个简单活动需求拆成页面、表单、内容和 QA 验收。

项目是最小 Flask 应用，不调用 OpenAI API，不调用 Sora API，不调用任何外部 API，也不使用数据库。报名数据会追加保存到本地文件 `data/registrations.json`。

## 功能页面

- `/`：活动首页
- `/agenda`：活动议程
- `/register`：报名表
- `/codex`：Codex 入门说明

## 安装依赖

```powershell
py -m pip install -r requirements.txt
```

`requirements.txt` 只包含 Flask。

## 本地运行

```powershell
py app.py
```

启动后在浏览器打开：

```text
http://127.0.0.1:5000
```

也可以使用 Flask 命令运行：

```powershell
$env:FLASK_APP = "app.py"
py -m flask run
```

## 测试报名提交

打开 `http://127.0.0.1:5000/register`，填写并提交表单。表单会 POST 到 `/register`，字段包括：

- `name`
- `wechat`
- `occupation`
- `ai_experience`
- `learning_goal`

提交成功后，报名信息会追加写入 `data/registrations.json`。

也可以用 Flask test client 做一次快速检查：

```powershell
@'
from app import app, REGISTRATIONS_PATH

payload = {
    "name": "测试用户",
    "wechat": "test_wechat",
    "occupation": "活动参与者",
    "ai_experience": "chat",
    "learning_goal": "学习如何用 Codex 做小工具",
}

with app.test_client() as client:
    response = client.post("/register", data=payload)
    print(response.status_code)
    print(REGISTRATIONS_PATH.read_text(encoding="utf-8"))
'@ | py -
```
