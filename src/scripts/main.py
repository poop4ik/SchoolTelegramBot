import sys
sys.path.append("src/scripts/tools")
import config
import botFunctions
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

def main():
    app_builder = ApplicationBuilder()
    app = app_builder.token(config.BOT_TOKEN).build()

    if app is not None:
        app.add_handler(CommandHandler("start", botFunctions.start))
        app.add_handler(MessageHandler(filters.Text(), botFunctions.MessagesHandler))
        app.run_polling()
    else:
        print("Failed to create the application object.")

if __name__ == "__main__":
    main()