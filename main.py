import requests
from datetime import datetime, timedelta, timezone
import os
import dotenv
import time

# Load environment variables from .env file
dotenv.load_dotenv()

# Importent variables
NOTION_TOKEN = os.getenv("NTOKEN")
DATABASE_ID = os.getenv("DBID")
DISCORD_WEBHOOK_URL = os.getenv("DCWEBHOOK")


headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json", 
}

def get_due_tasks():
    now = datetime.now(timezone.utc)
    window = now + timedelta(minutes=30) # Change this to your likiing

    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    body = {
        "filter": {
            "and": [
                {
                    "property": "Due Date",
                    "date": {
                        "on_or_before": window.isoformat()
                    }
                },
                {
                    "property": "Status",
                    "select": {
                        "equals": "Not Done"
                    }
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=body)
    if not response.ok:
        print("❌ Notion API error:", response.status_code)
        print("🔍 Response body:", response.text)
        response.raise_for_status()
    return response.json()["results"]

def send_to_discord(task, due):
    message = {
        "content": f"⏰ **Reminder:** `{task}` is due at `{due}`"
    }
    requests.post(DISCORD_WEBHOOK_URL, json=message)

def main():
    tasks = get_due_tasks()
    for task in tasks:
        print("🔍 Found task:", task["id"])
        title = task["properties"]["Task"]["title"][0]["text"]["content"]
        due = task["properties"]["Due Date"]["date"]["start"]
        send_to_discord(title, due)

if __name__ == "__main__":
    print("🤖 Notion Reminder bot is running...")
    while True:
        try:
            main()
        except Exception as e:
            print("⚠️ Error:", e)
        time.sleep(300)  # Wait 5 minutes change this to your liking
