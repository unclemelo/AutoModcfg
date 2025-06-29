# AutoModcfg
A helpful, open-source AutoMod preset system for Discord — powered by `discord.py` and Discord’s built-in AutoMod features.

Whether you're running a small friend group or a large community, our goal is to help you set up smart moderation *without* needing to learn complex regex or spend hours configuring filters.

---

## 🛠️ Setting Up the Project

### 1. Create a Virtual Environment
Keeps your dependencies clean and isolated.

```bash
python3 -m venv venv
```

### 2. Activate It
```bash
source venv/bin/activate
```

✅ Your Python environment is now active.

---

## 📦 Install Requirements

Install the libraries used by the bot:

```bash
pip install -r requirements.txt
```

---

## 🔐 Create a `.env` File

This is where your secret credentials go. Create a file named `.env` in the root folder and add:

```
TOKEN=your_discord_bot_token
WEBHOOK=your_webhook_url_if_applicable
```

Never share this file — it contains sensitive data!

---

## ▶️ Run the Bot

Once everything’s set, launch the bot with:

```bash
python3 bot.py
```

You should see it come online in your Discord server.

---

## 🧠 Skip the Regex, Use Presets

Let us handle the complicated parts.  
Instead of making your mods write and test regex manually, our system provides curated presets that plug directly into **Discord’s native AutoMod** system using the official API.

✅ Works great for profanity, scam links, spam patterns, and more  
✅ Easy to apply with a single command  
✅ Saves time and prevents errors

---

### 💬 Need Help?

We're constantly improving and adding presets based on real community needs.  
If you have questions or want to contribute your own filters, feel free to open an issue or join our support server.