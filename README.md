# ⏰ Notion → Discord Reminder Bot

A simple Python bot that checks your Notion database for upcoming tasks and sends reminders to your Discord server via a webhook — automatically.

---

## 📦 Features

- 🔄 Runs 24/7 (loop-based)
- 🔔 Sends Discord messages for tasks due within the next 30 minutes
- 🧠 Built for Notion databases with `Due Date` and `Status` fields
- 💬 Customizable interval and reminder window
- 🌐 Works great with Replit, Railway, or your own server

---

## 🛠️ Requirements

- Python 3.7+
- A Notion integration token
- A shared Notion database
- A Discord webhook URL

---

## 🧩 Notion Database Setup

Create a database with these properties:

| Property Name | Type   | Example      |
|---------------|--------|--------------|
| `Task`        | Title  | "Call Mom"   |
| `Due Date`    | Date   | 2025-08-04 14:30 |
| `Status`      | Select | "Not Done"   |

➡️ Make sure to invite your Notion integration to access the database!

---

## 🔐 Environment Variables

Create a `.env` file in the same directory:

```env
NTOKEN=your_notion_secret_token
DBID=your_database_id
DCWEBHOOK=your_discord_webhook_url
```

---

## 🚀 Run the Bot

```bash
pip install requests python-dotenv
python main.py
```

This will run the bot forever, checking for tasks due every 5 minutes (you can change the interval easily).

---

## ⚙️ Customize

- ⏳ To change how far ahead to check:
  ```python
  window = now + timedelta(minutes=30)
  ```

- ⏱ To change how often it checks:
  ```python
  time.sleep(300)  # 300 seconds = 5 minutes
  ```

---

## 📡 Hosting Suggestions

| Platform  | Works 24/7? | Notes |
|-----------|-------------|-------|
| 🌀 Replit   | ❌ (needs UptimeRobot or Flask) | Easy to set up |
| 🚆 Railway | ✅           | Great for long-running bots |
| 💻 Local PC | ✅           | But requires your machine on |

---

## 🧪 Example Discord Output

```
⏰ Reminder: Call Mom is due at 2025-08-04T14:30:00Z
```

---

## 🧼 License

MIT License — free to use, improve, and share!
