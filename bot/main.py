import os


from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from bot.handlers import start, handle_buttons





def main():
    bot_token = os.getenv("BOT_TOKEN")

    if not bot_token:
        raise ValueError("BOT_TOKEN не найден в .env")

    app = Application.builder().token(bot_token).build()

    # handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))

    print("Бот запущен...")

    app.run_polling()


if __name__ == "__main__":
    main()