# 🔥 Telegram Fast Image Spammer Bot

A fast & safe Telegram group bot that sends messages with attached photos at near-max speed while respecting Telegram's flood limits.

> 🚀 Built and maintained by [@isyrae](https://github.com/isyrae)

---

## 📸 Features

- 📷 Sends messages **with image attachments** to a Telegram group
- 🚦 Smart rate limiter to avoid **flood bans**
- 🧠 Retry logic for handling Telegram/network errors
- 🔧 Simple configuration through `config.py`
- 🖥️ CLI-based logs and clean code layout

---

## 🛠️ Setup

```bash
git clone https://github.com/isyrae/Telegram-Spammer-Bot.git
cd Telegram-Spammer-Bot
pip install -r requirements.txt
python bot.py
```

---

## 🔧 Configuration

Open `config.py` and customize the following:

- `BOT_TOKEN`: Get this from @BotFather
- `GROUP_CHAT_ID`: Add your Telegram group’s chat ID
- `MESSAGE_TEXT`: Customize the message that will be sent with the image
- `PHOTO_PATH`: Update the image file name/path
- `MAX_MESSAGES_PER_MINUTE`: Change this to control how fast the bot sends messages (18 is Telegram-safe)

---

## ⚠️ Disclaimer

This bot is intended for **educational and personal use only**.

- ❌ Do **not** use it to spam public or unauthorized groups
- ⚠️ Misuse can result in your **bot being banned** by Telegram

Use responsibly.

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.

You are free to use, modify, and redistribute this bot — but:
- You **must credit** the original author
- Any modified or derived versions **must also be open-sourced**

[📖 Read the full license here](LICENSE)

---

## 👑 Author

- GitHub: [@isyrae](https://github.com/isyrae)
- Telegram: [@isyrae](https://t.me/isyrae)

---

## 💌 Contributions & Feedback

Have an idea or improvement?  
Feel free to open an issue or submit a pull request!  
Let’s keep it ethical, open, and fun 🔥
