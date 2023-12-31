import scripts.tools.config as config
import scripts.bot.handlers as handlers
import scripts.bot.menus    as menus
import scripts.bot.notify   as notify
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

def main():
    app_builder = ApplicationBuilder()
    app = app_builder.token(config.BOT_TOKEN).build()

    if app is not None:
        app.add_handler(MessageHandler(filters.Text(["АДМІНІСТРАТОР", "ВЧИТЕЛЬ"]), handlers.MessagesHandlerAdminTeacher))
        
        app.add_handler(CommandHandler("start", menus.Start))
        app.job_queue.run_repeating(notify.CheckAirDangerous, interval = 60, first = 0)
        app.add_handler(MessageHandler(filters.Text(), handlers.MessagesHandler))
        app.run_polling()
    else:
        print("Failed to create the application object.")

if __name__ == "__main__":
    main()