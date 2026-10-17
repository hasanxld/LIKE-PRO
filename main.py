import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Paste your NEW BotFather token between the quotes below.
BOT_TOKEN = "8702203451:AAGDD_h2JdSjtr7RyCmjD2RX-t3SfvACUEk"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! 👋\nI am your simple Telegram bot. Send me a message and I will reply."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Commands:\n/start - Start the bot\n/help - Show this help message"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.message.text:
        await update.message.reply_text(f"You said: {update.message.text}")

def main() -> None:
    if not BOT_TOKEN or BOT_TOKEN == "PASTE_YOUR_NEW_BOT_TOKEN_HERE":
        raise SystemExit("Open app.py and paste your new BotFather token into BOT_TOKEN.")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running. Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
