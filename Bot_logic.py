from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Function to handle script requests
def get_script(update: Update, context: CallbackContext) -> None:
    script_title = ' '.join(context.args).lower()
    if script_title in scripts:
        script_link = scripts[script_title]
        update.message.reply_text(f"Here is the link to download the script: {script_link}")
    else:
        update.message.reply_text("The script is not found or check your spelling.")

def main() -> None:
    # Your bot's API token
    token = 'YOUR_API_TOKEN'
    
    # Create the Updater and pass it your bot's token
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /getscript command
    dispatcher.add_handler(CommandHandler("getscript", get_script))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
