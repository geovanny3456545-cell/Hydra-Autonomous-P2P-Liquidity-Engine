import requests
import os

# Hydra Project - Telegram Secure Notifier
# (Public Version for Portfolio)

class SecureNotifier:
    """
    Encapsulates notification logic via Telegram Bot.
    """
    def __init__(self, token=None, chat_id=None):
        self.token = token or os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")
        self.api_url = f"https://api.telegram.org/bot{self.token}/sendMessage"

    def send(self, message, use_markdown=True):
        """Sends a message to the configured Telegram chat."""
        if not self.token or not self.chat_id:
            print(f"[Notifier - Dry Run]: {message}")
            return False
            
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown" if use_markdown else None
        }
        try:
            r = requests.post(self.api_url, json=payload, timeout=10)
            return r.status_code == 200
        except Exception as e:
            print(f"Error sending notification: {e}")
            return False

if __name__ == "__main__":
    notifier = SecureNotifier()
    notifier.send("✅ System operational.")
