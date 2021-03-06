from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from telegram_bot.config import config_info
from telegram_bot.output.echoTest import button, en, de, echo, N_calc ,K_calc


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token=config_info.token,request_kwargs={'proxy_url': 'socks5h://127.0.0.1:1080/'} ,use_context = True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("EN", en))
    dp.add_handler(CommandHandler("DE", de))
    dp.add_handler(CommandHandler("N", N_calc))
    dp.add_handler(CommandHandler("K", K_calc))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    #dp.add_handler(MessageHandler(Filters.text & ~Filters.command, start))
    #updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()