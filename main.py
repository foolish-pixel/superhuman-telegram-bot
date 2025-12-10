import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

user_levels = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Your Level System Bot is ready.\nUse /level or /train.")

async def level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if user_id not in user_levels:
        user_levels[user_id] = 1

    await update.message.reply_text(f"Your Level: {user_levels[user_id]}")

async def train(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if user_id not in user_levels:
        user_levels[user_id] = 1

    user_levels[user_id] += 1
    await update.message.reply_text(f"Training complete! New Level: {user_levels[user_id]}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("level", level))
app.add_handler(CommandHandler("train", train))

if __name__ == "__main__":
    app.run_polling()
