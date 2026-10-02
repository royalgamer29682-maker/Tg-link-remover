import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "8976392936"))

def is_owner(update: Update) -> bool:
    return bool(update.effective_user and update.effective_user.id == OWNER_ID)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot Online!\n\n"
        "Group management bot is running."
    )

async def groups(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_owner(update):
        return
    await update.message.reply_text("📊 Groups system अभी setup किया जाएगा.")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_owner(update):
        return
    if not context.args:
        await update.message.reply_text(
            "❌ Message लिखो.\n\nExample:\n/broadcast Hello everyone"
        )
        return
    message = " ".join(context.args)
    await update.message.reply_text(f"📢 Message received:\n\n{message}")

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN missing in .env")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("groups", groups))
    app.add_handler(CommandHandler("broadcast", broadcast))

    print("🤖 Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
