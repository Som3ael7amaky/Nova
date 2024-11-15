import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# إعداد تسجيل الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# دالة start التي سيتم تنفيذها عند كتابة الأمر /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحباً! أنا بوت تليجرام.')

# دالة مخصصة لتنفيذ أمر /help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('استخدم /start لبدء التفاعل معي.')

def main() -> None:
    # هنا ضع التوكن الخاص بالبوت
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)

    # الحصول على الموزع
    dispatcher = updater.dispatcher

    # إضافة معالجات للأوامر
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()