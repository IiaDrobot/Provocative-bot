import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from bot.handlers import start, handle_buttons

ADMIN_ID = int(os.environ.get("ADMIN_ID", "0"))
completed_users = set()

async def stats(update, context):
    if update.effective_user.id != ADMIN_ID:
        return

    await update.message.reply_text(
        f"Прошли тест: {len(completed_users)}"
    )

def main():
    bot_token = os.getenv("BOT_TOKEN")

    if not bot_token:
        raise ValueError("BOT_TOKEN не найден!Проверь Railway Variables")

    app = Application.builder().token(bot_token).build()

    # handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CallbackQueryHandler(handle_buttons))

    print("Бот запущен...")

    app.run_polling()

if __name__ == "__main__":
    main()